from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')  # Assuming you have a config.py for app settings

db = SQLAlchemy(app)

from app import views
