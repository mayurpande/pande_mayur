from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, Form, FormField
from wtforms.validators import InputRequired, Length, Email, NumberRange


class TelephoneForm(Form):

    """class to hold form fields for country code and number"""

    country_code = IntegerField('Country Code', validators=[InputRequired(), NumberRange(
        min=2, max=2, message='Must be 2 digits long')])
    number = IntegerField('Number', validators=[InputRequired(), NumberRange(
        min=9, max=9, message="Must be 9 digits long")])


class ContactForm(FlaskForm):

    """Flask-WTF form to create form fields to use in template"""

    # created form fields using respective validators
    first_name = StringField('First name', validators=[InputRequired(), Length(max=50)])
    last_name = StringField('Last name', validators=[InputRequired(), Length(max=50)])
    address = StringField('Address', validators=[Length(max=300)])
    email = StringField('Email', validators=[Email(), Length(max=300)])
    # Created field enclosure object to handle child objects
    phone = FormField(TelephoneForm)

