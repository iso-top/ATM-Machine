from application.domain.entities.transaction import Transaction
from application.ports.input.withdraw_uc import WithdrawBalanceUC
class WithdrawBalance(WithdrawBalanceUC):
    def __init__(self, account_repository, transaction_repository):
        self._account_repository = account_repository
        self._transaction_repository = transaction_repository

    def execute(self, account, amount):
        account.withdrawal(amount)

        self._account_repository.update(account)

        transaction = Transaction(
            account_id=account.account_id,
            amount=amount,
            type="withdraw"
        )
        self._transaction_repository.add(transaction)

        return account.balance