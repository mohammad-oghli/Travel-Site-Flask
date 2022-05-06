from os import environ
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-secret-key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
# for deployment requirements on heroku
# uri = environ.get('DATABASE_URL') or 'sqlite:///my_database.db'
# if uri and uri.startswith("postgres://"):
#     uri = uri.replace("postgres://", "postgresql://", 1)
# app.config['SQLALCHEMY_DATABASE_URI'] = uri
db = SQLAlchemy(app)

login = LoginManager()
login.init_app(app)
login.login_view = 'login'

import routes, models