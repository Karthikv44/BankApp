from abc import ABC, abstractmethod
from Util.dbconn import DBConnection
from tabulate import tabulate
from Entity.customer import Customer
from Exception import InsufficientFundException,InvalidAccountException,OverDraftLimitExceededException
from Interface import ICustomerServiceProvider

class ICustomerServiceProviderImpl(ICustomerServiceProvider, DBConnection):
    
    # Method for identifying type of account

    def type(self, account_number):
        try:
            self.cursor.execute(
                "select account_type from account where account_number = (?)",
                (account_number),
            )
            row = self.cursor.fetchone()
            return row[0]
        except Exception as e:
            print(e)

    # Method for getting account balance
    def account_balance(self, account_number):
        try:
            self.cursor.execute(
                "select balance from account where account_number = (?)",
                (account_number),
            )
            row = self.cursor.fetchone()
            return row[0]
        except Exception as e:
            print(e)

    # Method for getting account balance and printing
    def get_account_balance(self, account_number):
        try:
            self.cursor.execute(
                "select balance from account where account_number = (?)",
                (account_number),
            )
            row = self.cursor.fetchone()
            if row is None: 
                raise InvalidAccountException
            else:
                print(f"Balance is {row[0]}")
                
        except Exception as e:
            print(e)

    # Method for deposit amount
    def deposit(self, account_number, amount):
        new_balance = self.account_balance(account_number) + amount
        try:
            self.cursor.execute(
                "UPDATE account SET balance = (?) WHERE account_number = (?);",
                (new_balance, account_number),
            )
            self.cursor.execute(
                '''DECLARE @CurrentDate DATE;
                SET @CurrentDate = FORMAT(GETDATE(), 'yyyy-MM-dd');
                INSERT INTO Transactions 
                (account_number, description, date, transaction_type, transaction_amount) VALUES
                (?, 'Deposit Successful', @CurrentDate, 'Deposit', ?)''',
                (account_number, amount),
                )
            self.get_account_balance(account_number)
            self.conn.commit()
        except Exception as e:
            print(e)
    # Method for withdraw amount
    def withdraw(self, account_number, amount):
        pass

    # Method for transfer amount        
    def transfer(self, from_account_number, to_account_number, amount):
        try:
            self.cursor.execute(
                "UPDATE Account SET Balance = Balance - ? WHERE account_number = ?",
                (amount, from_account_number),)
            
            self.cursor.execute(
                "UPDATE Account SET Balance = Balance + ? WHERE account_number = ?",
                (amount, to_account_number),
            )
            self.cursor.execute(
                '''DECLARE @CurrentDate DATE;
                SET @CurrentDate = FORMAT(GETDATE(), 'yyyy-MM-dd');
                INSERT INTO Transactions 
                (account_number, description, date, transaction_type, transaction_amount) VALUES
                (?, 'Transfer sent', @CurrentDate, 'Transfer', ?)''',
                (from_account_number, amount),
            )
            self.cursor.execute(
                '''DECLARE @CurrentDate DATE;
                SET @CurrentDate = FORMAT(GETDATE(), 'yyyy-MM-dd');
                INSERT INTO Transactions 
                (account_number, description, date, transaction_type, transaction_amount) VALUES
                (?, 'Transfer received', @CurrentDate, 'Transfer', ?)''',
                (to_account_number, amount),
            )

            self.conn.commit()

            print("Transaction Successful")
        except Exception as e:
            print(e)

    # Method for getting account details
    def get_account_details(self, account_number):
        try:
            self.cursor.execute(
                "Select * from account WHERE account_number = ?", (account_number)
            )
            details = self.cursor.fetchall()
            headers = [column[0] for column in self.cursor.description]
            print(tabulate(details, headers=headers, tablefmt="psql"))
        except InvalidAccountException as e:
            print(e)

    # Method for getting transactions of account between given interval
    def get_transactions(self, account_number, from_date, to_date):
        try:
            self.cursor.execute(
                """SELECT date, Description, transaction_amount FROM Transactions 
                                WHERE account_number = ? AND date >= ? AND date <= ? 
                                order by date""",
                (account_number, from_date, to_date),
            )
            details = self.cursor.fetchall()
            headers = [column[0] for column in self.cursor.description]
            print(tabulate(details, headers=headers, tablefmt="psql"))
        except Exception as e:
            print(e)


class SavingsAccount(ICustomerServiceProviderImpl):

    # Polymorphism
    # Method for withdraw amount of savings account type
    def withdraw(self, account_number, amount):
        try:
            balance = self.account_balance(account_number)
            if balance > amount and balance - amount > 500:
                self.cursor.execute(
                    """
                UPDATE account SET balance = (?) WHERE account_number = (?);
                """,
                    (balance - amount, account_number),
                )
                self.cursor.execute(
                '''DECLARE @CurrentDate DATE;
                SET @CurrentDate = FORMAT(GETDATE(), 'yyyy-MM-dd');
                INSERT INTO Transactions 
                (account_number, description, date, transaction_type, transaction_amount) VALUES
                (?, 'Withdraw Successful', @CurrentDate, 'Withdraw', ?)''',
                (account_number, amount),
                )
                current_balance = self.account_balance(account_number)
                print("Successful withdrawal")
                print(f"Your account balance is {current_balance}")
                self.conn.commit()
            else:
                raise InsufficientFundException
        except Exception as e:
            print(e)


class CurrentAccount(ICustomerServiceProviderImpl):

    # Polymorphism
    # Method for withdraw amount of current account type
    def withdraw(self, account_number, amount):
        try:
            balance = self.account_balance(account_number)
            overdraftlimit = -1000
            if (balance - amount) > overdraftlimit is not None:
                self.cursor.execute(
                    """
                UPDATE account SET balance = (?) WHERE account_number = (?);
                    """,
                    (balance - amount, account_number),
                )
                self.cursor.execute(
                '''DECLARE @CurrentDate DATE;
                SET @CurrentDate = FORMAT(GETDATE(), 'yyyy-MM-dd');
                INSERT INTO Transactions 
                (account_number, description, date, transaction_type, transaction_amount) VALUES
                (?, 'Withdraw Successful', @CurrentDate, 'Withdraw', ?)''',
                (account_number, amount),
                )
                current_balance = self.account_balance(account_number)
                print("Successful withdrawal")
                print(f"Your account balance is {current_balance}")
                self.conn.commit()
            else:
                raise OverDraftLimitExceededException
        except Exception as e:
            print(e)

class ZeroBalance(ICustomerServiceProviderImpl):

    # Polymorphism
    # Method for withdraw amount of Zero Balance account type            
    def withdraw(self, account_number, amount):
        try:
            balance = self.account_balance(account_number)
            if amount > 0 and balance - amount > 0:
                self.cursor.execute(
                    """
                UPDATE account SET balance = (?) WHERE account_number = (?);
                """,
                    (balance - amount, account_number),
                )
                self.cursor.execute(
                '''DECLARE @CurrentDate DATE;
                SET @CurrentDate = FORMAT(GETDATE(), 'yyyy-MM-dd');
                INSERT INTO Transactions 
                (account_number, description, date, transaction_type, transaction_amount) VALUES
                (?, 'Withdraw Successful', @CurrentDate, 'Withdraw', ?)''',
                (account_number, amount),
                )
                current_balance = self.account_balance(account_number)
                print("Successful withdrawal")
                print(f"Your account balance is {current_balance}")
                self.conn.commit()
            else:
                raise InsufficientFundException
        except Exception as e:
            print(e)