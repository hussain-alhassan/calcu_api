from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class CalculationForm(FlaskForm):
    first_number = StringField('first_number')
    second_number = StringField('second_number')

    submit = SubmitField("Calculate")
