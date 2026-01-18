from abc import ABC, abstractmethod

class TransactionRepository(ABC):

    @abstractmethod
    def add(self,account):
        pass
    @abstractmethod
    def get_for_account(self, account_number):
        pass
