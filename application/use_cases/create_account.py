from application.repositories.account_repository import AccountRepository
from application.domain.entities.account import Account
from application.domain.value_objects.number_card import Number_card
from application.domain.value_objects.pincode import Pincode

class CreateAccount:
    def __init__(self, account_repository: AccountRepository):
        self._account_repository = account_repository
    

    #Проверка на существование счета по номеру карты
    def execute(self, card_number: str, pin: str) -> Account:
        card_number_vo = Number_card(card_number)
        pin_vo = Pincode(pin)
    
        if self._account_repository.exists(card_number_vo):
            raise ValueError(f"the card with the number {card_number} already exists")
        
    #создание сущности домейн
        account = Account(card_number = card_number_vo, pin = pin_vo)

        self._account_repository.create(account)

        return account