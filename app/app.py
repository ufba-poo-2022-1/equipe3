from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse, fields, marshal
from datetime import datetime
from threading import Thread

from extensions import db
from controller.tenant_controller import add_tenant, show_tenants, get_tenants
from controller.owner_controller import add_owner, show_owners, get_owners
from controller.immobile_controller import add_house, add_apartment, show_immobiles
from controller.rent_controller import add_rent, cancel_rent, show_rent
from shared.responses import make_exception_response, make_success_response
from shared.app_errors import AppError


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


@app.errorhandler(AppError)
def handle_exception(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code

    return response


@app.errorhandler(Exception)
def handle_exception(error):
    return make_exception_response(description=error.__str__())


# APIs
class AddTenantAPI(Resource):
    # def __init__(self):
    #     self.reqparse = reqparse.RequestParser()
    #     super(AddTenantAPI, self).__init__()

    # def post_task(self, j):
    #     add_tenant(j)

    def post(self):
        json_data = request.get_json(force=True)

        tenant = add_tenant(json_data)

        return make_success_response(
            message="Inquilino criado com sucesso.",
            data=tenant,
            status_code=201,
        )

class AddRentAPI(Resource):
    # def __init__(self):
    #     self.reqparse = reqparse.RequestParser()
    #     super(AddTenantAPI, self).__init__()

    # def post_task(self, j):
    #     add_tenant(j)

    def post(self):
        json_data = request.get_json(force=True)

        rent = add_rent(json_data)

        return make_success_response(
            message="Aluguel criado com sucesso.",
            data=rent,
            status_code=201,
        )


class AddOwnerAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(AddOwnerAPI, self).__init__()

    def post_task(self, j):
        add_owner(j)

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
        return {"add_owner": marshal(result, api_fields)}, 201


class AddImmobileAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(AddImmobileAPI, self).__init__()

    def post_task(self, j):
        if j["flag"] == 1:
            add_house(j)
        else:
            add_apartment(j)

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
        return {"list_tenants": marshal(result, api_fields)}, 201


class ListOwnersAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(ListOwnersAPI, self).__init__()

    def get_task(self):
        show_owners()

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
        return {"list_owners": marshal(result, api_fields)}, 201


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


class GetTenantById(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(GetTenantById, self).__init__()

    def post_task(self, j):
        get_tenants(j)

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
        return {"get_tenant_by_id": marshal(result, api_fields)}, 201


class GetOwnersById(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(GetOwnersById, self).__init__()

    def post_task(self, j):
        get_owners(j)

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
        return {"get_owners_by_id": marshal(result, api_fields)}, 201

class CancelRentById(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(GetOwnersById, self).__init__()

    def post_task(self, j):
        cancel_rent(j)

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
        return {"cancel_rent_by_id": marshal(result, api_fields)}, 201

class ShowRentByUserId(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(GetOwnersById, self).__init__()

    def post_task(self, j):
        show_rent(j)

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
        return {"show_rent_by_user_id": marshal(result, api_fields)}, 201


# Routes
api.add_resource(AddTenantAPI, "/mobx/api/add_tenant", endpoint="add_tenant")
api.add_resource(AddRentAPI, "/mobx/api/add_rent", endpoint="add_rent")
api.add_resource(AddOwnerAPI, "/mobx/api/add_owner", endpoint="add_owner")
api.add_resource(AddImmobileAPI, "/mobx/api/add_immobile", endpoint="add_immobile")
api.add_resource(ListTenantsAPI, "/mobx/api/list_tenants", endpoint="list_tenants")
api.add_resource(ListOwnersAPI, "/mobx/api/list_owners", endpoint="list_owners")
api.add_resource(ListImmobilesAPI, "/mobx/api/list_immobiles", endpoint="list_immobiles")
api.add_resource(GetTenantById, "/mobx/api/get_tenant_by_id", endpoint="get_tenant_by_id")
api.add_resource(GetOwnersById, "/mobx/api/get_owners_by_id", endpoint="get_owners_by_id")
api.add_resource(CancelRentById, "/mobx/api/cancel_rent_by_id", endpoint="cancel_rent_by_id")
api.add_resource(ShowRentByUserId, "/mobx/api/show_rent_by_user_id", endpoint="show_rent_by_user_id")


if __name__ == "__main__":
    # App.run(host='0.0.0.0', port=5000, debug=True)
    app.run(debug=True)
