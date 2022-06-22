import json
from datetime import datetime
from models.rent_model import Rent, db


""" Controller responsible for adding rents endpoints """
def add_rent(json_data):

    start_date = json_data['start_date']
    end_date = json_data['end_date']
    expected_return_date = json_data['expected_return_date']
    total = json_data['total']
    fine_amount = json_data['fine_amount']
    owner_id = json_data['owner_id']
    immobile_id = json_data['immobile_id']
    tenant_id = json_data['tenant_id']

    rent = Rent(start_date,end_date,expected_return_date,total,fine_amount,owner_id,immobile_id,tenant_id)

    db.session.add(rent)
    db.session.commit()


def cancel_rent(json_data):
    print("\n\n\n\n\n###########")
    print("{} - Script starting".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    print("###########\n\n\n\n\n")
    print("Showing active users\n\n\n\n\n")

    id = json_data["id"]

    # TODO - Crud to cancel RENT
    #print(db.session.query(Owner).get(id))


    # db.session.commit()

    print("\n\n\n\n\n###########")
    print("{} - Script ending".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    print("###########\n\n\n\n\n")

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