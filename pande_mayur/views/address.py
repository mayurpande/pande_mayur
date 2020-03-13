from flask import Blueprint, render_template
from pande_mayur.forms import ContactForm
from pande_mayur.models.models import Contact
from pande_mayur.extensions import db

# created blueprint for main address routes
address = Blueprint('address', __name__)


@address.route('/', methods=['GET', 'POST'])
def index():

    """main index route for address book which will loads the form and handles post requests to save to db"""

    # instantiated ContactForm class
    contact = ContactForm()

    if contact.validate_on_submit():

        # create a Contact model object to insert to db
        contact_data = Contact(
            firstname=contact.first_name.data,
            lastname=contact.last_name.data,
            address=contact.address.data,
            email=contact.email.data,
            phone=contact.phone['country_code'].data + contact.phone['number'].data
        )

        # add the new object to the session and then commit it
        db.session.add(contact_data)
        db.session.commit()




    return render_template('index.html', form=contact)
