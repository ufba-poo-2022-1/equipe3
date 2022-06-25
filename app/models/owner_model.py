from extensions import db
from .user_model import User


class Owner(User):
    """
    Classe que faz a herança da classe User e define a entidade Owner.

    Parameters
    ----------
    id: string
    name:string
    email:string
    phone:string
    deed_id:string

    Returns
    -------
     response: JSON
        JSON com os dados da Entidade Owner criada

    """

    __tablename__ = "owners"

    id = db.Column(db.String, db.ForeignKey("users.id"), primary_key=True)
    deed_id = db.Column(db.String, db.ForeignKey("deeds.id"))

    __mapper_args__ = {"polymorphic_identity": "owners"}

    def __init__(self, name, email, password, phone, deed_id):
        super().__init__(
            name,
            email,
            password,
            phone,
        )
        self.deed_id = deed_id

    @classmethod
    def list_all(cls):
        """
        Método responsável por listar todos os owners

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
            "deed_id": self.deed_id if self.deed_id else None,
        }
