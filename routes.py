from flask import render_template, url_for, flash, redirect, request
from vars import app, db
from forms import registrationForm, loginForm, uriForm
from flask_login import login_user, current_user, logout_user, login_required
from models import Post, User
from functions import *
import random

@app.route("/", methods=['GET', 'POST'])
@login_required
def homePage():
    form = uriForm()
    if form.validate_on_submit():
        if(check_artist_url(form.uri.data) == True):
            post = Post(artist_uri = form.uri.data, author = current_user)
            db.session.add(post)
            db.session.commit()
            flash('Successfully added artist', 'success')
            return redirect(url_for('homePage'))
        else:
            flash('Please enter a valid artistID', 'error')

    artists_db_ones = Post.query.filter_by(author=current_user).all()
    length_of_db_values = len(artists_db_ones)
    artists = []

    if len(artists_db_ones) != 0:
        for data in artists_db_ones:
            uri = data.artist_uri
            name_of_that_artist = get_artist_name(uri)
            songs_by_that_artist = get_artist_data(uri)
            image_of_that_artist = get_artist_picture(name_of_that_artist)
            data_of_that_artist = [songs_by_that_artist, image_of_that_artist, name_of_that_artist]
            artists.append(data_of_that_artist)

    if len(artists_db_ones) != 0:
        random_number = random.randint(0,len(artists_db_ones)-1)
    else:
        random_number = 0
    return render_template('index.html',length_of_db_values = length_of_db_values,artists_db_ones = artists_db_ones, artists = artists, random_number = random_number, title = 'Homepage', form = form)

@app.route("/login", methods=['GET', 'POST'])
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for('homePage'))
    form = loginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if(user and user.password == form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(url_for('homePage'))
        else:
            flash('Incorrect username or password', 'error')
    return render_template('login.html', form = form, title = 'login page')

@app.route("/register", methods=['GET', 'POST'])
def register_page():
    if current_user.is_authenticated:
        return redirect(url_for('homePage'))
    form = registrationForm()
    if form.validate_on_submit():
        user = User(username = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit() 
        flash('Your account is now created and you can log in below', 'success')
        return redirect(url_for('login_page'))
    return render_template('register.html', form = form, title = 'Registration page')

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login_page'))

