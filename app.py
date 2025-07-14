from flask import Flask
from flask import render_template as rt #renderizar o html

app = Flask(__name__)

@app.route("/") #rota raiz flask
def home():
    return rt("main.html") #return do html main

