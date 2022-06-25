from flask import Flask, jsonify, request
from flask_restful import Api, Resource

from extensions import db
from controller.tenant_controller import add_tenant, show_tenants, get_tenant_by_id
from controller.owner_controller import add_owner, get_owner_by_id, show_owners
from controller.immobile_controller import add_house, add_apartment, show_immobiles
from controller.rent_controller import (
    add_rent,
    deliver_rent,
    show_owner_rents,
    show_tenant_rents,
)
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
        deed_model,
        house_model,
        immobile_model,
        owner_model,
        rent_contract_model,
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
    """
    Classe que faz a herança da classe base Resource e define o roteamento dos métodos HTTP para sua URL.

    Parameters
    ----------
    json_data: _type_
        JSON recebido pelo método POST via request com os dados para criação de um Tenant

    Returns
    -------
     response: response
        resposta da requisição com o status da chamada no endpoint

    """

    def post(self):
        json_data = request.get_json(force=True)

        tenant = add_tenant(json_data)

        return make_success_response(
            message="Inquilino criado com sucesso.",
            data=tenant,
            status_code=201,
        )


class AddRentAPI(Resource):
    """
    Classe que faz a herança da classe base Resource e define o roteamento dos métodos HTTP para sua URL.

    Parameters
    ----------
    json_data: _type_
        JSON recebido pelo método POST via request com os dados para criação de um Rent

    Returns
    -------
     response: response
        resposta da requisição com o status da chamada no endpoint

    """

    def post(self):
        json_data = request.get_json(force=True)

        rent = add_rent(json_data)

        return make_success_response(
            message="Aluguel criado com sucesso.",
            data=rent,
            status_code=201,
        )


class AddOwnerAPI(Resource):
    """
    Classe que faz a herança da classe base Resource e define o roteamento dos métodos HTTP para sua URL.

    Parameters
    ----------
    json_data: _type_
        JSON recebido pelo método POST via request com os dados para criação de um Owner

    Returns
    -------
     response: response
        resposta da requisição com o status da chamada no endpoint

    """

    def post(self):
        json_data = request.get_json(force=True)

        owner = add_owner(json_data)

        return make_success_response(
            message="Proprietário criado com sucesso.",
            data=owner,
            status_code=201,
        )


class AddHouseAPI(Resource):
    """
    Classe que faz a herança da classe base Resource e define o roteamento dos métodos HTTP para sua URL.

    Parameters
    ----------
    json_data: _type_
        JSON recebido pelo método POST via request com os dados para criação de uma House

    Returns
    -------
     response: response
        resposta da requisição com o status da chamada no endpoint

    """

    def post(self):
        json_data = request.get_json(force=True)

        house = add_house(json_data)

        return make_success_response(
            message="Apartamento criado com sucesso.",
            data=house,
            status_code=201,
        )


class AddApartmentAPI(Resource):
    """
    Classe que faz a herança da classe base Resource e define o roteamento dos métodos HTTP para sua URL.

    Parameters
    ----------
    json_data: _type_
        JSON recebido pelo método POST via request com os dados para criação de um Apartment

    Returns
    -------
     response: response
        resposta da requisição com o status da chamada no endpoint

    """

    def post(self):
        json_data = request.get_json(force=True)

        apartment = add_apartment(json_data)

        return make_success_response(
            message="Apartamento criado com sucesso.",
            data=apartment,
            status_code=201,
        )


class ListTenantsAPI(Resource):
    """
    Classe que faz a herança da classe base Resource e define o roteamento dos métodos HTTP para sua URL.

    Parameters
    ----------
    GET: _type_
        Método GET para chamada do endpoint que lista os Tenants criados

    Returns
    -------
     response: response
        resposta da requisição com o status da chamada no endpoint

    """

    def get(self):
        tenants = show_tenants()

        return make_success_response(
            message="Inquilinos listados com sucesso.", data=tenants
        )


class ListOwnersAPI(Resource):
    """
    Classe que faz a herança da classe base Resource e define o roteamento dos métodos HTTP para sua URL.

    Parameters
    ----------
    GET: _type_
        Método GET para chamada do endpoint que lista os Owners criados

    Returns
    -------
     response: response
        resposta da requisição com o status da chamada no endpoint

    """

    def get(self):
        owners = show_owners()

        return make_success_response(
            message="Proprietários listados com sucesso.", data=owners
        )


