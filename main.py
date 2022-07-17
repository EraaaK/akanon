import sqlite3
from flask import Flask, render_template

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def home():
    conn = get_db_connection()
    tickets = conn.execute('SELECT * from tickets').fetchall()
    conn.close()
    return render_template('index.html', tickets=tickets)


app.run()
