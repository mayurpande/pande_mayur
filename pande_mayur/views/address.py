from flask import Blueprint, render_template
from pande_mayur.forms import ContactForm

# created blueprint for main address routes
address = Blueprint('address', __name__)


@address.route('/', methods=['GET', 'POST'])
def index():

    """main index route for address book which will loads the form"""

    # instantiated ContactForm class
    contact = ContactForm()

    return render_template('index.html', form=contact)
