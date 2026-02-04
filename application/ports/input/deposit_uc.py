from abc import ABC, abstractmethod

class DepositBalanceUC(ABC):

    @abstractmethod
    def execute(self, account, amount: int):
        pass
