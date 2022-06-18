from datetime import datetime
from extensions import db
from models.owner_model import Owner


""" Controller responsible for adding and deleting user endpoints """


def add_owner(json_data):
    print("\n\n\n\n\n###########")
    print("{} - Script starting".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    print("###########\n\n\n\n\n")
    print("Adding the user into database\n\n\n\n\n")
    name = json_data["name"]
    email = json_data["email"]
    password = json_data["password"]
    phone = json_data["phone"]
    #Where does it come from?
    deed_id = json_data["deed_id"]

    owner = Owner(name, email, password, phone, deed_id)

    db.session.add(owner)
    db.session.commit()

    # j = jsonify(i=id, n=name,e=email,p=password,ph=phone,t=type)
    # res = j
    # res = list(map(lambda x: json.loads(x), res))
    # print(res)
    print("\n\n\n\n\n###########")
    print("{} - Script ending".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    print("###########\n\n\n\n\n")


def show_owners():
    print("\n\n\n\n\n###########")
    print("{} - Script starting".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    print("###########\n\n\n\n\n")
    print("Showing active users\n\n\n\n\n")

    # Fetch all customer records
    records = db.session.query(Owner.name).all()

    # Loop over records
    for record in records:
        print(record)

    # db.session.commit()

    print("\n\n\n\n\n###########")
    print("{} - Script ending".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    print("###########\n\n\n\n\n")


def get_owners(json_data):
    print("\n\n\n\n\n###########")
    print("{} - Script starting".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    print("###########\n\n\n\n\n")
    print("Showing active users\n\n\n\n\n")

    id = json_data["id"]

    # Fetch all customer records
    print(db.session.query(Owner).get(id))


    # db.session.commit()

    print("\n\n\n\n\n###########")
    print("{} - Script ending".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    print("###########\n\n\n\n\n")