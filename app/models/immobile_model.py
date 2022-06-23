from uuid import uuid4

from extensions import db


""" Controller responsible for adding user endpoints """


class Immobile(db.Model):
    __tablename__ = "immobiles"

    id = db.Column(db.String, primary_key=True)
    description = db.Column(db.String(128))
    daily_rate = db.Column(db.Float)
    fine_amount = db.Column(db.Float)
    area = db.Column(db.Float)
    is_available = db.Column(db.Boolean, default=True)
    type = db.Column(db.String(128))

    address = db.relationship("Address", backref="immobiles", uselist=False)

    __mapper_args__ = {"polymorphic_identity": "immobiles", "polymorphic_on": type}

    def __init__(self, description, daily_rate, fine_amount, area, is_available):
        self.id = str(uuid4())
        self.description = description
        self.daily_rate = daily_rate
        self.fine_amount = fine_amount
        self.area = area
        self.is_available = is_available

    @classmethod
    def find_by_id(cls, immobile_id):
        return db.session.query(cls).filter_by(id=immobile_id).first()

    @classmethod
    def list_all(cls):
        return db.session.query(cls).all()
