from pande_mayur.extensions import db


class Contact(db.Model):

    """Contact table class inherits from flask-sqlalchemy db.Model class"""

    contact_id = db.Column(db.Integer, primary_key=True, nullable=False)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(300))
    email = db.Column(db.String(300), nullable=False)
    phone = db.Column(db.Integer)
