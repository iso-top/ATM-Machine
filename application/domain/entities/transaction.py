from datetime import datetime

class Transaction:
    def __init__(
        self,
        account_id: int,
        amount: float,
        type: str,
        timestamp: datetime | None = None
    ):
        self.account_id = account_id
        self.amount = amount
        self.type = type  # "deposit" | "withdraw"
        self.timestamp = timestamp or datetime.utcnow()
