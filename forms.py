from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError
from models import User, Post

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

class uriForm(FlaskForm):
    uri = StringField('Enter artist URI', validators=[DataRequired()])
    submit = SubmitField('Save')

    def validate_uri(self, uri):
        post = Post.query.filter_by(artist_uri=uri.data).first()
        if post:
            raise ValidationError('You have already added this artist')
