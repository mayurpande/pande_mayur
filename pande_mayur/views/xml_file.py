from flask import Blueprint, render_template, flash, redirect, request
from pande_mayur.models.models import Contact
from pande_mayur.extensions import db

# created blueprint for handling xml file route
xml_file = Blueprint('xml_input', __name__)