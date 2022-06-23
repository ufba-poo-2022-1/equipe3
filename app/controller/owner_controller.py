from extensions import db
from models.owner_model import Owner
from models.user_model import User
from shared.app_errors import AppError


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

    owner = User.find_by_email(email)

    if owner is not None:
        raise AppError("Já existe um proprietário com estes dados.")

    owner = Owner(name, email, password, phone, deed_id)

    try:
        db.session.add(owner)
        db.session.commit()

    except Exception as error:
        raise AppError(
            "Não foi possível cadastrar um proprietário.", description=error.__str__()
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
        owners = Owner.list_all()

    except Exception as error:
        raise AppError(
            "Não foi possível listar os proprietários.", description=error.__str__()
        )

    owners_in_json = []

    for owner in owners:
        owners_in_json.append(owner.transform_to_json())

    return owners_in_json


def get_owner_by_id(owner_id):
    try:
        owner = User.find_by_id(owner_id)

    except Exception as error:
        raise AppError(
            "Não foi possível buscar o proprietário.", description=error.__str__()
        )

    return owner.transform_to_json()
