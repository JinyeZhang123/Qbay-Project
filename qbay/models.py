# model file 

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


class Product(db.Model):
    title = db.Column(
        db.String(80), unique=True, nullable=False, primary_key=True)
    description = db.Column(
        db.String(2000), nullable=False)
    price = db.Column(
        db.Float, nullable=False)
    date = db.Column(
        db.String(80), nullable=False)
    owner_email = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<Product %r>' % self.title


# create all tables
db.create_all()


# register function
def register(name, email, password):
    """
    Register a new user
      Parameters:
        name (string):     user name
        email (string):    user email
        password (string): user password
      Returns:
        True if registration succeeded otherwise False
    """
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
    # delete all spaces to check special chars only
    # (check prefix or suffix later)
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
    user = User(username=name, email=email, password=password,
                address=None, postcode=None, balance=100.0)
    # add it to the current database session
    db.session.add(user)
    # actually save the user object
    db.session.commit()

    return True


# login-related


def login(email, password):
    """
    Check login information
      Parameters:
        email (string):    user email
        password (string): user password
      Returns:
        The user object if login succeeded otherwise None
    """
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


def update_user_profile(email, name, shipping_address, postal):
    """
    R3-1: A user is only able to update his/her user name,
    shipping_address, and postal_code.
    R3-2: Shipping_address should be non-empty, alphanumeric-only,
    and no special characters such as !.
    R3-3: Postal code has to be a valid Canadian postal code.
    R3-4: User name follows the requirements above.
    """
    # x = User.query.get_or_404(email)

    # search the user by email
    x = User.query.filter_by(email=email).first()
    if x:
        # validate username
        if not len(name) <= 0:
            #  alphanumeric-only
            if re.search("^[a-zA-Z0-9]*$", name) is None:
                return False
            # space allowed only if it is not as the prefix or suffix
            if name.find(' ') == 0 or name.find(' ') == (len(name) - 1):
                return False
            # User name has to be longer than 2
            # characters and less than 20 characters
            if len(name) <= 2 or len(name) >= 20:
                return False
            # update

            x.username = name

        # validate shipping address
        if shipping_address == '':
            return False
        if len(shipping_address) > 0:
            address_spaceless = shipping_address.replace(' ', '')
            # shipping address being alphanumeric-only
            if re.fullmatch("^[a-zA-Z0-9]*$", address_spaceless) is None:
                return False
            # no special characters
            regexaddr = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            if not regexaddr.search(address_spaceless) is None:
                return False
            # update

            x.address = shipping_address

        # validate postal code
        if not len(postal) <= 0:
            spaceless = postal.replace(' ', '')
            # allowed numbers
            nums = "0123456789"
            # allowed characters (WZ handled below)
            alph = "ABCEGHJKLMNPRSTVWXYZ"
            # index of number
            mustBeNums = [1, 3, 5]
            # index of character (WZ handled below)
            mustBeAlph = [0, 2, 4]

            illegalCharacters = [x for x in spaceless if x not in
                                 (nums + alph.lower() + alph + " ")]
            if illegalCharacters:
                return False
            # copy to uppercase list
            postalCode = [x.upper() for x in spaceless]
            # length-validation
            if len(postalCode) != 6:
                return False
            # loop over all indexes
            for idx in range(0, len(postalCode) - 1):
                ch = postalCode[idx]
                # is is number, check index
                if ch in nums and idx not in mustBeNums:
                    return False
                # id is character, check index
                elif ch in alph and idx not in mustBeAlph:
                    return False
                # is space in between
                elif ch == " " and idx != 2:
                    return False
            # no W or Z first char
            if postalCode[0] in "WZ":
                return False

            # update
            x.postcode = postal
    else:
        return False
    # commit all changes
    db.session.commit()
    return True


def create_product(title, description, price, date, owner_email):
    # the title should be alphanumeric-only

    if title.isnumeric():
        return False
    if title.isalpha():
        return False
    # space allowed only if it is not as prefix and suffix
    if title.find(' ') == 0 or title.find(' ') == (len(title) - 1):
        return False
    titletrimed = title.replace(' ', '')
    if any(not c.isalnum() for c in titletrimed):
        return False
    # The title of the product is no longer than 80 characters
    if len(title) > 80:
        return False
    # a minimum length of 20 characters and a maximum of 2000 characters
    if len(description) < 20:
        return False
    if len(description) > 2000:
        return False
    # Description has to be longer than the product's title
    if len(description) <= len(title):
        return False
    # Price has to be of range [10, 10000]

    if float(price) < 10:
        return False
    if float(price) > 10000:
        return False

    # last_modified_date must be after 2021-01-02 and before 2025-01-02
    if int(date[0:4]) == 2021:
        if int(date[5:7]) <= 1:
            if int(date[8:]) <= 2:
                return False
    if int(date[0:4]) < 2021:
        return False
    if int(date[0:4]) == 2025:
        if int(date[5:7]) >= 1:
            if int(date[8:]) >= 2:
                return False
    if int(date[0:4]) > 2025:
        return False
    # owner_email cannot be empty
    # if empty input
    if len(owner_email) == 0:
        return False
    # if not valid email format
    if re.fullmatch(regex, owner_email) is None:
        return False
    # A user cannot create products that have the same title
    existed = Product.query.filter_by(title=title).all()
    if len(existed) > 0:
        return False

    # create a new product
    product = Product(title=title, description=description, price=float(price),
                      date=date, owner_email=owner_email)
    # add it to the current database session
    db.session.add(product)
    # actually save the product object
    db.session.commit()

    return True


def update_product(title, new_title, description, price):
    # R5-1: One can update all attributes of the product,
    # except owner_email and last_modified_date.
    # R5-2: Price can be only increased but cannot be decreased :)
    # R5-3: last_modified_date should be updated
    # when the update operation is successful.
    # R5-4: When updating an attribute,
    # one has to make sure that it follows the same requirements as above.
    # search the Product by owner email
    x = Product.query.filter_by(title=title).first()
    if x:
        # validate title
        if not len(new_title) <= 0:
            # The title of the product has to be alphanumeric-only
            if not new_title.isnumeric() and new_title.isalpha():
                print("test1")
                return False
            # space allowed only if it is not as prefix and suffix
            if new_title.find(' ') == 0 or new_title.find(' ')\
                    == (len(new_title) - 1):
                print("test2")
                return False
            if any(not c.isalnum() for c in new_title):
                print("test3")
                return False
            # title exist
            existed = Product.query.filter_by(title=new_title).all()
            if len(existed) > 0:
                return False
            # update
            x.title = new_title

        # validate description
        if len(description) > 0:
            # minimum length of 20 characters and a maximum of 2000 characters
            if not ((len(description) >= 20) and (len(description) <= 2000)):
                return False
            # Description has to be longer than the product's title
            if len(description) <= len(title):
                return False
            # update
            x.description = description

        # validate price
        if price:
            # Price has to be of range [10, 10000]
            if not float(price) >= 10 and float(price) <= 10000:
                return False
            # Price can be only increased but cannot be decreased
            if not float(price) > x.price:
                return False
            # update

            x.price = float(price)

        # update last_modified_date with current date
        last_update_date = datetime.today().strftime('%Y-%m-%d')
        x.date = last_update_date

        # save all changes
        db.session.commit()
    else:
        return False
    return True
