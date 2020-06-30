from flask import Flask
from flask import jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from setup_modules import User, Inventory, db, app


# Routes of the website
@app.route('/')
def home():
    return 'This is the homepage'

@app.route('/add_user')
def add_user():
    name = request.args.get('name')
    age = request.args.get('age')
    sex = request.args.get('sex')
    if name and age and sex:
        new_user = User(name, age, sex)
        db.session.add(new_user)
        db.session.commit()
        return 'User ' + str(name) + ' has been created!'
    else:
        'No user added'

@app.route('/all_users')
def show_users():
    users = User.query.all()
    return jsonify(str(users))

@app.route('/inventory')
def show_inventory():
    inv = Inventory.query.all()
    return jsonify(str(inv))
