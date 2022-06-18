from datetime import datetime
from extensions import db
from models.tenant_model import Tenant


""" Controller responsible for adding and deleting user endpoints """


def add_tenant(json_data):
    print("\n\n\n\n\n###########")
    print("{} - Script starting".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    print("###########\n\n\n\n\n")
    print("Adding the user into database\n\n\n\n\n")
    name = json_data["name"]
    email = json_data["email"]
    password = json_data["password"]
    phone = json_data["phone"]
    #Where does it come from?
    rent_contract = json_data["rent_contract"]

    tenant = Tenant(name, email, password, phone, rent_contract)

    db.session.add(tenant)
    db.session.commit()

    # j = jsonify(i=id, n=name,e=email,p=password,ph=phone,t=type)
    # res = j
    # res = list(map(lambda x: json.loads(x), res))
    # print(res)
    print("\n\n\n\n\n###########")
    print("{} - Script ending".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    print("###########\n\n\n\n\n")


def show_tenants():
    print("\n\n\n\n\n###########")
    print("{} - Script starting".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    print("###########\n\n\n\n\n")
    print("Showing active users\n\n\n\n\n")

    # Fetch all customer records
    records = db.session.query(Tenant.name).all()

    # Loop over records
    for record in records:
        print(record)

    # db.session.commit()

    print("\n\n\n\n\n###########")
    print("{} - Script ending".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    print("###########\n\n\n\n\n")
