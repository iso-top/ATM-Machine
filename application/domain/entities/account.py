from domain.value_objects.balance import Balance
from domain.value_objects.number_card import Number_card
from domain.value_objects.pincode import Pincode

class Account:
    def __init__(self, account_id,  balance: Balance, number_card:Number_card, pin_code:Pincode):
        self.account_id = account_id
        self.balance = Balance(0) #задается начальный баланс 0
        self.number_card = number_card
        self.pin_code = pin_code

    #пополнение счета
    def deposit_balance(self,amount: float):
        deposit += Balance(amount)
        self.balance = Balance(self.balance.amount + deposit.amount)
    #снятие с счета
    def withdrawal(self, amount):
        if self.balance < amount:
            raise ValueError("") 
        self.balance -= amount

    def check(self, balance):
        print("Ваш баланс:", balance)