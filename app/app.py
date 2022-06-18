from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse, fields, marshal
from controller.tenant_controller import add_tenant, show_tenants
from controller.building_controller import add_building, show_immobiles
from datetime import datetime
from threading import Thread
from extensions import db


db = db

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
        apartment_model,
        house_model,
        immobile_model,
        owner_model,
        rent_model,
        tenant_model,
        user_model,
    )

    db.create_all()


# APIs
class AddTenantAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(AddTenantAPI, self).__init__()

    def post_task(self, j):
        add_tenant(j)

    def post(self):
        args = self.reqparse.parse_args()

        json_data = request.get_json(force=True)

        start_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        thread = Thread(target=self.post_task(json_data))
        thread.start()

        end_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = "OK"

        result = {"start_date": start_date, "end_date": end_date, "status": status}
        api_fields = {
            "start_date": fields.String,
            "end_date": fields.String,
            "status": fields.String,
        }
        return {"add_user": marshal(result, api_fields)}, 201


class AddImmobileAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(AddImmobileAPI, self).__init__()

    def post_task(self, j):
        add_building(j)

    def post(self):
        args = self.reqparse.parse_args()

        json_data = request.get_json(force=True)

        start_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        thread = Thread(target=self.post_task(json_data))
        thread.start()

        end_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = "OK"

        result = {"start_date": start_date, "end_date": end_date, "status": status}
        api_fields = {
            "start_date": fields.String,
            "end_date": fields.String,
            "status": fields.String,
        }
        return {"add_immobile": marshal(result, api_fields)}, 201


class ListTenantsAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(ListTenantsAPI, self).__init__()

    def get_task(self):
        show_tenants()

    def get(self):
        args = self.reqparse.parse_args()

        start_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        thread = Thread(target=self.get_task())
        thread.start()

        end_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = "OK"

        result = {"start_date": start_date, "end_date": end_date, "status": status}
        api_fields = {
            "start_date": fields.String,
            "end_date": fields.String,
            "status": fields.String,
        }
        return {"list_users": marshal(result, api_fields)}, 201


class ListImmobilesAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(ListImmobilesAPI, self).__init__()

    def get_task(self):
        show_immobiles()
        pass

    def get(self):
        args = self.reqparse.parse_args()

        start_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        thread = Thread(target=self.get_task())
        thread.start()

        end_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = "OK"

        result = {"start_date": start_date, "end_date": end_date, "status": status}
        api_fields = {
            "start_date": fields.String,
            "end_date": fields.String,
            "status": fields.String,
        }
        return {"list_immobiles": marshal(result, api_fields)}, 201


# Routes
api.add_resource(AddTenantAPI, "/mobx/api/add_tenant", endpoint="add_tenant")
api.add_resource(AddImmobileAPI, "/mobx/api/add_immobile", endpoint="add_immobile")
api.add_resource(ListTenantsAPI, "/mobx/api/list_tenants", endpoint="list_tenants")
api.add_resource(ListImmobilesAPI, "/mobx/api/list_immobiles", endpoint="list_immobiles")


if __name__ == "__main__":
    # App.run(host='0.0.0.0', port=5000, debug=True)
    app.run(debug=True)
