from flask import Flask
from flask import jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Set the website
app = Flask('__name__')
app.config['DEBUG'] = True
# Set the Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'  # Location of the Database
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Model 1
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    sex = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __repr__(self):
        return str(self.id) + '|' + str(self.name) + '|' + str(self.age) + '|' + str(self.sex) + '|(created at)' + str(
            self.date_created)

# Database Model 2
class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    amount = db.Column(db.Integer)

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __repr__(self):
        return str(self.id) + '|' + str(self.name) + '|' + 'amount: ' + str(self.amount)
