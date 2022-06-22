from uuid import uuid4

from extensions import db


""" Controller responsible for adding user endpoints """


class Immobile(db.Model):
    __tablename__ = "immobiles"

    id = db.Column(db.String, primary_key=True)
    description = db.Column(db.String(128))
    value = db.Column(db.Float)
    area = db.Column(db.Float)
    _is_available = db.Column(db.Boolean, default=True)
    type = db.Column(db.String(128))

    address = db.relationship("Address", backref="immobiles", uselist=False)

    __mapper_args__ = {"polymorphic_identity": "immobiles", "polymorphic_on": type}

    def __init__(self, description, value, area, is_available):
        self.id = str(uuid4())
        self.description = description
        self.value = value
        self.area = area
        self._is_available = is_available

    @property
    def is_available(self):
        return self._is_available

    @is_available.setter
    def is_available(self, is_available):
        self._is_available = is_available
