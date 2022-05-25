from flask import Flask, jsonify
from database import db

# Function that create the app
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Simple route
    @app.route("/")
    def hello_world():
        return jsonify({"status": "success", "message": "Hello World!"})

    return app  # do not forget to return the app


APP = create_app()

if __name__ == "__main__":
    db.init_app(APP)
    # APP.run(host='0.0.0.0', port=5000, debug=True)
    APP.run(debug=True)
