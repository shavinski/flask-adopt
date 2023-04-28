"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL

class AddPetForm(FlaskForm):
    """ Form for adding pets """

    name = StringField(
        "Pet name",
        validators=[InputRequired()])

    species = SelectField(
        "Species",
        choices = [('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')],
        validators=[InputRequired()])

    photo_url = StringField("Photo URL",
        validators=[Optional(), URL()])

    age = SelectField(
        "Age",
        choices = [('baby', 'Baby'), ('young', 'Young'), ('adult', 'Adult'), ('senior', 'Senior')],
        validators=[InputRequired()])

    notes = StringField(
        "Notes")

    available = BooleanField(
        "Available",
        default=True)
        

class EditPetForm(FlaskForm):
    """ Form for editing pet """

    name = StringField(
        "Pet name",
        validators=[InputRequired()])

    species = SelectField(
        "Species",
        choices = [('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')],
        validators=[InputRequired()])

    photo_url = StringField("Photo URL",
        validators=[Optional(), URL()])
        #SHOULD WE HAVE OPTIONAL HERE OR JUST LEAVE IT OUT

    age = SelectField(
        "Age",
        choices = [('baby', 'Baby'), ('young', 'Young'), ('adult', 'Adult'), ('senior', 'Senior')],
        validators=[InputRequired()])

    notes = StringField(
        "Notes",
        validators=[Optional()])