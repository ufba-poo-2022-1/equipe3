from extensions import db
from .immobile_model import Immobile


class House(Immobile):
    __tablename__ = "houses"

    id = db.Column(db.String, db.ForeignKey("immobiles.id"), primary_key=True)

    __mapper_args__ = {"polymorphic_identity": "houses"}

    def __init__(self, description, value, area, is_available):
        super().__init__(description, value, area, is_available)
