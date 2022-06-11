from extensions import db
from .user_model import User


class Owner(User):
    __tablename__ = "owners"

    id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    deed_id = db.Column(db.Integer)

    __mapper_args__ = {"polymorphic_identity": "owners"}
