from extensions import db
from models.tenant_model import Tenant
from models.user_model import User
from models.rent_contract_model import RentContract
from shared.app_errors import AppError


""" Controller responsible for adding and deleting tenants endpoints """


def add_tenant(json_data):
    """
    Método responsável por receber o JSON de entrada e criar um inquilino

    Parameters
    ----------
    json_data: _type_
        JSON recebido pelo método POST via request com os dados para criação de um inquilino

    Returns
    -------
     response: _type_
        JSON com os atributos do inquilino criado

    """
    name = json_data["name"]
    email = json_data["email"]
    password = json_data["password"]
    phone = json_data["phone"]

    description = json_data["description"]
    rent_contract_number = json_data["rent_contract_number"]

    rent_contract = RentContract(description, rent_contract_number)

    tenant = User.find_by_email(email)

    if tenant is not None:
        raise AppError("Já existe um inquilino com estes dados.")

    tenant = Tenant(name, email, password, phone, rent_contract.id)

    try:
        db.session.add(rent_contract)
        db.session.add(tenant)
        db.session.commit()

    except Exception as error:
        raise AppError(
            "Não foi possível cadastrar o inqulino.",
            description=error.__str__(),
        )

    return tenant.transform_to_json()


def show_tenants():
    """
    Método responsável por listar todos os inquilinos existentes

    Parameters
    ----------


    Returns
    -------
     response: _type_
        JSON com os atributos dos inquilinos criados

    """

    try:
        tenants = Tenant.list_all()

    except Exception as error:
        raise AppError(
            "Não foi possível listar os inquilinos.", description=error.__str__()
        )

    tenants_in_json = []

    for tenant in tenants:
        tenants_in_json.append(tenant.transform_to_json())

    return tenants_in_json


def get_tenant_by_id(tenant_id):
    """
    Método responsável por recuperar o inquilinos existente por seu id

    Parameters
    ----------


    Returns
    -------
     response: _type_
        JSON com os atributos do inquilino recuperado

    """
    try:
        tenant = User.find_by_id(tenant_id)

    except Exception as error:
        raise AppError(
            "Não foi possível buscar o inquilino.", description=error.__str__()
        )

    return tenant.transform_to_json()
