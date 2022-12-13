from flask import Flask, render_template, request, redirect, session, flash
from pessoa import Pessoa

lista = []

app = Flask(__name__)
app.secret_key = 'moredevs'

@app.route('/')
def index():
    return render_template('login.html', titulo='Login')

