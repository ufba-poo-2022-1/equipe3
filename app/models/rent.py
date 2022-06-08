class Rent:
    def __init__(
        self,
        id,
        id_landlord,
        id_tenant,
        id_building,
        initial_date,
        final_date,
        projected_date,
        total,
        fee,
        creation_date,
    ):
        self.__id = id
        self.__id_landlord = id_landlord
        self.__id_tenant = id_tenant
        self.__id_building = id_building
        self.__initial_date = initial_date
        self.__final_date = final_date
        self.__projected_date = projected_date
        self.__total = total
        self.__fee = fee
        self.__creation_date = creation_date

    def get_dados(self):
        return [
            self.__id,
            self.__id_landlord,
            self.__id_tenant,
            self.__id_building,
            self.__initial_date,
            self.__final_date,
            self.__projected_date,
            self.__total,
            self.__fee,
            self.__creation_date,
        ]
