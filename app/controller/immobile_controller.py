from datetime import datetime
from extensions import db

from models.apartment_model import Apartment
from models.house_model import House
from models.immobile_model import Immobile



""" Controller responsible for adding and deleting immobiles endpoints """
def add_apartment(json_data):
    print('\n\n\n\n\n###########')
    print('{} - Script starting'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    print('###########\n\n\n\n\n')
    print('Adding the Apartment into database\n\n\n\n\n')

    description = json_data['description']
    value = json_data['value']
    area = json_data['area']
    is_available = json_data['is_available']
    floor = json_data['floor']

    apartment = Apartment(description,value,area,is_available,floor)

    db.session.add(apartment)
    db.session.commit()
    #j = jsonify(i=id, n=name,e=email,p=password,ph=phone,t=type)    
    #res = j
    #res = list(map(lambda x: json.loads(x), res))
    #print(res)
    print('\n\n\n\n\n###########')
    print('{} - Script ending'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    print('###########\n\n\n\n\n')

def add_house(json_data):
    print('\n\n\n\n\n###########')
    print('{} - Script starting'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    print('###########\n\n\n\n\n')
    print('Adding the user into database\n\n\n\n\n')
    description = json_data['description']
    value = json_data['value']
    area = json_data['area']
    is_available = json_data['is_available']
    backyard = json_data['backyard']
    pool = json_data['pool']


    house = House(description,value,area,is_available,backyard,pool)

    db.session.add(house)
    db.session.commit()
    #j = jsonify(i=id, n=name,e=email,p=password,ph=phone,t=type)    
    #res = j
    #res = list(map(lambda x: json.loads(x), res))
    #print(res)
    print('\n\n\n\n\n###########')
    print('{} - Script ending'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    print('###########\n\n\n\n\n')


def show_immobiles():
    print('\n\n\n\n\n###########')
    print('{} - Script starting'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    print('###########\n\n\n\n\n')
    print('Showing active Immobiles\n\n\n\n\n')

    # Fetch all customer records
    records = db.session.query(Immobile.id).all()

    # Loop over records
    for record in records:
        print(record)


    #db.session.commit()

    print('\n\n\n\n\n###########')
    print('{} - Script ending'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    print('###########\n\n\n\n\n')