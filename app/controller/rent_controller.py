from datetime import datetime

from extensions import db
from models.rent_model import Rent
from models.immobile_model import Immobile
from shared.app_errors import AppError


""" Controller responsible for adding rents endpoints """


def add_rent(json_data):
    owner_id = json_data["owner_id"]
    immobile_id = json_data["immobile_id"]
    tenant_id = json_data["tenant_id"]

    try:
        start_date = datetime.strptime(json_data["start_date"], "%Y/%m/%d %H:%M")
        expected_return_date = datetime.strptime(
            json_data["expected_return_date"], "%Y/%m/%d %H:%M"
        )

    except ValueError as error:
        raise AppError("A data está em um formato inválido.", description=error.__str__())

    minimum_rent_hour = 24

    rent_open_to_immobile = Rent.find_open_rent_by_imombile(immobile_id)
    rent_open_to_tenant = Rent.find_open_rent_by_tenant(tenant_id)
    rent_open_to_owner = Rent.find_open_rent_by_owner(owner_id)

    if rent_open_to_immobile:
        raise AppError("Já existe um aluguel em aberto para esse imóvel.")

    if rent_open_to_tenant:
        raise AppError("Já existe um aluguel em aberto para esse inquilino.")

    if rent_open_to_owner:
        raise AppError("Já existe um aluguel em aberto para esse proprietário.")

    date_now = start_date or datetime.now()
    compare = (expected_return_date - date_now).total_seconds() // 3600

    if compare < minimum_rent_hour:
        raise AppError("Data de retorno inválida.")

    rent = Rent(
        start_date,
        expected_return_date,
        owner_id,
        immobile_id,
        tenant_id,
    )

    immobile = Immobile.find_by_id(immobile_id)

    immobile.is_available = False

    try:
        db.session.add(rent)
        db.session.add(immobile)
        db.session.commit()

    except Exception as error:
        raise AppError(
            "Não foi possível cadastrar um aluguel",
            description=error.__str__(),
        )

    return rent.transform_to_json()


def deliver_rent(json_data):
    rent_id = json_data["id"]

    rent = Rent.find_by_id(rent_id)

    if not rent:
        raise AppError("Aluguel não encontrado")

    immobile = Immobile.find_by_id(rent.immobile_id)

    date_now = datetime.now()

    mininum_daily = 1

    daily = (date_now - rent.start_date).days

    if daily <= 0:
        daily = mininum_daily

    delay = (date_now - rent.expected_return_date).days

    total = 0

    if delay > 0:
        fine = delay * immobile.fine_amount
        total = fine

    total += daily * immobile.daily_rate

    rent.end_date = date_now
    rent.total = total

    immobile.is_available = True

    db.session.commit()

    return rent.transform_to_json()


def show_tenant_rents(tenant_id):
    try:
        rents = Rent.find_by_tenant_id(tenant_id)

    except Exception as error:
        raise AppError(
            "Não foi possível listar os aluguéis do inquilo.", description=error.__str__()
        )

    rents_in_json = []

    for rent in rents:
        rents_in_json.append(rent.transform_to_json())

    return rents_in_json

def show_rent(json_data):
    print("\n\n\n\n\n###########")
    print("{} - Script starting".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    print("###########\n\n\n\n\n")
    print("Showing active users\n\n\n\n\n")

    id = json_data["id"]

    # TODO - Crud to show RENT by user id
    #print(db.session.query(Owner).get(id))


    # db.session.commit()

    print("\n\n\n\n\n###########")
    print("{} - Script ending".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    print("###########\n\n\n\n\n")