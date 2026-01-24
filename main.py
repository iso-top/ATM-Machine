import psycopg
from infrastructure.persistence.db_connection import DatabaseConnection


# Пробуем явное соединение по localhost
db = DatabaseConnection(
    host="localhost",
    port=5432,
    dbname="atm_machine",
    user="postgres",
    password="postgres"
)
db.get_connection()