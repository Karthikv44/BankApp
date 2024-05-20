from DAO.bankservice import IBankServiceProviderImpl
from DAO.customerservice import SavingsAccount, CurrentAccount, ZeroBalance
from Util.dbconn import DBConnection
from tabulate import tabulate
from Entity.customer import Customer
from Interface import IBankRepository


class IBankRepositoryImpl(IBankRepository, IBankServiceProviderImpl):
    savings = SavingsAccount()
    current = CurrentAccount()
    zero = ZeroBalance()

    # Method for creating account
    def createAccount(
        self, name, email, phone_number, address, credit_score, accounttype
    ):
        self.create_account(
            name, email, phone_number, address, credit_score, accounttype
        )

    # Method for displaying all accounts
    def ListAccounts(self):
        self.list_Accounts()

    # Method for calculating interest
    def CalculateInterest(self, account_number):
        self.calculate_interest(account_number)

    # Method for getting Account Balance
    def getAccountBalance(self, account_number):
        self.get_account_balance(account_number)

    # Method for deposit amount
    def Deposit(self, account_number, amount):
        self.deposit(account_number, amount)

    # Method for withdraw amount
    def Withdraw(self, account_number, amount):
        account_type = self.type(account_number)
        if account_type == "Savings":
            self.savings.withdraw(account_number, amount)
        elif account_type == "Current":
            self.current.withdraw(account_number, amount)
        else:
            self.zero.withdraw(account_number, amount)

    # Method for transfer amount between accounts
    def Transfer(self, from_account_number, to_account_number, amount):
        self.transfer(from_account_number, to_account_number, amount)

    # Method for getting account details
    def GetAccountDetails(self, account_number):
        self.get_account_details(account_number)

    # Method for getting transactions of account between given interval
    def GetTransactions(self, account_number, from_date, to_date):
        self.get_transactions(account_number, from_date, to_date)
