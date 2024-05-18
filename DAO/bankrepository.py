from DAO.customerservice import ICustomerServiceProviderImpl
from DAO.bankservice import BankServiceProvider
from Util.dbconn import DBConnection
from tabulate import tabulate
from Entity.customer import Customer


class IBankRepository(ICustomerServiceProviderImpl, BankServiceProvider):
    
    def createAccount(self, name, email, phone_number, address, credit_score, accounttype):
        self.create_account(name, email, phone_number, address, credit_score, accounttype)

    def listAccounts(self):
        self.listAccounts()

    def calculate_interest(self, balance, interest_rate):
        self.calculate_interest(balance, interest_rate)
    def getAccountBalance(self, account_number):
        self.get_account_balance

    def deposit(self, account_number, amount):
        self.deposit(account_number, amount)

    def withdraw(self, account_number, amount):
        self.withdraw(account_number, amount)

    def transfer(self, from_account_number, to_account_number, amount):
        self.transfer(from_account_number, to_account_number, amount)

    def getAccountDetails(self, account_number):
       self.get_account_details(account_number)

    def getTransactions(self, account_number, from_date, to_date):
        self.get_transactions(account_number, from_date, to_date)
