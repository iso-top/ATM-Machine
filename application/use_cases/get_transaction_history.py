from application.repositories.transaction_repository import TransactionRepository

class GetTransactionHistory:
    def __init__(self, transaction_repository: TransactionRepository):
        self._transaction_repository = transaction_repository

    def execute(self, account_id: int):
        transactions = self._transaction_repository.get_for_account(account_id)
        return transactions if transactions else []
