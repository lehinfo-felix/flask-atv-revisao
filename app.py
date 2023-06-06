from flask import Flask

from routes.routes import routes_bp

app = Flask(
    __name__,
    static_folder="static",
    template_folder="templates")

app.register_blueprint(routes_bp)

if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0")
