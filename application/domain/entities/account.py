from domain.value_objects.balance import Balance
from domain.value_objects.number_card import Number_card
from domain.value_objects.pincode import Pincode

class Account:
    def __init__(self, account_id,  balance: Balance, number_card:Number_card, pin_code:Pincode):
        self.account_id = account_id
        self.balance = balance
        self.number_card = number_card
        self.pin_code = pin_code

    def replenishment(self,amount):
        self.balance += amount

    def withdrawal(self, amount):
        if self.balance < amount:
            raise ValueError("") 
        self.balance -= amount

    def check(self, balance):
        print("Ваш баланс:", balance)