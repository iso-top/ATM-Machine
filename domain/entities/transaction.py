class Transaction:
    def __init__(self,amount,account_id,operetion_type,):
        self.amount = amount
        self.account_id = account_id
        self.operetion_type = operetion_type
    def replenishment(self,amount):
        self.balance += amount
    def withdrawal(self, amount):
        if self.balance < amount:
            raise ValueError("") 
        self.balance -= amount

        
#    def history(self, operations):
#        
    def check(self, balance):
        print("Ваш баланс:", balance)