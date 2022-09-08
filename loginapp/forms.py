from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import InputRequired, Length

class RegisterForm(FlaskForm):
    """form to register a user"""

    username = StringField("Username", 
    validators=[InputRequired(), 
    Length(min=1, max=20, message="Username cannot be longer than 20 characters")])
    
    password = PasswordField("Password", 
    validators=[InputRequired()])
    
    email = StringField("Email", 
    validators=[InputRequired()])
    
    first_name = StringField("First Name",
    validators=[InputRequired(), 
    Length(min=1, max=30, message="first name cannot be longer than 30 characters")])
    
    last_name = StringField("Last Name", 
    validators=[InputRequired(), 
    Length(min=1, max=30, message="last name cannot be longer than 30 characters")])

class LoginForm(FlaskForm):
    """form to login a user"""
    username = StringField("Username")
    
    password = PasswordField("Password")

class FeedbackForm(FlaskForm):
    """form to submit feedback"""
    title = StringField("Title",
    validators=[InputRequired(),
    Length(min=1, max=100, message="Title can be no longer than 100 characters")])
    
    content = TextAreaField("Content", validators=[InputRequired()])