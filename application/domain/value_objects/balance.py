class Balance:
    def __init__(self,amount):
        if amount <0:
            raise ValueError("Money cannot be negative")
        self._amount = amount
    
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self,value):
        if value < 0:
            raise ValueError("Money cannot be negative")
        self._amount = value
