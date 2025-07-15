from flask import Flask
from flask import render_template as rt #renderizar o html

app = Flask(__name__)

@app.route("/") #rota raiz flask
def home():
    return rt("main.html", tarefas=tarefas) #return do html main

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)