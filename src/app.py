import os

from flask import Flask, session, flash, redirect, render_template, request, send_from_directory
from dao import UserDao

app = Flask(__name__)
secret = os.environ.get('SESSIONKEY')
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
    session.modified = True
    return redirect('/')


@app.route('/autenticar', methods=['POST'])
def autenticar():
    if (user.read(request.form['email'], request.form['senha'])):
        session['usuario_logado'] = user.nome
        session.modified = True
        return redirect('/perfil')
    else:
        flash("Email ou senha incorretos")
        return redirect('/login')


@app.route('/perfil')
def visualizar_perfil():
    return render_template('profile.html')


@app.route('/criar', methods=['POST'])
def criar():
    if (user.create_user(request.form['email'], request.form['nome'], request.form['senha'], request.form['valida_senha'])):
        session['usuario_logado'] = request.form['nome']
        return redirect('/perfil')
    else:
        flash(user.message)
        return redirect('/register')


@app.route('/buscar', methods=['POST'])
def buscar():
    docs = user.query_by_description(request.form['description'])
    results = []
    for curso in docs:
        results.append(curso)
    return render_template('busca.html', results=results, query=request.form['description'])


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/avaliacoes')
def avaliacoes():
    return render_template('avaliacoes.html')


@app.route('/forum')
def forum():
    return render_template('forum.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')