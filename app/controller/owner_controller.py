from datetime import datetime
from extensions import db
from models.owner_model import Owner
from shared.app_errors import AppError
from shared.responses import make_exception_response


""" Controller responsible for adding and deleting owners endpoints """


def add_owner(json_data):
    """
    Método responsável por receber o JSON de entrada e criar o dono

    Parameters
    ----------
    json_data: _type_
        JSON recebido pelo método POST via request com os dados para criação de um dono

    Returns
    -------
     response: _type_
        JSON com os atributos do dono criado

    """

    name = json_data["name"]
    email = json_data["email"]
    password = json_data["password"]
    phone = json_data["phone"]

    deed_id = None

    if "deed_id" in json_data:
        deed_id = json_data["deed_id"]

    owner = Owner(name, email, password, phone, deed_id)

    owner = Owner.query.filter_by(email=email).first()

    if owner is not None:
        raise AppError("Já existe um dono com estes dados.")

    owner = Owner(name, email, password, phone, deed_id)

    try:
        db.session.add(owner)
        db.session.commit()

    except Exception as error:
        return make_exception_response(
            description=error.__str__(), message="Não foi possível cadastrar o dono."
        )

    return owner.transform_to_json()


def show_owners():
    """
    Método responsável por listar todos os donos existentes

    Parameters
    ----------
    

    Returns
    -------
     response: _type_
        JSON com os atributos dos donos criados

    """

    # Fetch all customer records
    try:
        owners = Owner.query.all()

    except Exception as error:
        return make_exception_response(
            description=error, message="Não foi possível listar os donos."
        )

    owners_in_json = []

    for owner in owners:
        owners_in_json.append(owner.transform_to_json())

    return owners_in_json


def get_owners(json_data):
    """
    Método responsável por retornas os ids dos donos existentes

    Parameters
    ----------
    

    Returns
    -------
     response: _type_
        resposta com os ids dos donos criados

    """


    id = json_data["id"]

    # Fetch all customer records
    print(db.session.query(Owner).get(id))

