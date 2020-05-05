from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, current_user, logout_user
#from app.users import User
#from app.forms import RegistrationForm, LoginForm, UpdateAccountForm
from app import app


@app.route('/')
@app.route('/home')
def index():
    return "<h1>hello</h1>"

@app.route('/about')
def about():
    return "<h1>about</h1>"

