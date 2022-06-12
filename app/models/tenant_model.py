from uuid import uuid4

from extensions import db
from .user_model import User


class Tenant(User):
    __tablename__ = "tenants"

    id = db.Column(db.String, db.ForeignKey("users.id"), primary_key=True)

    # TODO: criar relacionamento com a classe de de contrato de alguuel, que irá extender
    # de documentos
    rent_contract_id = db.Column(db.Integer)

    __mapper_args__ = {"polymorphic_identity": "tenants"}

    def __init__(self, name, email, password, phone, rent_contract_id):
        super().__init__(
            name,
            email,
            password,
            phone,
        )
        self.rent_contract_id = rent_contract_id
