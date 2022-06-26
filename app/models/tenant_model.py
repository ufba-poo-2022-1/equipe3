from extensions import db
from .user_model import User


class Tenant(User):
    """
    Classe que faz a herança da classe User e define a entidade Tenant.

    Parameters
    ----------
    id: string
    name:string
    email:string
    phone:string
    rent_contract_id:string

    Returns
    -------
     response: JSON
        JSON com os dados da Entidade Owner criada

    """

    __tablename__ = "tenants"

    id = db.Column(db.String, db.ForeignKey("users.id"), primary_key=True)
    rent_contract_id = db.Column(db.String, db.ForeignKey("rent_contracts.id"))

    __mapper_args__ = {"polymorphic_identity": "tenants"}

    def __init__(self, name, email, password, phone, rent_contract_id):
        super().__init__(
            name,
            email,
            password,
            phone,
        )
        self.rent_contract_id = rent_contract_id

    @classmethod
    def list_all(cls):
        """
        Método responsável por listar todos os tenants

        Parameters
        ----------
        cls:__type__

        Returns
        -------
        response: __type__
        Todas as entidades cadastradas daquela classe

        """
        return db.session.query(cls).all()

    def transform_to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "rent_contract_id": self.rent_contract_id if self.rent_contract_id else None,
        }
