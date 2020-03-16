from flask import Blueprint, render_template, flash, redirect, request
from pande_mayur.models.models import Contact
from pande_mayur.extensions import db
from pathlib import Path
import os

# created blueprint for handling xml file route
xml_blueprint = Blueprint('xml_input', __name__)


# defined route, passed get variable to handle filename
@xml_blueprint.route('/xml/<xml>', methods=['GET','POST'])
def xml_file(xml):

    # set path string (subject to change depending on which directory the end user wants to put the xml file
    path = str(Path(__file__).resolve().parent.parent)

    if os.path.exists(path + '/' + xml):
        print(path + '/' + xml)

    return 'hello'
