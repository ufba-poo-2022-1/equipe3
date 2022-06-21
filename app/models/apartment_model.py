from extensions import db
from .immobile_model import Immobile


class Apartment(Immobile):
    __tablename__ = "apartments"

    id = db.Column(db.String, db.ForeignKey("immobiles.id"), primary_key=True)
    floor = db.Column(db.Integer)

    __mapper_args__ = {"polymorphic_identity": "apartments"}

    def __init__(self, description, value, area, is_available, floor):
        super().__init__(description, value, area, is_available)
        self.floor = floor

    def transform_to_json(self):
        return {
            "id": self.id,
            "description": self.description,
            "value": self.value,
            "area": self.area,
            "is_available": self.is_available,
            "backyard": self.backyard,
            "floor": self.floor,
        }
