from uuid import uuid4

from extensions import db
from .user_model import Document


class Rent_Contract(Document):
    __tablename__ = "rent_contracts"

    id = db.Column(db.String, db.ForeignKey("documents.id"), primary_key=True)
    rent_contract_number = db.Column(db.Integer(), unique=True)
    

    __mapper_args__ = {"polymorphic_identity": "rent_contracts"}

    def __init__(self, description, rent_contract_number):
        super().__init__(
            description,
        )
        self.rent_contract_number = rent_contract_number



    def transform_to_json(self):
        return {
            "id": self.id,
            "description": self.description,
            "rent_contract_number": self.rent_contract_number,
        }
