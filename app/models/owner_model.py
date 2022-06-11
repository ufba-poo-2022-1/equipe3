from extensions import db
from .user_model import User


class Owner(User):
    __tablename__ = "owners"

    id = db.Column(db.String, db.ForeignKey("users.id"), primary_key=True)

    # TODO: criar relacionamento com a classe de de escritura, que irá extender
    # de documentos
    deed_id = db.Column(db.Integer)

    __mapper_args__ = {"polymorphic_identity": "owners"}

    def __init__(self, name, email, password, phone, deed_id):
        super().__init__(
            name,
            email,
            password,
            phone,
        )
        self.deed_id = deed_id
