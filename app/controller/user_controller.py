import json
from datetime import datetime
from models.user_model import User, db


""" Run anomaly detection inference based on interval passed in database.ini file """
def add_user(json_data):
    print('\n\n\n\n\n###########')
    print('{} - Script starting'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    print('###########\n\n\n\n\n')
    print('Adding the user into database\n\n\n\n\n')
    id = json_data["id"]
    name = json_data['name']
    email = json_data['email']
    password = json_data['password']
    phone = json_data['phone']
    address = json_data['address']

    user = User(id,name,email,password,phone,address)
    print(user.id,flush=True)
    db.session.add(user)
    db.session.commit()
    #j = jsonify(i=id, n=name,e=email,p=password,ph=phone,t=type)    
    #res = j
    #res = list(map(lambda x: json.loads(x), res))
    #print(res)
    print('\n\n\n\n\n###########')
    print('{} - Script ending'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    print('###########\n\n\n\n\n')
