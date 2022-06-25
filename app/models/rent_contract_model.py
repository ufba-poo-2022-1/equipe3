from extensions import db
from .document_model import Document


class RentContract(Document):
    """
    Classe que faz a herança da classe Document e define a entidade rent_contract.

    Parameters
    ----------
    id: string
    description:string
    rent_contract_number:Integer


    Returns
    -------
     response: JSON
        JSON com os atributos da entidade criada

    """

    __tablename__ = "rent_contracts"

    id = db.Column(db.String, db.ForeignKey("documents.id"), primary_key=True)
    rent_contract_number = db.Column(db.Integer, unique=True)

    __mapper_args__ = {"polymorphic_identity": "rent_contracts"}

    def __init__(self, description, rent_contract_number):
        super().__init__(
            description,
        )
        self.rent_contract_number = rent_contract_number

    def transform_to_json(self):
        return {
            "id": self.id,
            "description": self.description,
            "rent_contract_number": self.rent_contract_number,
        }
