from application.domain.value_objects.password import Password
from application.domain.value_objects.number_card import Number_card
from application.domain.value_objects.pincode import Pincode
from application.domain.value_objects.balance import Balance
from application.domain.entities.transaction import Transaction
from application.repositories.transaction_repository import TransactionRepository

import psycopg

class PostgresTransactionRepository(TransactionRepository):
    def __init__(self,connection):
        self._connection = connection
    def add(self, transaction: Transaction) -> None:
        with self._connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO transactions (account_number, amount, type)
                VALUES (%s, %s, %s)
                """,
                (
                    transaction.account_id,
                    transaction.amount,
                    transaction.type,
                )
            )
        self._connection.commit()
        
    def get_for_account(self, account_number: Number_card) -> list[Transaction]:    
        with self._connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT account_number, amount, type, timestamp
                FROM transactions
                WHERE account_number = %s
                ORDER BY timestamp DESC
                """,
                (account_number.value,)
            )
        rows = cursor.fetchall()

        transactions = []
        for row in rows:
            transactions.append(
                Transaction(
                    account_id=row[0],
                    amount=row[1],
                    type=row[2],
                    timestamp=row[3]
                )
            )
        return transactions