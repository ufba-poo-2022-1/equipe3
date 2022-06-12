from uuid import uuid4
from datetime import datetime, timezone

from extensions import db


def get_correct_datetime():
    current_time = datetime.now(timezone.utc)
    return current_time.strftime("%Y-%m-%d %H:%M:%S%z")


class Rent:
    __tablename__ = "rents"

    id = db.Column(db.String, primary_key=True)
    start_date = db.Column(db.DateTime(timezone=True))
    end_date = db.Column(db.DateTime(timezone=True))
    expected_return_date = db.Column(db.DateTime(timezone=True))
    total = db.Column(db.Float)
    fine_amount = db.Column(db.Float)
    created_at = db.Column(db.DateTime(timezone=True), default=get_correct_datetime)

    owner_id = db.Column(db.String, db.ForeignKey("owners.id"))
    tenant_id = db.Column(db.String, db.ForeignKey("tenants.id"))
    immobile_id = db.Column(db.String, db.ForeignKey("immobiles.id"))

    def __init__(
        self,
        start_date,
        end_date,
        expected_return_date,
        total,
        fine_amount,
        created_at,
        owner_id,
        tenant_id,
        immobile_id,
    ):
        self.id = str(uuid4())
        self.start_date = start_date
        self.end_date = end_date
        self.expected_return_date = expected_return_date
        self.total = total
        self.fine_amount = fine_amount
        self.created_at = created_at
        self.owner_id = owner_id
        self.tenant_id = tenant_id
        self.immobile_id = immobile_id
