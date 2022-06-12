from extensions import db
from .immobile_model import Immobile


class Apartment(Immobile):
    __tablename__ = "apartments"

    id = db.Column(db.String, db.ForeignKey("immobiles.id"), primary_key=True)

    __mapper_args__ = {"polymorphic_identity": "apartments"}

    def __init__(self, description, value, area, is_available):
        super().__init__(description, value, area, is_available)
