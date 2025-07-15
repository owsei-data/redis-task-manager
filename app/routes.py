from flask import blueprints, render_template

bp = Blueprint('route', __name__) #cria a bp

#rota raiz
@bp.route('/')
def home():
    return render_template('main.html')