from uuid import uuid4

from extensions import db


class Immobile(db.Model):
    """
    Classe que faz a herança da classe base Model e define a entidade Immobile.

    Parameters
    ----------
    id: string
    description:string
    daily_rate:float
    fine_amount:float
    area:float
    is_available:boolean
    type:string

    Returns
    -------
     response: __type__
        Entidade immobile criada

    """
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
        """
        Método responsável por buscar um imóvel em determinada classe por seu id

        Parameters
        ----------
        immobile_id: string
        cls:__type__

        Returns
        -------
        response: __type__
        Entidade filtrada por seu id

        """
        return db.session.query(cls).filter_by(id=immobile_id).first()

    @classmethod
    def list_all(cls):
        """
        Método responsável por listados todos os imóveis de uma classe

        Parameters
        ----------
        cls:__type__

        Returns
        -------
        response: __type__
        Todas as entidades cadastradas daquela classe

        """
        
        return db.session.query(cls).all()
