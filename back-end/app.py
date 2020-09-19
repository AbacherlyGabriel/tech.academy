import secrets

from flask import Flask, session, flash, redirect, render_template, request

app = Flask(__name__)
secret = secrets.token_urlsafe(32)
app.secret_key = secret


@app.route('/')
def home():
    return '<h1>Home<h1>'


@app.route('/login')
def login():
    return '<h1>Login</h1>'


@app.route('/autenticar', methods=['POST'])
def autenticar():
    session['usuario_logado'] = 'user'
    return redirect('/login')


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    return '<h1>Logout</h1>'


app.run()
