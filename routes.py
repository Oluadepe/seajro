#!/usr/bin/python3
""" Manages application routes. """
from flask import Flask, redirect, url_for, request, session, render_template
from weather.climate import current
from flask import flash, jsonify
from datetime import datetime
from models.favourite import Favourite
from models.feedback import Feedback
from models.user import User, Event
from models import storage
#from flask_wtf.csrf import csrf_protect
import hashlib
import secrets


app = Flask(__name__)
app.url_map.strict_slashes = False
app.secret_key = secrets.token_hex(32)


@app.teardown_appcontext
def close(exception):
    """ closes current SQLAlchemy session. """
    storage.close()


@app.route('/', methods=['GET', 'POST'])
def home():
    if 'logged_in' not in session and request.method == 'GET':
        return render_template('index.html')
    elif 'logged_in' in session and request.method == 'GET':
        email = session['email']
        user = list(storage.retrieve(User, email).values())[0]
        events = []
        for ev in user.events:
            dic = {}
            dic['title'] = ev.title
            dic['date'] = ev.date
            events.append(dic)
        return render_template('index.html')
    else:
        lon = request.json['lon']
        lat = request.json['lat']
        details = current(lon=lon, lat=lat)
        return jsonify(details)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """ sign up form """
    if request.method == 'GET':
        return render_template('register.html')
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    password = request.form['password']
    state = request.form['state']
    country = request.form['country']
    city = request.form['city']
    if email:
        try:
            user = storage.retrieve(User, email).values()
            if len(user) == 1:
                if list(user)[0] is None:
                    raise Exception('Value of user is None')
                else:
                    flash('User already exists.', 'info')
                    return redirect(url_for('signin'))
        except Exception:
            pass
    user = User(email=email, first_name=first_name, last_name=last_name,
                password=password, state=state, country=country, city=city)
    storage.new(user)
    storage.save()
    flash('Thank you for Signing up with us!, please proceed to Sign In.')
    return redirect(url_for('signin'))


@app.route('/login', methods=['GET', 'POST'])
def signin():
    """ User Authentication """
    if 'logged_in' not in session and request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        password = hashlib.md5(password.encode()).hexdigest()
        user = storage.retrieve(User, email).values()
        user = list(user)
        if user[0].password == password:
            session['logged_in'] = True
            session['email'] = email
            flash('You have been logged in')
            return redirect(url_for('user'))
        else:
            msg = "wrong password or email, perhaps you don't have an account"
            msg = msg + ' with us yet!.'
            flash(msg)
            return redirect(url_for('signin'))
    elif 'logged_in' in session:
        flash('You are already logged in', 'info')
        return redirect(url_for('user'))
    else:
        return render_template('login.html')


@app.route('/user')
#@csrf_protect
#@login_required
def user():
    return 'User Landing Page/Dashboard'


@app.route('/user/schedule', methods=['POST'])
#@csrf_protect
def schedule():
    user_event = request.json
    date = user_event['date']
    date = datetime.strptime(date, '%Y-%m-%d').date()
    title = user_event['title']
    country = user_event['country']
    city = user_event['city']
    state = user_event['state']
    user = storage.retrieve(User, session['email']).values()
    user = list(user)[0]
    event = Event(title=title, date=date, country=country, city=city,
                  state=state, User=user)
    storage.new(event)
    storage.save()
    flash('Successfully added an event!')
    return redirect(url_for('home'))


@app.route('/signout', methods=['GET'])
#@csrf_protect

def signout():
    session.pop('logged_in', None)
    flash('You have been logged out', 'info')
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(port=5000)
