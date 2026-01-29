from application.domain.entities.transaction import Transaction
from application.repositories.transaction_repository import TransactionRepository

class PostgresTransactionRepository(TransactionRepository):
    def __init__(self, connection):
        self._connection = connection

    def add(self, transaction: Transaction) -> None:
        with self._connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO transactions (account_id, amount, type, created_at)
                VALUES (%s, %s, %s, %s)
                """,
                (
                    transaction.account_id,
                    transaction.amount,
                    transaction.type,
                    transaction.timestamp
                )
            )
        self._connection.commit()

    def get_for_account(self, account_id: int) -> list[Transaction]:
        with self._connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT account_id, amount, type, created_at
                FROM transactions
                WHERE account_id = %s
                ORDER BY created_at DESC
                """,
                (account_id,)
            )
            rows = cursor.fetchall()

        transactions = []
        for row in rows:

            transactions.append(
                Transaction(
                    account_id=row["account_id"],
                    amount=float(row["amount"]),
                    type=row["type"],
                    timestamp=row["created_at"]
                )
            )
        return transactions