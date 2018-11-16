from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flaskapp.model_base import ModelBase

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app, model_class=ModelBase)

from flaskapp import views
