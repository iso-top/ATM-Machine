from application.domain.value_objects.password import Password
from application.domain.value_objects.number_card import Number_card
from application.domain.value_objects.pincode import Pincode
from application.domain.value_objects.balance import Balance
from application.domain.entities.account import Account
from application.repositories.account_repository import AccountRepository

import psycopg

class PostgresAccountRepository(AccountRepository):
    def __init__(self,connection):
        self._connection = connection

    def create(self, account):
        with self._connection as cursor:
            cursor.execute(
                """
                INSERT INTO accounts (card_number, pin, balance)
                VALUES (%s,%s,%s)
                """,
                (
                    account.card_number.value,
                    account.pin.value,
                    account.balance.amount
                )
            )
        self._connection.commit()

    def get_by_card(self, card_number: Number_card) -> Account | None:
        with self._connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT id,card_number, pin, balance
                FROM accounts
                WHERE card_number = %s
                """,
                (card_number.value,)
            )
            row = cursor.fetchone()

        if row is None:
            return None

        return Account(
            account_id=row["id"],
            balance=Balance(row["balance"]),
            number_card=Number_card(row["card_number"]),
            pin_code=Pincode(row["pin"])
        )

    def update(self, account: Account) -> None:
        with self._connection.cursor() as cursor:
            cursor.execute(
                """
                UPDATE accounts
                SET balance = %s
                WHERE card_number = %s
                """,
                (
                    account.balance.amount,
                    account.card_number.value
                )
            )
        self._connection.commit()


"""
CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    card_number VARCHAR(19) UNIQUE NOT NULL,
    pin VARCHAR(10) NOT NULL,
    balance NUMERIC NOT NULL
);
"""