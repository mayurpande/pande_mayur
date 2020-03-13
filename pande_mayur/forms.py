from flask_wtf import FlaskForm
from wtforms import StringField, Form, FormField
from wtforms.validators import InputRequired, Length, Email, ValidationError


class TelephoneForm(Form):
    """class to hold form fields for country code and number"""

    country_code = StringField('Country Code')
    number = StringField('Number')

    def validate_country_code(self, field):

        """Method to create a custom validation rule to check for length and input type cast"""

        if len(field.data) > 0:
            try:
                # checks if instance type is of field data is int (once type casted to int)
                True if isinstance(int(field.data), int) else False
            except ValueError:
                raise ValidationError('Not a numeric number (it needs to be 2 or 3 digits).')

            if len(field.data) != 2 and len(field.data) != 3:
                # raise wtf custom validation error, with custom message
                raise ValidationError('You have not entered 2 or 3 digits.')

    def validate_number(self, field):

        """Method to create a custom validation rule to check for length and input type cast"""

        if len(field.data) > 0:
            try:
                True if isinstance(int(field.data), int) else False
            except ValueError:
                raise ValidationError('Not a numeric number (it needs to be 2 or 3 digits).')

            if len(field.data) < 9 or len(field.data) > 11:
                raise ValidationError('You have not entered between 9-11 digits.')


class ContactForm(FlaskForm):
    """Flask-WTF form to create form fields to use in template"""

    # created form fields using respective validators
    first_name = StringField('First name', validators=[InputRequired(), Length(max=50)])
    last_name = StringField('Last name', validators=[InputRequired(), Length(max=50)])
    address = StringField('Address', validators=[Length(max=300)])
    email = StringField('Email', validators=[Email(), Length(max=300)])
    # Created field enclosure object to handle child objects
    phone = FormField(TelephoneForm)
