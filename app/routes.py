from flask import render_template, redirect, url_for, request, flash
#from flask_login import login_user, login_required, current_user, logout_user
#from app.modules import User
from app.forms import RegistrationForm, LoginForm, UpdateAccountForm
from app import app


@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', form=form)

