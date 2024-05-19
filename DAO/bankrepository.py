from DAO.bankservice import BankServiceProvider
from DAO.customerservice import SavingsAccount, CurrentAccount, ZeroBalance
from Util.dbconn import DBConnection
from tabulate import tabulate
from Entity.customer import Customer


class IBankRepository(BankServiceProvider):

    def createAccount(
        self, name, email, phone_number, address, credit_score, accounttype
    ):
        self.create_account(
            name, email, phone_number, address, credit_score, accounttype
        )

    def ListAccounts(self):
        self.listAccounts()

    def CalculateInterest(self, account_number):
        self.calculate_interest(account_number)

    def getAccountBalance(self, account_number):
        self.get_account_balance(account_number)

    def Deposit(self, account_number, amount):
        self.deposit(account_number, amount)

    def Withdraw(self, account_number, amount):
        account_type = self.type(account_number)
        if account_type == "Savings":
            SavingsAccount.withdraw(account_number, amount)
        elif account_type == "Current":
            CurrentAccount.withdraw(account_number, amount)
        else:
            ZeroBalance.withdraw(account_number, amount)

    def Transfer(self, from_account_number, to_account_number, amount):
        self.transfer(from_account_number, to_account_number, amount)

    def GetAccountDetails(self, account_number):
        self.get_account_details(account_number)

    def GetTransactions(self, account_number, from_date, to_date):
        self.get_transactions(account_number, from_date, to_date)
