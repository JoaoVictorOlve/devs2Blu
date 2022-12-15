from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy

#============================================================================================================================

app = Flask(__name__)
app.secret_key = 'moredevs'

app.config['SQLALCHEMY_DATABASE_URI'] = '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
    SGBD = 'postgresql',
    usuario = "teste",
    senha = "123456",
    servidor = "localhost:5435",
    database = "postgres"
)

#============================================================================================================================

db = SQLAlchemy(app)

class Funcionarios(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    altura = db.Column(db.Float, nullable=False)

    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def __repr__(self):
        return '<Name %r>' % self.name

class Usuarios(db.Model):
    nickname = db.Column(db.String(8), primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

#============================================================================================================================
lista = Funcionarios.query.order_by(Funcionarios.id)

@app.route('/') #FEITO
def index():
    return render_template('login.html', titulo='Login')

@app.route('/list') #FEITO
def list():
    lista = Funcionarios.query.order_by(Funcionarios.id)
    return render_template("list.html", titulo = 'jogos', pessoas = lista)


@app.route('/novo') #FEITO
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login', proximo = url_for('/novo'))
    else:
        return render_template('novo.html', titulo = 'Cadastro Funcionario')



@app.route('/criar', methods = ['POST']) #FEITO
def criar():
    nome = request.form['nome']
    idade = request.form['idade']
    altura = request.form['altura']

    cad_funcionario = Funcionarios(nome, idade, altura)

    lista.append(cad_funcionario)

    return redirect(url_for('list'))

@app.route('/login') #FEITO
def login():
    proximo = request.args.get('proximo')
    return render_template('login.html', titulo='Login Usuario', proximo=proximo)

@app.route('/autenticacao', methods=['POST'])
def autenticar():
    usuario = Usuarios.query.filter_by(nickname=request.form['usuario']).first()
    if usuario:
        
        if request.form['senha'] == usuario.senha:

            session['usuario_logado'] = usuario.nickname
            

            flash(usuario.nickname + 'logado com sucesso')

            proxima_pagina = request.form['proximo']

            return redirect(proxima_pagina)

    else:
        flash('usuario ou senha incorretos tente novamente')
        #dinamizando url

        return redirect(url_for('login'))

@app.route('/logout') #FEITO
def logout():
    session['usuario_logado'] = None
    flash('Você foi desconectado!')
    return redirect('/login')

app.run(debug=True)
