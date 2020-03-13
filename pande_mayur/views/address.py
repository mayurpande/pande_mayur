from flask import Blueprint

# created blueprint for main address routes
address = Blueprint('address', __name__)


@address.route('/', methods=['GET', 'POST'])
def index():

    """main index route for address book which will loads the form"""

    # TODO generate form and pass to template
    return '<h1>hello world</h1>'