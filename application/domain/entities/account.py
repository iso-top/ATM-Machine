from ..value_objects.balance import Balance
from ..value_objects.number_card import Number_card
from ..value_objects.pincode import Pincode

class Account:
    def __init__(self, account_id: int, balance: Balance, number_card: Number_card, pin_code: Pincode):
        self.account_id = account_id
        self.balance = balance  # используем переданный баланс
        self.number_card = number_card
        self.pin_code = pin_code

    # Пополнение счета
    def deposit_balance(self, amount: float):
        self.balance = Balance(self.balance.amount + amount)

    # Снятие со счета
    def withdrawal(self, amount: float):
        if self.balance.amount < amount:
            raise ValueError("Недостаточно средств на счете")
        self.balance = Balance(self.balance.amount - amount)

    # Проверка баланса
    def check_balance(self):
        print("Ваш баланс:", self.balance.amount)
