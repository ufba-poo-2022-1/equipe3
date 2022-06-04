from app import db


class Immobile(db.Model):
    __tablename__ = "immobiles"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(128))
    description = db.Column(db.String(128))
    value = db.Column(db.Float)
    area = db.Column(db.Float)
    is_available = db.Column(db.Boolean, default=True)

    # TODO: include adress field

    def __init__(self, id, type, description, address, value, area, is_available):
        self.__id = id
        self.__type = type
        self.__description = description
        self.__address = address
        self.__value = value
        self.__area = area
        self.__is_available = is_available

    def get_dados(self):
        return [
            self.__id,
            self.__type,
            self.__description,
            self.__address,
            self.__value,
            self.__area,
            self.__is_available,
        ]
