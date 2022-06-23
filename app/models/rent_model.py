from uuid import uuid4

from extensions import db


class Rent(db.Model):
    __tablename__ = "rents"

    id = db.Column(db.String, primary_key=True)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    expected_return_date = db.Column(db.DateTime)
    total = db.Column(db.Float)

    owner_id = db.Column(db.String, db.ForeignKey("owners.id"))
    immobile_id = db.Column(db.String, db.ForeignKey("immobiles.id"))
    tenant_id = db.Column(db.String, db.ForeignKey("tenants.id"))

    def __init__(
        self,
        start_date,
        expected_return_date,
        owner_id,
        immobile_id,
        tenant_id,
    ):
        self.id = str(uuid4())
        self.start_date = start_date
        self.expected_return_date = expected_return_date
        self.owner_id = owner_id
        self.immobile_id = immobile_id
        self.tenant_id = tenant_id

    @classmethod
    def find_by_id(cls, rent_id):
        return db.session.query(cls).filter_by(id=rent_id).first()


    def transform_to_json(self):
        return {
            "id": self.id,
            "start_date": self.start_date.strftime("%Y/%m/%d %H:%M"),
            "end_date": self.end_date.strftime("%Y/%m/%d %H:%M")
            if self.end_date
            else None,
            "expected_return_date": self.expected_return_date.strftime("%Y/%m/%d %H:%M"),
            "total": self.total,
            "owner_id": self.owner_id,
            "immobile_id": self.immobile_id,
            "tenant_id": self.tenant_id,
        }
