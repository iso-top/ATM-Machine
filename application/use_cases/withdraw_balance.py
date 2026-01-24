from application.repositories.account_repository import AccountRepository
from domain.value_objects.balance import Balance
class WithdrawBalance:
    def __init__(self,account_repository):
        self.repo = account_repository

    def execute(self,card_number,amount):
        account = self.repo.get_by_card(card_number)
        account = Balance()
        self.repo.save(account)