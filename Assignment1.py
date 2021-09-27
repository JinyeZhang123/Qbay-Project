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

class Transaction(db.Model):
    # the id of the transaction(marked individually)
    id = db.Column(db.Integer, primary_key=True)
    # name of the product
    prodectname = db.Column(db.String(80), unique=True, nullable=False)
    # amount of the transaction
    amount = db.Column(db.Float)
    # date of the transaction
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # status of the transaction (buy/sell)
    status = db.Column(db.String(80), unique=True, nullable=False)
    # payment status (in process/complete)
    payment = db.Column(db.Float)
    # review for this product
    review = db.Column(db.String(9999))
    # relate to shipment information      
    shipment = db.relationship('Shipment')
    # relate to product information
    product = db.relationship('Product')
    # relate this model back to user
    User_id = db.Column(db.Interger, db.ForeignKey('user.id'))

class Shipment(db.Model):
    # id of shipment
    id = db.Column(db.Integer, primary_key=True)
    # shipment status (prepare/on the way/arrived)
    status = db.Column(db.String(80), unique=False, nullable=False)
    # shiipping address
    address = db.Column(db.String(200), unique=False, nullable=False)
    # tracking information
    trackdown = db.Column(db.String(200), unique=False, nullable=False)
    # relate this model to transaction
    Shipment_id = db.Column(db.Interger, db.ForeignKey('transaction.id'))