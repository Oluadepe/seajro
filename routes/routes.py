#!/usr/bin/python3
""" """
from flask import Flask, redirect, url_for, request, session, render_template
from flask import flash
from models.favourite import Favourite
from models.feedback import Feedback
from models.user import User
from models import storage
from flask_wtf.csrf import csrf_protect
import hashlib
import secrets



app = Flask(__name__)
app.url_map.strict_slashes = False
app.secret_key = secrets.token_hex(32)


@app.teardown_appcontext
def close(exception):
    """ closes current SQLAlchemy session. """
    storage.close()


@app.route('/')
def home():
    return 'This os the Home Page!\nWeather data will be generated'


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """ sign up form """
    if request.method == 'GET':
        return render_template('signup.html')
    email = request.form['email']
    first_name = request.form['firstName']
    last_name = request.form['lastName']
    password = request.form['password']
    state = request.form['state']
    country = request.form['country']
    city = request.form['city']
    if email:
        try:
            user = storage.retrieve(User, email).values()
            if user:
                if user is None:
                    raise Exception('Value of user is None')
                else:
                    flash('User already exists.', 'info')
                    return redirect(url_for('signin'))
        except Exception:
            pass
    user = User(email=email, first_name=first_name, last_name=last_name
                password=password, state=state, country=country, city=city)
    storage.new(user)
    storage.save()
    flash('Thank you for Signing up with us!, please proceed to Sign In.')
    return redirect(url_for('signin'))


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    """ User Authentication """
    if session['logged_in'] is not True and request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        password = hashlib.md5(password.encode()).hexdigest()
        user = storage.retrieve(User, email).values()
        if user['password'] == password:
            session['logged_in'] = True
            session['user_email'] = email
            flash('You have been logged in')
            return redirect(url_for('user'))
        else:
            msg = "wrong password or email, perhaps you don't have an account"
            msg = msg + ' with us yet!.'
            flash(msg)
            return redirect(url_for('signin'))
    elif session['logged_in'] is True:
        flash('You are already logged in', 'info')
        return redirect(url_for('user'))
    else:
        render_template('login.html')


@app.route('/user')
@csrf_protect
@login_required
def user():
    return 'User Landing Page/Dashboard'


@app.route('/user/schedule')
@csrf_protect
@login_required
def schedule():
    return "returns schedule page where user can set schedules"


@app.route('/signout', methods=['GET'])
@csrf_protect
@login_required
def signout():
    session.pop('logged_in', None)
    flash('You have been logged out', 'info')
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(port=5000)
