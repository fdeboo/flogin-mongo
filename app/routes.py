from flask import render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash
from flask_login import current_user
from app.modules import User
from app.forms import RegistrationForm, LoginForm
from app import app, mongo 


@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    users = mongo.db.users
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        users.insert({'username': form.username.data, 'email': form.email.data, 'password': hashed_password, 'picture': None})
        flash('You are now registered and can log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

