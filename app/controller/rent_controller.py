from datetime import datetime

from extensions import db
from models.rent_model import Rent
from models.immobile_model import Immobile
from models.user_model import User
from shared.app_errors import AppError


""" Controller responsible for adding rents endpoints """


def add_rent(json_data):
    """
    Método responsável por receber o JSON de entrada e criar o aluguel

    Parameters
    ----------
    json_data: _type_
        JSON recebido pelo método POST via request com os dados para criação de um aluguel

    Returns
    -------
     response: _type_
        JSON com os atributos do aluguel criado

    """
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

    owner = User.find_by_id(owner_id)
    tenant = User.find_by_id(tenant_id)

    rent = Rent(
        start_date,
        expected_return_date,
        owner_id,
        immobile_id,
        tenant_id,
        deed_id=owner.deed_id,
        rent_contract_id=tenant.rent_contract_id,
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
    """
    Método responsável por receber o JSON de entrada e devolver o aluguel

    Parameters
    ----------
    json_data: _type_
        JSON recebido pelo método POST via request com os dados para devolução de um aluguel

    Returns
    -------
     response: _type_
        JSON com os atributos do aluguel devolvido

    """

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
    """
    Método responsável por listar todos os aluguéis associados a um inquilino

    Parameters
    ----------
    tenant_id: _type_
        id to inquilino a ser recuperado

    Returns
    -------
     response: _type_
        JSON com os atributos do aluguéis associados àquele inquilino

    """
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


def show_owner_rents(owner_id):
    """
    Método responsável por listar todos os aluguéis associados a um dono

    Parameters
    ----------
    tenant_id: _type_
        id to dono a ser recuperado

    Returns
    -------
     response: _type_
        JSON com os atributos do aluguéis associados àquele dono

    """
    try:
        rents = Rent.find_by_owner_id(owner_id)

    except Exception as error:
        raise AppError(
            "Não foi possível listar os aluguéis do proprietário.",
            description=error.__str__(),
        )

    rents_in_json = []

    for rent in rents:
        rents_in_json.append(rent.transform_to_json())

    return rents_in_json
