from abc import ABC, abstractmethod

class AccountRepository(ABC):

    @abstractmethod
    def create(self,account):
        pass
    @abstractmethod
    def get_by_number(self, account_number):
        pass

    @abstractmethod
    def save(self, account):
        pass