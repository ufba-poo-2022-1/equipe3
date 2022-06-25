from uuid import uuid4

from extensions import db


class User(db.Model):
    """
    Classe que faz a herança da classe base Model e define a entidade Usuário.

    Parameters
    ----------
    id: string
    name:string
    email:string
    password:string
    phone:string
    type:string

    Returns
    -------
     response: __type__
        Entidade Usuário criada

    """
    __tablename__ = "users"

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(128))
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    phone = db.Column(db.String(120))
    type = db.Column(db.String(128))  # necessário para a herança

    __mapper_args__ = {"polymorphic_identity": "users", "polymorphic_on": type}

    def __init__(self, name, email, password, phone):
        self.id = str(uuid4())
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone

    @classmethod
    def list_all(cls):
        """
        Método responsável por listados todos os usuários de uma classe

        Parameters
        ----------
        cls:__type__

        Returns
        -------
        response: __type__
        Todas as entidades cadastradas daquela classe

        """
        return db.session.query(cls).all()

    @classmethod
    def find_by_email(cls, user_email):
        """
        Método responsável por buscar um usuário em determinada classe por seu email

        Parameters
        ----------
        user_email: string
        cls:__type__

        Returns
        -------
        response: __type__
        Entidade filtrada por seu id

        """
        return db.session.query(cls).filter_by(email=user_email).first()

    @classmethod
    def find_by_id(cls, user_id):
        """
        Método responsável por buscar um usuário em determinada classe por seu id

        Parameters
        ----------
        user_id: string
        cls:__type__

        Returns
        -------
        response: __type__
        Entidade filtrada por seu id

        """
        return db.session.query(cls).filter_by(id=user_id).first()
