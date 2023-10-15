from flask import Flask
from flask_sqlalchemy import SQLAlchemy
print("Before importing MigrateCommand")
from flask_migrate import Migrate, MigrateCommand
print("After importing MigrateCommand")

from flask_script import Manager
import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
