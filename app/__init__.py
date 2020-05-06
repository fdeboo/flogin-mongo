import os
from flask import Flask
from config import Config
from flask_pymongo import PyMongo
from flask_login import LoginManager

app = Flask(__name__)

app.config.from_object(Config)
mongo = PyMongo(app)
login_manager = LoginManager(app)
login_manager.login.view = 'login'
login_manager.login_message_category = 'info'

from app import routes