import psycopg
from psycopg.rows import dict_row

class DatabaseConnection:
    def __init__(self, host: str, port: int, dbname: str, user: str, password: str):
        self._host = host
        self._port = port
        self._dbname = dbname
        self._user = user
        self._password = password

    def get_connection(self):
        print(f"HOST: {self._host}, PORT: {self._port}, DB: {self._dbname}, USER: {self._user}")

        conn = psycopg.connect(
            host=self._host,
            port=self._port,
            dbname=self._dbname,
            user=self._user,
            password=self._password,
            row_factory=dict_row  # чтобы курсор возвращал словари
        )
        return conn

