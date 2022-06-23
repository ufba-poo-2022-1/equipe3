from extensions import db
from models.tenant_model import Tenant
from models.user_model import User
from shared.app_errors import AppError


""" Controller responsible for adding and deleting user endpoints """


def add_tenant(json_data):
    name = json_data["name"]
    email = json_data["email"]
    password = json_data["password"]
    phone = json_data["phone"]
    rent_contract_id = None

    # Where does it come from?
    if "rent_contract_id" in json_data:
        rent_contract_id = json_data["rent_contract_id"]

    tenant = User.find_by_email(email)

    if tenant is not None:
        raise AppError("Já existe um inquilino com estes dados.")

    tenant = Tenant(name, email, password, phone, rent_contract_id)

    try:
        db.session.add(tenant)
        db.session.commit()

    except Exception as error:
        raise AppError(
            "Não foi possível cadastrar o inqulino.",
            description=error.__str__(),
        )

    return tenant.transform_to_json()


def show_tenants():
    # Fetch all customer records
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
    try:
        tenant = User.find_by_id(tenant_id)

    except Exception as error:
        raise AppError(
            "Não foi possível buscar o inquilino.", description=error.__str__()
        )

    return tenant.transform_to_json()
