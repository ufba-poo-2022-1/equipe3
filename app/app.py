from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse, fields, marshal
from controller.user_controller import add_user
from controller.building_controller import add_building
from datetime import datetime
from threading import Thread



db = SQLAlchemy()

# Function that create the app
def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # Simple route
    @app.route("/")
    def hello_world():
        return jsonify({"status": "success", "message": "Hello World!"})

    return app  # do not forget to return the app


app = create_app()
api = Api(app)

@app.before_first_request
def init_db():
    from models import (
        address_model,
        immobile_model,
        owner_model,
        tenant_model,
        user_model,
    )

    db.create_all()


# APIs
class AddUserAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(AddUserAPI, self).__init__()

    def post_task(self,j):
        add_user(j)
        pass

    def post(self):
        args = self.reqparse.parse_args()

        json_data = request.get_json(force=True)
        un = json_data['username']
        pw = json_data['password']
        #args = parser.parse_args()
        #un = str(args['username'])
        #pw = str(args['password'])
        j = jsonify(u=un, p=pw)


        start_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        thread = Thread(target=self.post_task(j))
        thread.start()

        end_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        status = 'OK'

        result = {
            'start_date': start_date,
            'end_date': end_date,
            'status': status
        }
        api_fields = {
            'start_date': fields.String,
            'end_date': fields.String,
            'status': fields.String
        }
        return {'add_user': marshal(result, api_fields)}, 201

class AddBuildingAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(AddBuildingAPI, self).__init__()

    def get_task(self,id):
        add_building(id)
        pass

    def get(self,id):
        args = self.reqparse.parse_args()
        start_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        thread = Thread(target=self.get_task(id))
        thread.start()

        end_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        status = 'OK'

        result = {
            'start_date': start_date,
            'end_date': end_date,
            'status': status
        }
        api_fields = {
            'start_date': fields.String,
            'end_date': fields.String,
            'status': fields.String
        }
        return {'add_building': marshal(result, api_fields)}, 201

# Routes
api.add_resource(AddUserAPI, '/mobx/api/add_user', endpoint='add_user')
api.add_resource(AddBuildingAPI, '/mobx/api/add_building','/mobx/api/add_building/<id>', endpoint='add_building')




if __name__ == "__main__":
    # App.run(host='0.0.0.0', port=5000, debug=True)
    app.run(debug=True)
