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


    def __init__(self, street, number, district, city, cep, user_id, complement=None):
        self.id = str(uuid4())
        self.street = street
        self.number = number
        self.district = district
        self.city = city
        self.cep = cep
        self.complement = complement
        self.user_id = user_id
