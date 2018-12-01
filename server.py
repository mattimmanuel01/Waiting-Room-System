from flask import Flask
from flask_login import LoginManager
from src.system import *
import csv
import datetime


app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'Another_highly_secret_key'

# Initiate login clas
login_manager = LoginManager()
login_manager.init_app(app)

# Initiate system class
sys = System()

