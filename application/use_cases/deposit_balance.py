from application.domain.entities.transaction import Transaction
class DepositBalance:
    def __init__(self, account_repository, transaction_repository):
        self._account_repository = account_repository
        self._transaction_repository = transaction_repository

    def execute(self, account, amount):
        # 1. Используем существующую доменную логику
        account.deposit_balance(amount)

        # 2. Сохраняем аккаунт
        self._account_repository.update(account)

        # 3. Пишем транзакцию
        transaction = Transaction(
            account_id=account.account_id,
            amount=amount,
            type="deposit"
        )
        self._transaction_repository.add(transaction)