import os
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length, Email, EqualTo, ValidationError

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"

if __name__ == "__main__":
    app.run(debug="True")