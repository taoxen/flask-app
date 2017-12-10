# Import Form and RecaptchaField (optional)
from flask_wtf import FlaskForm # , RecaptchaField

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import StringField, PasswordField, BooleanField

# Import Form validators
from wtforms.validators import InputRequired, Email, EqualTo, Length


# Define the login form (WTForms)
class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), 
		Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(),
	       	Length(min=8, max=80)])
    remember = BooleanField('remember me')


class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(),
	    Email(message='Invalid Email Address'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(),
	       	Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(),
	       	Length(min=8, max=80)])

#
#class LoginForm(Form):
#    email    = TextField('Email Address', [Email(),
#                Required(message='Forgot your email address?')])
#    password = PasswordField('Password', [
#                Required(message='Must provide a password. ;-)')])
#
