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

# Relational Database Model 3
class Item_status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    status = db.Column(db.String(10))

    def __init__(self, name, status):
        item = Inventory.query.filter_by(name=name).first()
        if item is not None:
            self.id = item.id
            self.name = name
            self.status = status
        else:
            print('That item doesnt exist in the inventory')
    def __repr__(self):
        return str(self.id) + '|' + str(self.name) + '|' + 'status: ' + str(self.status)

# Student Class
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return str(self.id) + '|' + str(self.name)

# Subject Class
class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return str(self.id) + '|' + str(self.name)

# Student --> Subject Class
class StudentSubject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_student = db.Column(db.Integer)
    id_subject = db.Column(db.Integer)

    def __init__(self, id_student, id_subject):
        self.id_student = id_student
        self.id_subject = id_subject

    def __repr__(self):
        student = Student.query.filter_by(id=self.id_student).first()
        subject = Subject.query.filter_by(id=self.id_subject).first()
        if student is not None and subject is not None:
            return str(self.id) + '|' + 'ID:' + str(self.id_student) + '|' + str(student.name) + '<---viewing--->' + 'ID:' + str(self.id_subject) + '|' + str(subject.name)
        elif student is None:
            return 'That student id doesnt exist, delete this entry. (ID=)' + str(self.id)
        elif subject is None:
            return 'That subject id doesnt exist, delete this entry. (ID=)' + str(self.id)

# Teacher Class
class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    subject_id = db.Column(db.String(50))

    def __init__(self, name, subject_id):
        self.name = name
        self.subject_id = subject_id

    def __repr__(self):
        subject = Subject.query.filter_by(id=self.subject_id).first()
        return str(self.id) + '|' + str(self.name) + '<---teaching--->' + 'ID:' + str(self.subject_id) + '|' + str(subject.name)
