from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, validators, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired


class RatingLabels(FlaskForm):
    rating = FloatField('Rank the movie out of 10', [validators.DataRequired(message='Please insert a number'),
                        validators.NumberRange(min=1, max=10, message='Only numbers 1 to 10')],
                        description="For example 5.5")
    review = StringField("Share a thought about the movie", validators=[InputRequired()],
                         description="I loved X character...")
    submit = SubmitField('Submit')


class MovieLabels(FlaskForm):
    name = StringField('Movie Title', validators=[InputRequired()])
    submit = SubmitField('Search')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')


class SearchForm(FlaskForm):
    searched = StringField('Searched', validators=[InputRequired()])
    submit = SubmitField('<i class="fas fa-search"></i>')
