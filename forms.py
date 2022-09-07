from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding pets to adoption agency"""
    name = StringField("Name", validators=[InputRequired()])
    species = SelectField("Species",
     choices=[("cat", "cat"), ("dog", "dog"), ("porcupine", "porcupine")], 
     validators=[InputRequired()])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes")