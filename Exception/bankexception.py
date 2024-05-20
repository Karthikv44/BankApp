class InsufficientFundException(Exception):
    def __init__(self):
        super().__init__(f"Insufficient funds in your account")

class InvalidAccountException(Exception):
    def __init__(self):
        super().__init__(f"Account does not exist")

class OverDraftLimitExceededException(Exception):
    def __init__(self):
        super().__init__("Overdraft limit exceeded.")