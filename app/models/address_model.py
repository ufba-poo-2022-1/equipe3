from uuid import uuid4

from extensions import db


class Address(db.Model):
    """
    Classe que faz a herança da classe base Model e define a entidade Address.

    Parameters
    ----------
    id: string
    street:string
    number:integer
    district:string
    city:string
    cep:string
    complement:string
    owner_id:string
    complement:string

    Returns
    -------
     response: JSON
        JSON com os atributos da entidade criada

    """

    __tablename__ = "addresses"

    id = db.Column(db.String, primary_key=True)
    street = db.Column(db.String(128))
    number = db.Column(db.Integer)
    district = db.Column(db.String(128))
    city = db.Column(db.String(128))
    cep = db.Column(db.String(128))
    complement = db.Column(db.String(128))

    owner_id = db.Column(db.String, db.ForeignKey("owners.id"))
    immobile_id = db.Column(db.String, db.ForeignKey("immobiles.id"))

    def __init__(
        self, street, number, district, city, cep, owner_id, immobile_id, complement=None
    ):
        self.id = str(uuid4())
        self.street = street
        self.number = number
        self.district = district
        self.city = city
        self.cep = cep
        self.complement = complement
        self.owner_id = owner_id
        self.immobile_id = immobile_id

    def transform_to_json(self):
        return {
            "id": self.id,
            "street": self.street,
            "number": self.number,
            "district": self.district,
            "city": self.city,
            "cep": self.cep,
            "complement": self.complement,
            "owner_id": self.owner_id,
            "immobile_id": self.immobile_id,
        }
