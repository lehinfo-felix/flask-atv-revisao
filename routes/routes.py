from flask import Blueprint, render_template, request, redirect

from data.data import todos

routes_bp = Blueprint("routes", __name__)

@routes_bp.route("/")
def index():
    return render_template("index.html", page_title='Início')

@routes_bp.route("/lista-tarefas")
def listaTarefas():
    return render_template("listar.html", page_title='Lista de Tarefas', todos=todos)

@routes_bp.route("/adicionar-tarefa", methods=["GET", "POST"])
def adicionarTarefa():
    if request.method == 'POST':
        if request.form['to-do'] == '':
            return render_template("adicionar.html", page_title='Adicionar Tarefas', error='Campo obrigatório')
        todo = request.form['to-do']
        todo = {
            'id': len(todos) + 1,
            'name': todo,
            'completed': False
        }
        todos.append(todo)

    return render_template("adicionar.html", page_title='Adicionar Tarefas')

@routes_bp.route("/concluir-tarefa/<int:id>", methods=["POST"])
def concluirTarefa(id):
    for todo in todos:
        if todo['id'] == int(id):
            if todo['completed'] == False:
                todo['completed'] = True
            else:
                todo['completed'] = False
            break
    return redirect('/concluir-tarefa')

@routes_bp.route("/concluir-tarefa", methods=["GET"])
def concluirTarefaGet():
    return render_template("concluir.html", page_title='Concluir Tarefas', todos=todos)

@routes_bp.route("/excluir-tarefa", methods=["GET"])
def excluirTarefaGet():
    return render_template("excluir.html", page_title='Excluir Tarefas', todos=todos)

@routes_bp.route("/excluir-tarefa/<int:id>", methods=["POST"])
def excluirTarefa(id):
    for todo in todos:
        if todo['id'] == int(id):
            todos.remove(todo)
            break
    for i, todo in enumerate(todos):
        todo['id'] = i + 1
    return redirect('/excluir-tarefa')
