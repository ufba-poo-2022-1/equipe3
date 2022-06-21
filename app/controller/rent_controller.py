import json
from datetime import datetime
from models.rent_model import Rent, db


""" Controller responsible for adding user endpoints """
def add_rent(json_data):
    print('\n\n\n\n\n###########')
    print('{} - Script starting'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    print('###########\n\n\n\n\n')
    print('Adding the rent into database\n\n\n\n\n')
    start_date = json_data['start_date']
    end_date = json_data['end_date']
    expected_return_date = json_data['expected_return_date']
    total = json_data['total']
    fine_amount = json_data['fine_amount']
    owner_id = json_data['owner_id']
    immobile_id = json_data['immobile_id']

    tenant_id = json_data['tenant_id']

    rent = Rent(start_date,end_date,expected_return_date,total,fine_amount,owner_id,tenant_id,immobile_id)

    db.session.add(rent)
    db.session.commit()
    #j = jsonify(i=id, n=name,e=email,p=password,ph=phone,t=type)    
    #res = j
    #res = list(map(lambda x: json.loads(x), res))
    #print(res)
    print('\n\n\n\n\n###########')
    print('{} - Script ending'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    print('###########\n\n\n\n\n')
