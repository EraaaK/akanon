from flask import Flask

app = Flask(__name__)


@app.route('/')
def raiz():
    return "Olá"


app.run()
