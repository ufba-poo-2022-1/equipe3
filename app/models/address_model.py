from uuid import uuid4

from extensions import db


class Address(db.Model):
    __tablename__ = "addresses"

    id = db.Column(db.String, primary_key=True)
    street = db.Column(db.String(128))
    number = db.Column(db.Integer)
    district = db.Column(db.String(128))
    city = db.Column(db.String(128))
    cep = db.Column(db.String(128))
    complement = db.Column(db.String(128))

    user_id = db.Column(db.String, db.ForeignKey("users.id"))
    immobile_id = db.Column(db.String, db.ForeignKey("immobiles.id"))

    def __init__(self, street, number, district, city, cep, user_id, complement=None):
        self.id = str(uuid4())
        self.street = street
        self.number = number
        self.district = district
        self.city = city
        self.cep = cep
        self.complement = complement
        self.user_id = user_id
