from domain.entities.account import Account
from domain.value_objects.number_card import Number_card
from domain.value_objects.pincode import Pincode

class GetTransactionHistory:
    def __init__(self, account_repository):
        self._account_repository = account_repository

    def execute(self, card_number: str):
        #получаем карту через 
        card_number_vo = Number_card(card_number)
        account = self._account_repository.get_by_card(card_number)

        #проверка на наличие 
        if account is None:
            raise ValueError("Account not found")

        return account.transactions