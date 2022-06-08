from extensions import db


class Address(db.Model):
    __tablename__ = "adresses"

    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(128))
    number = db.Column(db.Integer)
    district = db.Column(db.String(128))
    city = db.Column(db.String(128))
    cep = db.Column(db.String(128))
    complement = db.Column(db.String(128))
