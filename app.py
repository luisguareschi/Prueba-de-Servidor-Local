from flask import Flask
from flask import jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from setup_modules import User, Inventory, db, app
from routes import home
# Run the database
db.create_all()

home() #runs all the routes in modules.py

# Function to print all entries in the model, ONLY WORKS on the TERMINAL
def show_all(model):
    all_info = model.query.all()
    for i in all_info:
        print(i)

# Function to add data faster, ONLY WORKS on the TERMINAL
def add(item, directory):
    db.session.add(item)
    db.session.commit()
    if validate_all_data():
        print('ERROR')
    else:
        print('New entry added:')
        show_all(directory)

# Function to delete data faster, ONLY WORKS on the TERMINAL
def delete(item_id, directory):
    data = directory.query.get(item_id)
    db.session.delete(data)
    db.session.commit()
    print(data.name, 'deleted successfully')

### Functions to validate the format of the data
def validate_name(model):
    all_info = model.query.all()
    for i in all_info:
        if i.name[0] in 'QWERTYUIOPASDFGHJKLZXCVBNM' and type(i.name) == str:
            pass
        else:
            db.session.delete(i)
            db.session.commit()
            print('The data', i, 'has a bad name format')
            return True

def validate_sex(model):
    all_info = model.query.all()
    for i in all_info:
        if i.sex[0] in 'QWERTYUIOPASDFGHJKLZXCVBNM' and type(i.sex) == str:
            pass
        else:
            db.session.delete(i)
            db.session.commit()
            print('The data', i, 'has a bad sex format')
            return True

def validate_age(model):
    all_info = model.query.all()
    for i in all_info:
        if i.age > 0 and type(i.age) == int:
            pass
        else:
            db.session.delete(i)
            db.session.commit()
            print('The data', i, 'has a bad age format')
            return True

def validate_amount(model):
    all_info = model.query.all()
    for i in all_info:
        if i.amount > 0 and type(i.amount) == int:
            pass
        else:
            db.session.delete(i)
            db.session.commit()
            print('The data', i, 'has a bad amount format')
            return True

def validate_all_data():
    if validate_name(User) or validate_age(User) or validate_sex(User) or validate_amount(Inventory) or validate_name(Inventory):
        return True

# Running the functions
validate_all_data()
# Run the server
app.run()


