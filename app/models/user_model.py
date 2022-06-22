from uuid import uuid4

from extensions import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(128))
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    phone = db.Column(db.String(120))
    type = db.Column(db.String(128))  # necessário para a herança

    address = db.relationship("Address", backref="users", uselist=False)

    __mapper_args__ = {"polymorphic_identity": "users", "polymorphic_on": type}

    def __init__(self, name, email, password, phone):
        self.id = str(uuid4())
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
