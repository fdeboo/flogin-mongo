from flask import render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash
from flask_login import current_user
from app.modules import User
from app.forms import RegistrationForm
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
    if form.validate_on_submit():
        users = mongo.db.users
        existing_user = users.find_one({'email': request.form['email']})
        if existing_user is None:
            hashed_password = generate_password_hash(form.password.data)
            user = User(username=form.username.data, email=form.email.data, password=hashed_password)
            users.insert({'name': form.username.data, 'email': form.email.data, 'password': hashpass})
            session['username'] = form.username.data
            flash('You are now registered and can log in', 'success')
            return redirect(url_for('login'))
        flash('That email already exists!', 'danger')
    return render_template('register.html', form=form)


@app.route('/login')
def login():
    return render_template('login.html')

