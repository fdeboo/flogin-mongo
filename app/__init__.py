import os
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_login import LoginManager

mongo = mongo.db. 
login_manager = LoginManager()
login_manager.login.view = 'login'
login_manager.login_message_category = 'info'

app = Flask(__name__)