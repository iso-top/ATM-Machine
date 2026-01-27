from abc import ABC, abstractmethod

class AccountRepository(ABC):
    @abstractmethod
    def create(self,account):
        pass
    @abstractmethod
    def get_by_card(self, account_number):
        pass

    @abstractmethod
    def update(self, account):
        pass
