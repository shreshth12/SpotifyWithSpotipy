from flask import Flask, render_template, url_for, flash, redirect
from get_artist import *
import random
import os
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

#skaushik2test
app = Flask(__name__)
app.config['SECRET_KEY'] = 'the random string' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

from sqlalchemy.orm import backref

class registrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min = 2, max = 20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min = 6, max = 12)])
    repeat_password = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username is already taken')
        

class loginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min = 2, max = 20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.password}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_uri = db.Column(db.String(500), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
        return f"Artist_ID('{self.artist_uri}')"

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    #artists = [Justin, Weekend, Taylor]
    random_number = random.randint(0,2)
    return render_template('index.html', artists = artists, random_number = random_number)

@app.route("/login", methods=['GET', 'POST'])
def login_page():
    form = loginForm()
    if form.validate_on_submit():
        if(form.username.data == 'skaushik2' and form.password.data == 'hello123'):
            flash('Welcome back!', 'success')
            return redirect(url_for('hello_world'))
        else:
            flash('Incorrect username or password', 'error')
    return render_template('login.html', form = form)

@app.route("/register", methods=['GET', 'POST'])
def register_page():
    form = registrationForm()
    if form.validate_on_submit():
        user = User(username = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit() 
        flash('Your account is now created and you can log in below', 'success')
        return redirect(url_for('login_page'))
    return render_template('register.html', form = form)

if __name__ == '__main__':
    app.run(debug = True, host="0.0.0.0")