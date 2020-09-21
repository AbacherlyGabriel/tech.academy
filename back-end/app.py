import secrets

from flask import Flask, session, flash, redirect, render_template, request

app = Flask(__name__)
secret = secrets.token_urlsafe(32)
app.secret_key = secret


@app.route('/')
def home():
    session['usuario_logado'] = None
    return render_template('index.html')


@app.route('/register')
def registrar():
    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autenticar', methods=['POST'])
def autenticar():
    session['usuario_logado'] = 'user'
    return redirect('/perfil')


@app.route('/perfil')
def visualizar_perfil():
    return render_template('profile.html')


@app.route('/criar', methods=['POST'])
def criar():
    return redirect('/perfil')


app.run(debug=True)
