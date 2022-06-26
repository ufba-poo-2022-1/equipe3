from uuid import uuid4

from extensions import db


class Document(db.Model):
    """
    Classe que faz a herança da classe base Model e define a entidade Document.

    Parameters
    ----------
    id: string
    description:string
    type:string

    Returns
    -------
     response: __type__
        Entidade document criada

    """

    __tablename__ = "documents"

    id = db.Column(db.String, primary_key=True)
    description = db.Column(db.String(256))
    type = db.Column(db.String(128))  # necessário para a herança

    __mapper_args__ = {"polymorphic_identity": "documents", "polymorphic_on": type}

    def __init__(self, description):
        self.id = str(uuid4())
        self.description = description
