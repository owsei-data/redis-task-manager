from flask import Blueprint, render_template

bp = Blueprint('route', __name__, template_folder='../templates') #cria a bp

#rota raiz
@bp.route('/')
def home():
    return render_template('main.html')