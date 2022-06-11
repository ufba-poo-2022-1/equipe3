from uuid import uuid4

from extensions import db


""" Controller responsible for adding user endpoints """


class Immobile(db.Model):
    __tablename__ = "immobiles"

    id = db.Column(db.String, primary_key=True)
    description = db.Column(db.String(128))
    value = db.Column(db.Float)
    area = db.Column(db.Float)
    type = db.Column(db.String(128))

    address = db.relationship("Address", backref="immobiles")

    __mapper_args__ = {"polymorphic_identity": "immobiles", "polymorphic_on": type}

    def __init__(self, description, value, area, is_available):
        self.id = str(uuid4())
        self.description = description
        self.address = address
        self.value = value
        self.area = area
        self.is_available = is_available

    def get_dados(self):
        return [
            self.__id,
            self.__type,
            self.__description,
            self.__address,
            self.__value,
            self.__area,
            self.__is_available,
        ]
