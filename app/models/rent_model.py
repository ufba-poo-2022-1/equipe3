from uuid import uuid4

from extensions import db


class Rent(db.Model):
    """
    Classe que faz a herança da classe base Model e define a entidade Rent.

    Parameters
    ----------
    id: string
    start_date:datetime
    end_date:datetime
    expected_return_date:datetime
    total:float
    owner_id:string
    immobile_id:string
    tenant_id:string

    Returns
    -------
     response: __type__
        Entidade Rent criada

    """

    __tablename__ = "rents"

    id = db.Column(db.String, primary_key=True)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    expected_return_date = db.Column(db.DateTime)
    total = db.Column(db.Float)

    owner_id = db.Column(db.String, db.ForeignKey("owners.id"))
    immobile_id = db.Column(db.String, db.ForeignKey("immobiles.id"))
    tenant_id = db.Column(db.String, db.ForeignKey("tenants.id"))
    deed_id = db.Column(db.String, db.ForeignKey("deeds.id"))
    rent_contract_id = db.Column(db.String, db.ForeignKey("rent_contracts.id"))

    def __init__(
        self,
        start_date,
        expected_return_date,
        owner_id,
        immobile_id,
        tenant_id,
        deed_id,
        rent_contract_id,
    ):
        self.id = str(uuid4())
        self.start_date = start_date
        self.expected_return_date = expected_return_date
        self.owner_id = owner_id
        self.immobile_id = immobile_id
        self.tenant_id = tenant_id
        self.deed_id = deed_id
        self.rent_contract_id = rent_contract_id

    @classmethod
    def find_by_id(cls, rent_id):
        """
        Método responsável por buscar um aluguel em determinada classe por seu id

        Parameters
        ----------
        rent_id: string
        cls:__type__

        Returns
        -------
        response: __type__
        Entidade filtrada por seu id

        """

        return db.session.query(cls).filter_by(id=rent_id).first()

    @classmethod
    def find_by_tenant_id(cls, tenant_id):
        """
        Método responsável por buscar um aluguel em determinada classe por seu tenant_id

        Parameters
        ----------
        tenant_id: string
        cls:__type__

        Returns
        -------
        response: __type__
        Entidade filtrada por seu id

        """

        return db.session.query(cls).filter_by(tenant_id=tenant_id).all()

    @classmethod
    def find_by_owner_id(cls, owner_id):
        """
        Método responsável por buscar um aluguel em determinada classe por seu owner_id

        Parameters
        ----------
        owner_id: string
        cls:__type__

        Returns
        -------
        response: __type__
        Entidade filtrada por seu id

        """
        return db.session.query(cls).filter_by(owner_id=owner_id).all()

    @classmethod
    def find_open_rent_by_imombile(cls, immobile_id):
        """
        Método responsável por buscar um aluguel em aberto por seu immobile_id

        Parameters
        ----------
        immobile_id: string
        cls:__type__

        Returns
        -------
        response: __type__
        Entidade filtrada por seu id

        """
        return (
            db.session.query(cls)
            .filter_by(immobile_id=immobile_id, end_date=None)
            .first()
        )

    @classmethod
    def find_open_rent_by_tenant(cls, tenant_id):
        """
        Método responsável por buscar um aluguel em em aberto por seu tenant_id

        Parameters
        ----------
        tenant_id: string
        cls:__type__

        Returns
        -------
        response: __type__
        Entidade filtrada por seu id

        """
        return db.session.query(cls).filter_by(tenant_id=tenant_id, end_date=None).first()

    @classmethod
    def find_open_rent_by_owner(cls, owner_id):
        """
        Método responsável por buscar um aluguel em em aberto por seu owner_id

        Parameters
        ----------
        owner_id: string
        cls:__type__

        Returns
        -------
        response: __type__
        Entidade filtrada por seu id

        """
        return db.session.query(cls).filter_by(owner_id=owner_id, end_date=None).first()

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
            "deed_id": self.deed_id,
            "rent_contract_id": self.rent_contract_id,
        }
