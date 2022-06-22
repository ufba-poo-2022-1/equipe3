from datetime import datetime

from extensions import db
from models.tenant_model import Tenant
from shared.app_errors import AppError
from shared.responses import make_exception_response


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

    tenant = Tenant.query.filter_by(email=email).first()

    if tenant is not None:
        raise AppError("Já existe um inquilino com estes dados.")

    tenant = Tenant(name, email, password, phone, rent_contract_id)

    try:
        db.session.add(tenant)
        db.session.commit()

    except Exception as error:
        return make_exception_response(
            description=error.__str__(), message="Não foi possível cadastrar o inqulino."
        )

    return tenant.transform_to_json()


def show_tenants():
    # Fetch all customer records
    try:
        tenants = Tenant.query.all()

    except Exception as error:
        return make_exception_response(
            description=error, message="Não foi possível listar os inquilinos."
        )

    tenants_in_json = []

    for tenant in tenants:
        tenants_in_json.append(tenant.transform_to_json())

    return tenants_in_json


def get_tenants(json_data):
    print("\n\n\n\n\n###########")
    print("{} - Script starting".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    print("###########\n\n\n\n\n")
    print("Showing active users\n\n\n\n\n")

    id = json_data["id"]

    # Fetch all customer records
    print(db.session.query(Tenant).get(id))

    # Loop over records

    # db.session.commit()

    print("\n\n\n\n\n###########")
    print("{} - Script ending".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    print("###########\n\n\n\n\n")
