from flask import render_template, request, session, redirect
from qbay.models import login, User, register, Product,\
    update_product, update_user_profile, create_product


from qbay import app


def authenticate(inner_function):
    """
    :param inner_function: any python function that accepts a user object
    Wrap any python function and check the current session to see if 
    the user has logged in. If login, it will call the inner_function
    with the logged in user object.
    To wrap a function, we can put a decoration on that function.
    Example:
    @authenticate
    def home_page(user):
        pass
    """

    def wrapped_inner():

        # check did we store the key in the session
        if 'logged_in' in session:
            email = session['logged_in']
            try:
                user = User.query.filter_by(email=email).one_or_none()
                if user:
                    # if the user exists, call the inner_function
                    # with user as parameter
                    return inner_function(user)
            except Exception:
                pass
        else:
            # else, redirect to the login page
            return redirect('/login')

    # return the wrapped version of the inner_function:
    return wrapped_inner


@app.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html', message='Please login')


@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    user = login(email, password)
    if user:
        session['logged_in'] = user.email
        """
        Session is an object that contains sharing information 
        between a user's browser and the end server. 
        Typically it is packed and stored in the browser cookies. 
        They will be past along between every request the browser made 
        to this services. Here we store the user object into the 
        session, so we can tell if the client has already login 
        in the following sessions.
        """
        # success! go back to the home page
        # code 303 is to force a 'GET' request
        return redirect('/', code=303)
    else:
        return render_template('login.html', message='login failed')


@app.route('/')
@authenticate
def home(user):
    # authentication is done in the wrapper function
    # see above.
    # by using @authenticate, we don't need to re-write
    # the login checking code all the time for other
    # front-end portals

    # some fake product data
    ownerEmail = user.email
    products = Product.query.filter_by(owner_email=ownerEmail).all()
    return render_template('index.html', user=user, products=products)


@app.route('/register', methods=['GET'])
def register_get():
    # templates are stored in the templates folder
    return render_template('register.html', message='')


@app.route('/register', methods=['POST'])
def register_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    error_message = None

    if password != password2:
        error_message = "The passwords do not match"
    else:
        # use backend api to register the user
        success = register(name, email, password)
        if not success:
            error_message = "Registration failed."
    # if there is any error messages when registering new user
    # at the backend, go back to the register page.
    if error_message:
        return render_template('register.html', message=error_message)
    else:
        return redirect('/login')


@app.route('/update_user_profile', methods=['GET'])
def update_user_profile_get():
    # templates are stored in the templates folder
    return render_template('update_user_profile.html', message='')


@app.route('/update_user_profile', methods=['POST'])
def update_user_profile_post():
    email = request.form.get('email')
    name = request.form.get('name')
    address = request.form.get('address')
    postal = request.form.get('postcode')

    error_message = None

    # use backend api to register the user
    success = update_user_profile(email, name, address, postal)
    if not success:
        error_message = "Update failed."
    # if there is any error messages when registering new user
    # at the backend, go back to the register page.
    if error_message:
        return render_template('update_user_profile.html',
                               message=error_message)
    else:
        return redirect('/')


@app.route('/create_product', methods=['GET'])
def create_product_get():
    # templates are stored in the templates folder
    return render_template('create_product.html', message='')


@app.route('/create_product', methods=['POST'])
def create_product_post():
    title = request.form.get('title')
    description = request.form.get('description')
    price = request.form.get('price')
    date = request.form.get('date')
    owner_email = request.form.get('owner_email')
    error_message = None

    success = create_product(title, description, price, date, owner_email)
    if not success:
        error_message = 'Creation Failed'
    # if there is any error messages when registering new user
    # at the backend, go back to the register page.
    if error_message:
        return render_template('create_product.html', message=error_message)
    else:
        return redirect('/')


@app.route('/update_product', methods=['GET'])
def update_product_get():
    # templates are stored in the templates folder
    return render_template('update_product.html', message='')


@app.route('/update_product', methods=['POST'])
def update_product_post():
    # def update_product(title, new_title, description, price):
    title = request.form.get('title')
    new_title = request.form.get('new_title')
    description = request.form.get('description')
    price = request.form.get('price')
    error_message = None

    success = update_product(title, new_title, description, price)
    if not success:
        error_message = "Product update failed."
    # if there is any error messages when registering new user
    # at the backend, go back to the register page.
    if error_message:
        return render_template('update_product.html', message=error_message)
    else:
        return redirect('/')


@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in', None)
    return redirect('/')
