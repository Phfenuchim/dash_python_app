# app/controllers/auth_controller.py
from flask import Blueprint, render_template, request, redirect, session
from app.services.db_service import get_db_connection
import bcrypt

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def home():
    return render_template('home.html')

@auth_bp.route('/login', methods=['GET'])
def login_form():
    return render_template('login.html')

@auth_bp.route('/login', methods=['POST'])
def login():
    email = request.form.get('username')
    password = request.form.get('password')

    try:
        conn = get_db_connection()
        if not conn:
            return render_template('login.html', erro='Erro ao conectar com o banco')

        cursor = conn.cursor()
        cursor.execute("SELECT SenhaHash FROM users WHERE email = ?", (email,))
        resultado = cursor.fetchone()

        if resultado and bcrypt.checkpw(password.encode(), resultado[0].encode()):
            session['usuario'] = email
            return redirect('/dash')
        else:
            return render_template('login.html', erro='Usuário ou senha inválidos')

    except Exception as e:
        print("Erro ao consultar o banco:", e)
        return render_template('login.html', erro='Erro interno')

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/')
