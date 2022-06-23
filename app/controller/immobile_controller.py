from extensions import db

from models.apartment_model import Apartment
from models.house_model import House
from models.immobile_model import Immobile
from models.address_model import Address
from shared.responses import make_exception_response


""" Controller responsible for adding and deleting immobiles endpoints """


def add_apartment(json_data):
    # Apartment fields
    description = json_data["description"]
    daily_rate = json_data["daily_rate"]
    fine_amount = json_data["fine_amount"]
    area = json_data["area"]
    is_available = json_data["is_available"]
    floor = json_data["floor"]

    # Address fields
    street = json_data["street"]
    number = json_data["number"]
    district = json_data["district"]
    city = json_data["city"]
    cep = json_data["cep"]
    complement = json_data["complement"]
    user_id = json_data["user_id"]

    apartment = Apartment(description, daily_rate, fine_amount, area, is_available, floor)

    address = Address(
        street=street,
        number=number,
        district=district,
        city=city,
        cep=cep,
        complement=complement,
        user_id=user_id,
        immobile_id=apartment.id,
    )

    try:
        db.session.add(apartment)
        db.session.add(address)
        db.session.commit()

    except Exception as error:
        return make_exception_response(
            description=error,
            message="Não foi possível cadastrar um apartamento",
        )

    return apartment.transform_to_json()


def add_house(json_data):

    # House fields
    description = json_data["description"]
    value = json_data["value"]
    area = json_data["area"]
    is_available = json_data["is_available"]
    backyard = json_data["backyard"]
    pool = json_data["pool"]

    # Address fields
    street = json_data["street"]
    number = json_data["number"]
    district = json_data["district"]
    city = json_data["city"]
    cep = json_data["cep"]
    complement = json_data["complement"]
    user_id = json_data["user_id"]

    house = House(description, value, area, is_available, backyard, pool)

    address = Address(
        street=street,
        number=number,
        district=district,
        city=city,
        cep=cep,
        complement=complement,
        user_id=user_id,
        immobile_id=house.id,
    )

    try:
        db.session.add(house)
        db.session.add(address)
        db.session.commit()

    except Exception as error:
        return make_exception_response(
            description=error,
            message="Não foi possível cadastrar um apartamento",
        )

    return house.transform_to_json()


def show_immobiles():
    # Fetch all customer records
    try:
        immobiles = Immobile.query.all()

    except Exception as error:
        return make_exception_response(
            description=error.__str__(), message="Não foi possível listar os imóveis"
        )

    immobiles_in_json = []

    for immobile in immobiles:
        immobiles_in_json.append(immobile.transform_to_json())

    return immobiles_in_json
