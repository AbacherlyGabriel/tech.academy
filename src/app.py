import secrets

from flask import Flask, session, flash, redirect, render_template, request
from dao import UserDao

app = Flask(__name__)
secret = secrets.token_urlsafe(32)
app.secret_key = secret
user = UserDao()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register')
def registrar():
    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    return redirect('/')


@app.route('/autenticar', methods=['POST'])
def autenticar():
    if (user.read(request.form['email'], request.form['senha'])):
        session['usuario_logado'] = user.nome
        return redirect('/perfil')
    else:
        flash("Email ou senha incorretos")
        return redirect('/login')


@app.route('/perfil')
def visualizar_perfil():
    return render_template('profile.html')


@app.route('/criar', methods=['POST'])
def criar():
    if (user.create(request.form['email'], request.form['nome'], request.form['senha'], request.form['valida_senha'])):
        session['usuario_logado'] = request.form['nome']
        return redirect('/perfil')
    else:
        flash(user.message)
        return redirect('/register')


app.run()