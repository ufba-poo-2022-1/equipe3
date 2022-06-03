from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

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


if __name__ == "__main__":
    # App.run(host='0.0.0.0', port=5000, debug=True)
    app.run(debug=True)
