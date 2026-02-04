class Balance:
    def __init__(self, amount):
        if amount < 0:
            raise ValueError("Сумма баланса для снятия или пополнения не может быть отрицательной")
        self._amount = amount
    
    @property
    def amount(self):
        return self._amount

    def increase(self, amount):
        if amount < 0:
            raise ValueError("Сумма для увеличения не может быть отрицательной")
        self._amount += amount
    def decrease(self, amount):
        if amount < 0:
            raise ValueError("Сумма для уменьшения не может быть отрицательной")
        
        if self._amount < amount:
            raise ValueError("Недостаточно средств на балансе")
        self._amount -= amount

    def __str__(self):
        return f"{self._amount:.2f}"
    