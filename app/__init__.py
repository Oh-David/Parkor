import os
import sys
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config.from_object('Parkor.config')  # Assuming you have a config.py for app settings

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/David/Documents/Parkor/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'YourSecretKeyHere'  # Change this!


print(app.config['SQLALCHEMY_DATABASE_URI'])

print(sorted(sys.modules.keys()))

db = SQLAlchemy(app)
print(db)

from app import views
migrate = Migrate(app, db)