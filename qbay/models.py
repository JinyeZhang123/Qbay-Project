# model 

import re

from qbay import app
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

'''
This file defines data models and related business logics
'''

# define a global variable for checking valid email address
regex = '^[a-z0-9]+[._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
db = SQLAlchemy(app)


class User(db.Model):
    username = db.Column(
        db.String(80), nullable=False)
    email = db.Column(
        db.String(120), unique=True, nullable=False,
        primary_key=True)
    password = db.Column(
        db.String(120), nullable=False)
    address = db.Column(
        db.String(150), unique=False)
    postcode = db.Column(
        db.String(20), unique=False)
    balance = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


# create all tables
db.create_all()


#register function ----------------------------------
def register(name, email, password):
    '''
    Register a new user
      Parameters:
        name (string):     user name
        email (string):    user email
        password (string): user password
      Returns:
        True if registration succeeded otherwise False
    '''
    # R1-1: Both the email and password cannot be empty.
    # if empty input
    if len(email) == 0 or len(password) == 0:
        return False
    # if not valid email format
    if re.fullmatch(regex, email) is None:
        return False
    # password too short
    if len(password) < 6:
        return False
    # password all lower
    if password.islower():
        return False
    # password all upper
    if password.isupper():
        return False
    # validate password (for special chars)
    regexp = re.compile('[^0-9a-zA-Z]+')
    if not regexp.search(password):
        return False
    # empty name
    if len(name) < 0:
        return False
    # validate name (special chars)
    # delete all spaces to check special chars only (check prefix or suffix later)
    nametrimed = name.replace(' ', '')
    if re.search("^[a-zA-Z0-9 ]*$", nametrimed) is None:
        return False
    # space allowed only if it is not as the prefix or suffix
    if name.find(' ') == 0 or name.find(' ') == (len(name) - 1):
        return False
    # length limit of name
    if len(name) <= 2 or len(name) >= 20:
        return False
    # check if the email has been used:
    existed = User.query.filter_by(email=email).all()
    # if by email not found
    if len(existed) > 0:
        return False

    # create a new user
    user = User(username=name, email=email, password=password, address=None, postcode=None, balance=100.0)
    # add it to the current database session
    db.session.add(user)
    # actually save the user object
    db.session.commit()

    return True

#-------------
#login-related


def login(email, password):
    '''
    Check login information
      Parameters:
        email (string):    user email
        password (string): user password
      Returns:
        The user object if login succeeded otherwise None
    '''
    # if empty input
    if len(email) == 0 or len(password) == 0:
        return None
    # if not valid email format
    if re.fullmatch(regex, email) is None:
        return None
    # password too short
    if len(password) < 6:
        return None
    # if all lower
    if password.islower():
        return None
    # if all upper
    if password.isupper():
        return None
    # check valid email
    regexp = re.compile('[^0-9a-zA-Z]+')
    if regexp.search(password) is None:
        return None

    # fetch out an entity with matched email and password
    valids = User.query.filter_by(email=email, password=password).all()
    if len(valids) != 1:
        return None
    return valids[0]
