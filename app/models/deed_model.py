from extensions import db
from .document_model import Document


class Deed(Document):
    """
    Classe que faz a herança da classe Document e define a entidade Deed.

    Parameters
    ----------
    id: string
    description:string
    deed_number:Integer
    date_of_acquaitance:datetime


    Returns
    -------
     response: JSON
        JSON com os atributos da entidade criada

    """

    __tablename__ = "deeds"

    id = db.Column(db.String, db.ForeignKey("documents.id"), primary_key=True)
    deed_number = db.Column(db.Integer, unique=True)
    date_of_acquaintance = db.Column(db.DateTime)

    __mapper_args__ = {"polymorphic_identity": "deeds"}

    def __init__(self, description, deed_number, date_of_acquaintance):
        super().__init__(
            description,
        )
        self.deed_number = deed_number
        self.date_of_acquaintance = date_of_acquaintance

    def transform_to_json(self):
        return {
            "id": self.id,
            "description": self.description,
            "deed_number": self.deed_number,
            "date_of_acquaintance": self.date_of_acquaintance.strftime("%Y/%m/%d %H:%M"),
        }
