from abc import ABC, abstractmethod

# abstract class for Bank repository service

class IBankRepository(ABC):

    @abstractmethod
    def createAccount(self, name, email, phone_number, address, credit_score, accounttype):
        pass

    @abstractmethod
    def ListAccounts(self):
        pass

    @abstractmethod
    def CalculateInterest(self, account_number):
        pass

    @abstractmethod
    def getAccountBalance(self, account_number):
        pass

    @abstractmethod
    def Deposit(self, account_number, amount):
        pass

    @abstractmethod
    def Withdraw(self, account_number, amount):
        pass

    @abstractmethod
    def Transfer(self, from_account_number, to_account_number, amount):
        pass

    @abstractmethod
    def GetAccountDetails(self, account_number):
        pass

    @abstractmethod
    def GetTransactions(self, account_number, from_date, to_date):
        pass
