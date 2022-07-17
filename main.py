from flask import Flask, render_template
from api import InboxAPI

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


app.run()