class ListImmobilesAPI(Resource):
    """
    Classe que faz a herança da classe base Resource e define o roteamento dos métodos HTTP para sua URL.

    Parameters
    ----------
    GET: _type_
        Método GET para chamada do endpoint que lista os Immobiles criados

    Returns
    -------
     response: response
        resposta da requisição com o status da chamada no endpoint

    """

    def get(self):
        immobiles = show_immobiles()

        return make_success_response(
            message="Imóveis listados com sucesso.", data=immobiles
        )


class GetTenantById(Resource):
    """
    Classe que faz a herança da classe base Resource e define o roteamento dos métodos HTTP para sua URL.

    Parameters
    ----------
    json_data: _type_
        JSON recebido pelo método POST via request com os dados para buscar o Tenant

    Returns
    -------
     response: response
        resposta da requisição com o status da chamada no endpoint

    """

    def get(self, tenant_id):
        tenant = get_tenant_by_id(tenant_id)

        return make_success_response(
            message="Inquilino listado com sucesso.", data=tenant
        )


class GetOwnerById(Resource):
    """
    Classe que faz a herança da classe base Resource e define o roteamento dos métodos HTTP para sua URL.

    Parameters
    ----------
    json_data: _type_
        JSON recebido pelo método POST via request com os dados para buscar o Owner

    Returns
    -------
     response: response
        resposta da requisição com o status da chamada no endpoint

    """

    def get(self, owner_id):
        owner = get_owner_by_id(owner_id)

        return make_success_response(
            message="Proprietário listado com sucesso.", data=owner
        )


class DeliverRent(Resource):
    def post(self):
        json_data = request.get_json(force=True)

        rent = deliver_rent(json_data)

        return make_success_response(
            message="Aluguel devolvido com sucesso.",
            data=rent,
            status_code=200,
        )


class ShowTenantRents(Resource):
    def get(self, tenant_id):
        rents = show_tenant_rents(tenant_id)

        return make_success_response(message="Aluguéis listados com sucesso.", data=rents)


class ShowOwnerRent(Resource):
    def get(self, owner_id):
        rents = show_owner_rents(owner_id)

        return make_success_response(message="Aluguéis listados com sucesso.", data=rents)


# Routes
api.add_resource(AddTenantAPI, "/mobx/api/add_tenant", endpoint="add_tenant")
api.add_resource(AddRentAPI, "/mobx/api/add_rent", endpoint="add_rent")
api.add_resource(AddOwnerAPI, "/mobx/api/add_owner", endpoint="add_owner")
api.add_resource(AddHouseAPI, "/mobx/api/add_house", endpoint="add_house")
api.add_resource(AddApartmentAPI, "/mobx/api/add_apartment", endpoint="add_apartment")
api.add_resource(ListTenantsAPI, "/mobx/api/list_tenants", endpoint="list_tenants")
api.add_resource(ListOwnersAPI, "/mobx/api/list_owners", endpoint="list_owners")
api.add_resource(ListImmobilesAPI, "/mobx/api/list_immobiles", endpoint="list_immobiles")
api.add_resource(
    GetTenantById,
    "/mobx/api/get_tenant_by_id/<string:tenant_id>",
    endpoint="get_tenant_by_id",
)
api.add_resource(
    GetOwnerById,
    "/mobx/api/get_owner_by_id/<string:owner_id>",
    endpoint="get_owner_by_id",
)
api.add_resource(DeliverRent, "/mobx/api/deliver_rent", endpoint="deliver_rent")
api.add_resource(
    ShowTenantRents,
    "/mobx/api/show_tenant_rent/<string:tenant_id>",
    endpoint="show_tenant_rent",
)
api.add_resource(
    ShowOwnerRent,
    "/mobx/api/show_owner_rent/<string:owner_id>",
    endpoint="show_owner_rent",
)


if __name__ == "__main__":
    # App.run(host='0.0.0.0', port=5000, debug=True)
    app.run(debug=True)
