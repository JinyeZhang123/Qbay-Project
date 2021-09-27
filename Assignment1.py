from flask_login import UserMixin
from sqlalchemy.sql import func
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    # user's id
    id = db.Column(db.Integer, primary_key=True)
    # user's username
    username = db.Column(db.String(80), unique=True, nullable=False)
    # user's email
    email = db.Column(db.String(120), unique=True, nullable=False)
    # user's password
    password = db.Column(db.String(150), unique=False, nullable=False)
    # user's balance
    balance = db.Column(db.Float)
    def __repr__(self):
        return '<User %r>' % self.username

class Credit(db.Model):
    # id for this credite purchase
    id = db.Column(db.Integer, primary_key=True)
    # amount of this purchase
    creditamount = db.Column(db.Float)
    # comment for this purchase
    creditcomment = db.Column(db.String(9999))
    # date of the purchase
    date = db.Column(db.DateTime(timezone=True), default=func.now())
