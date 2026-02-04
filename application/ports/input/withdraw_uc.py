from abc import ABC, abstractmethod

class WithdrawBalanceUC(ABC):

    @abstractmethod
    def execute(self, account, amount: int):
        pass