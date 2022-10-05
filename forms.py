from email.policy import default
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, URLField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, DataRequired


class AddPetForm(FlaskForm):
    """Form for adding new pets"""

    name = StringField("Pet Name", validators=[
                       InputRequired(message="Must Add Pet Name")])
    species = SelectField("Pet Species", choices=["Cat", "Dog", "Rabbit", "Fish"], validators=[
                          InputRequired(message="Must Choose Pet Species")])
    breed = StringField("Pet Breed", validators=[
                        InputRequired(message="Must Add Pet Breed")])
    age = IntegerField("Pet Age", validators=[
                       InputRequired(message="Must Add Pet Age"), NumberRange(min=0, max=30, message="Age Must Be Between 0 And 30 (Inclusive)")])
    photo_url = URLField("Upload Pet Photo", validators=[Optional(), URL()])
    notes = StringField("Notes", validators=[Optional()])


class EditPetForm(FlaskForm):
    """Form for editing new pets"""
    name = StringField("Pet Name", validators=[
                       DataRequired(message="You can't change the pet name")], render_kw={"disabled": "disabled"})
    species = SelectField("Pet Species", choices=["Cat", "Dog", "Rabbit", "Fish"], validators=[
                          DataRequired(message="You can't change the pet species")], render_kw={"disabled": "disabled"})
    breed = StringField("Pet Breed", validators=[
                        DataRequired(message="You can't change the pet breed")], render_kw={"disabled": "disabled"})
    age = IntegerField("Pet Age", validators=[
                       DataRequired(message="You can't change the pet age"), NumberRange(min=0, max=30, message="Age Must Be Between 0 And 30 (Inclusive)")], render_kw={"disabled": "disabled"})
    photo_url = URLField("Upload Pet Photo", validators=[Optional(), URL()])
    notes = StringField("Notes", validators=[Optional()])
    availability = BooleanField(
        "Availability", validators=[Optional()])
