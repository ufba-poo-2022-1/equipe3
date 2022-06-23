from uuid import uuid4

from extensions import db


class Document(db.Model):
    __tablename__ = "documents"

    id = db.Column(db.String, primary_key=True)
    description = db.Column(db.String(256))
    type = db.Column(db.String(128))  # necessário para a herança


    __mapper_args__ = {"polymorphic_identity": "documents", "polymorphic_on": type}

    def __init__(self, id, type, description):
        self.id = str(uuid4())
        self.description = description
        self.type = type

