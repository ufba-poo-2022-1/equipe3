from flask import Flask, jsonify

from database import db
from config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Function that create the app
def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Simple route
    @app.route("/")
    def hello_world():
        return jsonify({"status": "success", "message": "Hello World!"})

    return app  # do not forget to return the app


app = create_app()


@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == "__main__":
    db.init_app(app)
    # App.run(host='0.0.0.0', port=5000, debug=True)
    app.run(debug=True)
