from flask_script import Command
from test_app import db

class InitDB(Command):
    def run(self):
        db.create_all()

class DropDB(Command):
    def run(self):
        db.drop_all()