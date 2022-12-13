from flask import Flask, render_template, request, redirect, session, flash, url_for
from pessoa import Pessoa
from usuario import Usuario

pessoa1 = Pessoa('Haiko', '17', '1.50')
pessoa2 = Pessoa('Jean', '42', '1.84')
pessoa3 = Pessoa('Leandro', '27', '1.94')

lista = [pessoa1, pessoa2, pessoa3]

usuario1 = Usuario('andre','vitor','moredevs')
usuario2 = Usuario('felipe','weiis','123456')
usuario3 = Usuario('larissa','sebold','654321')

usuarios = { 
    usuario1.nickname: usuario1,
    usuario2.nickname: usuario2,
    usuario3.nickname: usuario3
}

app = Flask(__name__)
app.secret_key = 'moredevs'

@app.route('/')
def index():
    return render_template('login.html', titulo='Login')

@app.route('/list')
def list():
    return render_template('list.html', titulo='Lista', pessoas = lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login')
    else:
        return render_template('novo.html', titulo = 'Cadastro Pessoa')


@app.route('/criar', methods = ['POST'])
def criar():
    nome = request.form['nome']
    idade = request.form['idade']
    altura = request.form['altura']

    cad_pessoa = Pessoa(nome, idade, altura)

    lista.append(cad_pessoa)

    return redirect(url_for('list'))

@app.route('/login')
def login():
    proximo = request.args.get('proximo')
    return render_template('login.html', titulo='Login Usuario', proximo=proximo)

@app.route('/autenticacao', methods=['POST'])
def autenticacao():
    if request.form['usuario'] in usuarios:

        usuario = usuarios[request.form['usuario']]

        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname

            flash(usuario.nickname + 'Deu Boa')
            proxima_pagina = request.form['proximo']
            return redirect(proxima_pagina)
    else:
        flash('Usuario ou senha invalidos')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Você foi desconectado!')
    return redirect('/login')

app.run(debug=True)
