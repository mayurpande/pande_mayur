from flask import Blueprint, render_template, flash, redirect, request
from pande_mayur.models.models import Contact
from pande_mayur.extensions import db
from pathlib import Path
from xml.etree import ElementTree
from validate_email import validate_email
import os
import re

# created blueprint for handling xml file route
xml_blueprint = Blueprint('xml_input', __name__)


# defined route, passed get variable to handle filename
@xml_blueprint.route('/xml/<xml>', methods=['GET', 'POST'])
def xml_file(xml):
    # set path string have to put file in data folder
    file_path = str(Path(__file__).resolve().parent.parent / "data" / xml)

    # first check if file path exists
    if os.path.exists(file_path):

        # parse xml using ElementTree object
        dom = ElementTree.parse(file_path)
        # find all contact in the dom
        contacts_xml = dom.findall('contact')
        data_contacts = []
        errors = {
            'content_missing': [],
            'email': [],
            'country_code': [],
            'phone': []
        }

        # loop through contacts
        for s, item in enumerate(contacts_xml):

            # get the text for each and validate

            def check_content_present(col):
                """function to check to see if element is in the xml tree and return the text"""
                try:
                    col_content = item.find(col).text
                    return col_content
                except Exception:
                    return ''

            # call check_content_present for various elements in xml
            first_name = check_content_present('firstname')
            last_name = check_content_present('lastname')
            email = check_content_present('email')

            # run check for mandatory columns - append errors
            if not first_name or not last_name or not email:
                errors['content_missing'].append(
                    "<h1>You are missing data for either column(s): firstname, lastname, email for entry no: " + \
                    str(s) + "</h1>")
                continue

            # validate email address
            is_valid_email = validate_email(email)
            if not is_valid_email:
                errors['email'].append('<h1>Email is not of valid type for entry no: ' + str(s) + '</h1>')
                continue

            address = check_content_present('address')
            phone = check_content_present('phone')

            # check if phone present as not a mandatory field
            if phone:

                # remove brackets with digit to check instance is int
                phone = re.sub(r'\(\w+\)', '', phone)
                split_phone = phone.split()
                try:
                    True if isinstance(int("".join(split_phone)), int) else False
                    country_code = phone.split()[0]
                    # check if phone number start with + and country code is correct number of digits

                    if country_code.startswith("+") and len(country_code) <= 4:
                        # insert joined phone number
                        phone = "".join(split_phone)
                    elif len(country_code) <= 3:
                        split_phone.insert(0, "+")
                        phone = "".join(split_phone)

                    else:
                        # append errors if not 2 or 3 digits
                        errors['country_code'].append("<h1>Country code needs to be either 2 or 3 digits long, "
                                                      "for entry no: " + str(s) + "</h1>")
                        continue
                except ValueError:
                    errors['phone'].append("<h1>Phone number is not numeric digits, for entry no: " + str(s) + "</h1>")
                    continue
            # create object to and append to list for bulk insert
            print(phone)
            contact = Contact(
                firstname=first_name,
                lastname=last_name,
                address=address,
                email=email,
                phone=phone
            )
            data_contacts.append(contact)

            if len(errors) > 0:
                context = {
                    'errors': errors
                }
                for key, value in errors.items():
                    for error in value:
                        print(error)

        db.session.add_all(data_contacts)
        db.session.commit()

    return render_template('xml_content.html', **context)
