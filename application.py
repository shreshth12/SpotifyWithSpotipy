from flask import Flask, render_template, url_for, flash, redirect
from get_artist import *
import random
import os
from forms import registrationForm, loginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the random string' 

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
        flash('Your account is now created and you can log in below', 'success')
        return redirect(url_for('login_page'))
    return render_template('register.html', form = form)

if __name__ == '__main__':
    app.run(debug = True, host="0.0.0.0")