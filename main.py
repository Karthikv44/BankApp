from DAO import ICustomerServiceProviderImpl
from DAO import BankServiceProvider
from DAO import IBankRepository
# class Customer:
#     def __init__(
#         self, customer_id, first_name, last_name, email, phone_number, address
#     ):
#         self.customer_id = customer_id
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.phone_number = phone_number
#         self.address = address


# class Account:

#     interest_rate = 0.045

#     def __init__(self, account_number, account_type, account_balance):
#         self.account_number = account_number
#         self.account_type = account_type
#         self.account_balance = account_balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.account_balance += amount
#             print("Deposit of", amount, "successful.")
#         else:
#             print("Invalid deposit amount.")

#     def withdraw(self, amount):
#         if amount > 0:
#             if amount <= self.account_balance:
#                 self.account_balance -= amount
#                 print("Withdrawal of", amount, "successful.")
#             else:
#                 print("Insufficient balance.")
#         else:
#             print("Invalid withdrawal amount.")

#     def calculate_interest(self):
#         interest_amount = self.account_balance * self.interest_rate
#         return interest_amount

#     def display(self):
#         print(self.account_balance)


# class Bank:

#     def create_account(self, account_number, account_type, account_balance):
#         return Account(account_number, account_type, account_balance)


# class SavingsAccount(Account):

#     def __init__(self, account_number, account_balance, interest_rate):
#         super().__init__(account_number, account_balance)
#         self.interest_rate = interest_rate

#     def calculate_interest(self):
#         interest_amount = self.account_balance * self.interest_rate
#         self.account_balance += interest_amount
#         print("Interest added to account balance: ", interest_amount)


# class CurrentAccount(Account):
#     OVERDRAFT_LIMIT = 1000  # Configure overdraft limit as a constant

#     def withdraw(self, amount):
#         if amount > 0:
#             if self.account_balance - amount >= self.OVERDRAFT_LIMIT:
#                 self.account_balance -= amount
#                 print(f"Withdrawal of {amount}successful.")
#             else:
#                 print("Withdrawal amount exceeds overdraft limit.")
#         else:
#             print("Invalid withdrawal amount.")


if __name__ == "__main__":

    bank = IBankRepository()

    print("Welcome to the Bank")
    while True:
        print("""
        Banking System Main Menu
        1. Create Account
        2. List Accounts
        3. Calculate Interest
        4. Get Account Balance
        5. Deposit
        6. Withdraw
        7. Transfer
        8. Get Account Details
        9. Get Transactions
        0. Exit
        """)
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter Customer Name: ")
            email = input("Enter Customer Email: ")
            phone_number = input("Enter Customer Phone Number: ")
            address = input("Enter Customer Address: ")
            credit_score = int(input("Enter Customer Credit Score: "))
            accounttype = int(
                input("1 for Savings / 2 for Current / 3 for Zero balance")
            )
            bank.create_account(
                name, email, phone_number, address, credit_score, accounttype
            )
        elif choice == '2':
            bank.ListAccounts()
        elif choice == '3':
            account_number = int(input("Enter the account_number "))
            bank.calculate_interest(account_number)
        elif choice == '4':
            account_number = int(input("Enter the account_number "))
            bank.get_account_balance(account_number)
        elif choice == '5':
            account_number = int(input("Enter the account_number "))
            amount = int(input("Enter the amount "))
            bank.Deposit(account_number, amount)
        elif choice == '6':
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter amount to withdraw: "))
            bank.Withdraw(account_number, amount)
        elif choice == '7':
            from_account_number = int(input("Enter from account number: "))
            to_account_number = int(input("Enter to account number: "))
            amount = float(input("Enter amount to transfer: "))
            bank.Transfer(from_account_number, to_account_number, amount)
        elif choice == '8':
            account_number = int(input("Enter account number: "))
            bank.GetAccountDetails(account_number)
        elif choice == '9':
            account_number = int(input("Enter account number: "))
            from_date = input("Enter from date (YYYY-MM-DD): ")
            to_date = input("Enter to date (YYYY-MM-DD): ")
            bank.GetTransactions(account_number, from_date, to_date)
        elif choice == '0':
            print("Thank you for visiting our bank")
            break
        else:
            print("Invalid choice. Please try again.")
        # if choice == 1:
        #     account_number = int(input("Enter the account_number "))
        #     ban.get_account_balance(account_number)
        # #     account_type = input("Enter the account_type ")
        # #     account_balance = int(input("Enter the account_balance "))
        # #     bank.create_account(account_number, account_type, account_balance)
        # elif choice == 2:
        #     account_number = int(input("Enter the account_number "))
        #     amount = int(input("Enter the amount "))
        #     ban.deposit(account_number, amount)
        # elif choice == 3:
        #     amount = int(input("Enter the amount "))
        #     account_number1 = int(input("Enter the account_number "))
        #     account_number2 = int(input("Enter the account_number "))
        #     ban.transfer( account_number1, account_number2, amount)
        # elif choice == 4:
        #     account_number = int(input("Enter the account_number "))
        #     ban.get_account_details(account_number)
        # elif choice == 5:
        #     ban.listAccounts()
        # elif choice == 6:
        #     name = input("Enter Customer Name: ")
        #     email = input("Enter Customer Email: ")
        #     phone_number = input("Enter Customer Phone Number: ")
        #     address = input("Enter Customer Address: ")
        #     credit_score = int(input("Enter Customer Credit Score: "))
        #     accounttype = int(
        #         input("1 for Savings / 2 for Current / 3 for Zero balance")
        #     )
        #     ban.create_account(
        #         name, email, phone_number, address, credit_score, accounttype
        #     )

        # elif choice == 7:
        #     account_number = int(input("Enter the account_number "))
        #     ban.getAccountDetails(account_number)
        # elif choice == 8:
        #     account_number = int(input("Enter the account_number "))
        #     ban.calculate_interest(account_number)    
        # elif choice == 9:
        #     account_number = int(input("Enter the account_number "))
        #     amount = int(input("Enter the amount0 "))
        #     ban.withdraw(account_number, amount)    
