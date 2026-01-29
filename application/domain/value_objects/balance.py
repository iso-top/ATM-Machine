class Balance:
    def __init__(self, amount):
        if amount < 0:
            raise ValueError("Money cannot be negative")
        self._amount = amount
    
    @property
    def amount(self):
        return self._amount

    def __str__(self):
        return f"{self._amount:.2f}"