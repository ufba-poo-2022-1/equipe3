import sqlite3

from backend.solution.utils.config import DB_PATH


class DAO:
    def __init__(self):
        self.db_client = sqlite3.connect(DB_PATH, check_same_thread=False)

    def insert_data(self, dic):
        cursor = self.db_client.cursor()
        cursor.executemany(dic["sql"], dic["data"])
        self.db_client.commit()

    def select_data(self, sql):
        cursor = self.db_client.cursor()
        cursor.execute(sql)
        res = cursor.fetchall()
        return res

    def update_data(self, sql):
        cursor = self.db_client.cursor()
        cursor.execute(sql)
        self.db_client.commit()
        cursor.fetchall()
        return None

    def close(self):
        self.db_client.close()
