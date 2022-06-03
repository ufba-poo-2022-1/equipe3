from .user_model import User


class Tenant(User):
    __tablename__ = "tenants"

    pass
