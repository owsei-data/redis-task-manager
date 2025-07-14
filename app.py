from flask import Flask
from flask import render_template as rt #renderizar o html
import redis_client

app = Flask(__name__)

@app.route("/") #rota raiz flask
def home():
    tarefas = redis_client.mostrar_tarefas()
    return rt("main.html", tarefas=tarefas) #return do html main

