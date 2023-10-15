import os
from sqlalchemy import create_engine

# BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DATABASE_URL = 'postgresql+psycopg2://postgres:Hydroxide2@parkor-test.cysrviwivbqg.us-east-2.rds.amazonaws.com:5432/parkor-test'
engine = create_engine(DATABASE_URL, echo=True)
# SQLite for simplicity, but you might want to change this to PostgreSQL, MySQL, etc.
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
# SQLALCHEMY_TRACK_MODIFICATIONS = False
# SECRET_KEY = 'YourSecretKeyHere'  # Change this!
