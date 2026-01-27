class GetAccountByCard:
    def __init__(self, account_repository):
        self._repo = account_repository

    def execute(self, card_number):
        return self._repo.get_by_card(card_number)