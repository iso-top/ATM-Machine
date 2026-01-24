class DepositBalance:
    def __init__ (self,account_repository):
        self._account_repository = account_repository

    def execute(self,card_number, amount):
        account = self.repo.get_by_card(card_number)
        account.deposit_balance(amount)
        self._account_repository.save(account)
        return account.balance
