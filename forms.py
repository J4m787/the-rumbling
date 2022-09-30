from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Length, Email


# class items in login form
class LoginForm(FlaskForm):
    email = StringField('Username',
                        validators=[DataRequired(), Length(max=256)],
                        render_kw={"placeholder": "Email"})
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(max=36)],
                             render_kw={"placeholder": "Password"})
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

# classes items in registration form
class RegistrationForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email(), Length(max=256)],
                        render_kw={"placeholder": "Email"})
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(max=36)],
                             render_kw={"placeholder": "Password"})
    # makes sure 2nd password is same as 1st password
    password2 = PasswordField('Repeat Password',
                              validators=[DataRequired(), EqualTo('password'),
                              Length(max=36)],
                              render_kw={"placeholder": "Confirm Password"})
    submit = SubmitField('Register')