# Coloquei o 'todos' aqui pois não estava sabendo fazer importação de outro arquivo para renderizar
todos = [
    {1 : "Levar o gato para passear"},
    {2 : "Comprar tinta spray"},
    {3 : "Estudar Node"},
    {4 : "Estudar Ruby"},
    {5 : "Terminar validação de eventos API do Im Here"},
    {6 : "Fazer salvamento local dos dados da API em SQLite no próprio app android"}
]

from flask import Blueprint, render_template

routes_bp = Blueprint("routes", __name__)

@routes_bp.route("/")
def index():
    return render_template("index.html", page_title='Início')

@routes_bp.route("/lista-tarefas")
def listaTarefas():
    return render_template("listar.html", page_title='Lista de Tarefas', todos=todos)

@routes_bp.route("/adicionar-tarefa")
def adicionarTarefa():
    return render_template("adicionar.html", page_title='Adicionar Tarefas')

@routes_bp.route("/concluir-tarefa/<id>")
def concluirTarefa():
    return render_template("concluir.html", page_title='Concluir Tarefas')

@routes_bp.route("/excluir-tarefa/<id>")
def excluirTarefa(): 
    return render_template("excluir.html", page_title='Excluir Tarefas')
