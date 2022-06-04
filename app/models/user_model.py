from extensions import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    phone = db.Column(db.String(120))
    type = db.Column(db.String(128))

    # TODO: Add address filed

    def __init__(self, id, name, email, password, celphone, address):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.celphone = celphone
        self.address = address

    def get_id(self):
        return self.id

    def get_data(self):
        return [
            self.__id,
            self.__name,
            self.__email,
            self.__password,
            self.__celphone,
            self.__address,
        ]

    def set_cellphone(self, number):
        self.__celphone = number
        return 0

    def set_email(self, email):
        self.__email = email
        return 0

    def set_password(self, password):
        self.__password = password
        return 0
