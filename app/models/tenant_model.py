from extensions import db
from .user_model import User


class Tenant(User):
    __tablename__ = "tenants"

    id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    rent_contract_id = db.Column(db.Integer)

    __mapper_args__ = {"polymorphic_identity": "tenants"}
