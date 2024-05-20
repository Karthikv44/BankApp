from abc import ABC, abstractmethod

# abstract class for Bank service


class IBankServiceProvider(ABC):
    @abstractmethod
    def create_account(
        self, name, email, phone_number, address, credit_score, accounttype
    ):
        pass

    @abstractmethod
    def list_Accounts(self):
        pass

    @abstractmethod
    def get_Account_Details(self, account_number):
        pass

    @abstractmethod
    def calculate_interest(self, account_number):
        pass
