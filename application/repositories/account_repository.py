from abc import ABC, abstractmethod

class AccountRepository(ABC):

    @abstractmethod
    def exists(self,card_number):
        #проверяет есть ли такой аккаунт
        pass
    @abstractmethod
    def create(self,account):
        pass
    @abstractmethod
    def get_by_number(self, account_number):
        pass

    @abstractmethod
    def update(self, account):
        pass
