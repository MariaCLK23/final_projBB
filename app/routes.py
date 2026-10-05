from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db
from .models import Participant

main = Blueprint('main', __name__)

@main.get('/')
def home():
    return render_template('home.html')

@main.post('/cadastro')
def cadastro():
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    if not name or not email or '@' not in email:
        flash('Preencha os campos para continuar.', 'error')
        return redirect(url_for('main.home') + '#inscricao')
    try:
        db.session.add(Participant(name=name, email=email))
        db.session.commit()
    except Exception:
        db.session.rollback()
        flash('Não foi possivel concluir a simulação. Tente novamente.', 'error')
        return redirect(url_for('main.home') + '#inscricao')
    return redirect(url_for('main.sucesso'))

@main.get('/sucesso')
def sucesso():
    return render_template('success.html')

@main.get('/seguranca')
def seguranca():
    return render_template('security.html')
