from flask import Flask

def criar_app(): #construtor
    app = Flask(__name__)

    from .routes import bp as routes_bp #importando routes.py
    app.register_blueprint(routes_bp) #registrando no flask

    return app #retorna configuracoes