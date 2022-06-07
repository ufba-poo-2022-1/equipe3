from datetime import datetime
from models.immobile_model import Immobile, db


""" Controller responsible for adding and deleting immobiles endpoints """
def add_building(json_data):
    print('\n\n\n\n\n###########')
    print('{} - Script starting'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    print('###########\n\n\n\n\n')
    print('Adding the user into database\n\n\n\n\n')
    id = json_data["id"]
    type = json_data['type']
    description = json_data['description']
    address = json_data['address']
    value = json_data['value']
    area = json_data['area']
    is_available = json_data['is_available']

    immobile = Immobile(id,type,description,address,value,area,is_available)

    db.session.add(immobile)
    db.session.commit()
    #j = jsonify(i=id, n=name,e=email,p=password,ph=phone,t=type)    
    #res = j
    #res = list(map(lambda x: json.loads(x), res))
    #print(res)
    print('\n\n\n\n\n###########')
    print('{} - Script ending'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    print('###########\n\n\n\n\n')