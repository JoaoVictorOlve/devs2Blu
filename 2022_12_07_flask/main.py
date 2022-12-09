from flask import Flask, render_template, request, redirect
from pessoa import Pessoa

pessoa1 = Pessoa('Haiko', '17', '1.50')
pessoa2 = Pessoa('Jean', '42', '1.84')
pessoa3 = Pessoa('Leandro', '27', '1.94')

lista = [pessoa1, pessoa2, pessoa3]

#
app = Flask(__name__)



#
@app.route('/')
def index():
    return render_template('index.html', titulo='Lista' ,pessoas = lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo = 'Cadastro Pessoa')


@app.route('/criar', methods = ['POST'])
def criar():
    nome = request.form['nome']
    idade = request.form['idade']
    altura = request.form['altura']

    cad_pessoa = Pessoa(nome, idade, altura)

    lista.append(cad_pessoa)

    return redirect('/')

app.run(debug=True)

