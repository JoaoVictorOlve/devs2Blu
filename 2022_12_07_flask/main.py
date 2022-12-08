from flask import Flask, render_template
from pessoa import Pessoa

app = Flask(__name__)



@app.route('/')
def inicio():
    pessoa1 = Pessoa('Haiko', '17', '1.50')
    pessoa2 = Pessoa('Jean', '42', '1:84')
    pessoa3 = Pessoa('Gisele', '16', '1:30')
    pessoa4= Pessoa('Leandro', '27', '1:94')

    lista = [pessoa1, pessoa2, pessoa3, pessoa4]
    return render_template('index.html', titulo='Gerola', pessoas = lista)

@app.route('/new')
def novo():
    return 'New Route'

app.run()