from abc import ABC, abstractmethod

class GetHistoryUC(ABC):

    @abstractmethod
    def execute(self, account):
        pass