from flask import jsonify


def make_exception_response(
    description: str = "", message: str = "Ocorreu um erro no servidor."
):
    """
    Responses 500
    """

    response = jsonify({"message": message, "description": description})

    response.status_code = 500

    return response


def make_success_response(message: str, data=None, status_code=200, **kwargs):
    """
    Responses 200
    """

    response = {"status": status_code, "message": message}

    if data is not None:
        response["data"] = data

    for key, value in kwargs.items():
        response[key] = value

    response = jsonify(response)

    response.status_code = status_code

    return response
