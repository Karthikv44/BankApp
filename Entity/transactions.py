class Transaction:
    def __init__(self, account, description, date, transaction_type, transaction_amount):
        self.account = account
        self.description = description
        self.date = date
        self.transaction_type = transaction_type
        self.transaction_amount = transaction_amount