from flask import Flask, render_template, url_for, flash, redirect, request
from get_artist import *
import random
import os
from forms import registrationForm, loginForm
from flask_login import LoginManager, login_user, current_user, logout_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the random string'
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return 'skaushik2'

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    #artists = [Justin, Weekend, Taylor]
    random_number = random.randint(0,2)
    return render_template('index.html', artists = artists, random_number = random_number, title = 'Homepage')

@app.route("/login", methods=['GET', 'POST'])
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for('hello_world'))
    form = loginForm()
    if form.validate_on_submit():
        user = form
        if(form.username.data == 'skaushik2' and form.password.data == 'hello123'):
            login_user(user)
            next_page = request.args.get('next')
            flash('Welcome back!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('hello_world'))
        else:
            flash('Incorrect username or password', 'error')
    return render_template('login.html', form = form, title = 'login page')

@app.route("/register", methods=['GET', 'POST'])
def register_page():
    form = registrationForm()

    if form.validate_on_submit():
        flash('Your account is now created and you can log in below', 'success')
        return redirect(url_for('login_page'))
    return render_template('register.html', form = form, title = 'Registration page')

if __name__ == '__main__':
    app.run(debug = True, host="0.0.0.0")