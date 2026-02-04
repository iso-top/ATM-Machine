from application.domain.entities.transaction import Transaction
from application.ports.input.deposit_uc import DepositBalanceUC 

class DepositBalance(DepositBalanceUC):
    def __init__(self, account_repository, transaction_repository):
        self._account_repository = account_repository
        self._transaction_repository = transaction_repository

    def execute(self, account, amount):
        account.deposit_balance(amount)
        self._account_repository.update(account)

        transaction = Transaction(
            account_id=account.account_id,
            amount=amount,
            type="deposit"
        )
        self._transaction_repository.add(transaction)