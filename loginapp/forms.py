from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
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
