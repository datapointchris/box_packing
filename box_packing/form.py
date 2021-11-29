from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, DateField, BooleanField
from wtforms.validators import DataRequired, Length


class CheckForm(FlaskForm):
    """Checkbox form."""
    date = DateField(
        'Date',
        [DataRequired()]
    )
    green_tea = BooleanField(
        'Green Tea',
        []
    )
    portion_control = BooleanField(
        'Portion Control',
        []
    )
    submit = SubmitField('Submit')