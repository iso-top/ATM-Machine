from abc import ABC, abstractmethod
from application.domain.entities.transaction import Transaction
from application.domain.value_objects.number_card import Number_card


class TransactionRepository(ABC):

    @abstractmethod
    def add(self, transaction: Transaction) -> None:
        pass

    @abstractmethod
    def get_for_account(self, account_number: Number_card) -> list[Transaction]:
        pass