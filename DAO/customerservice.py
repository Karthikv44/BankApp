from abc import ABC, abstractmethod
from Util.dbconn import DBConnection
from tabulate import tabulate
from Entity.customer import Customer
from Exception import InsufficientFundException,InvalidAccountException,OverDraftLimitExceededException


class ICustomerServiceProvider(ABC):
    @abstractmethod
    def get_account_balance(self, account_number):
        pass

    @abstractmethod
    def deposit(self, account_number, amount):
        pass

    @abstractmethod
    def withdraw(self, account_number, amount):
        pass

    @abstractmethod
    def transfer(self, from_account_number, to_account_number, amount):
        pass

    @abstractmethod
    def get_account_details(self, account_number):
        pass

    @abstractmethod
    def get_transactions(self, account_number, from_date, to_date):
        pass


class ICustomerServiceProviderImpl(DBConnection):

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

    def get_account_balance(self, account_number):
        try:
            self.cursor.execute(
                "select balance from account where account_number = (?)",
                (account_number),
            )
            row = self.cursor.fetchone()
            print(f"Balance is {row[0]}")
            return row[0]
        except Exception as e:
            print(e)

    def deposit(self, account_number, amount):
        new_balance = self.account_balance(account_number) + amount
        try:
            self.cursor.execute(
                "UPDATE account SET balance = (?) WHERE account_number = (?);",
                (new_balance, account_number),
            )
            self.get_account_balance(account_number)
            self.conn.commit()
        except Exception as e:
            print(e)

    def withdraw(self, account_number, amount):
        try:
            balance = self.account_balance(account_number)
            type = self.type(account_number)
            if type == "Savings":
                if balance > amount and amount > 500:
                    self.cursor.execute(
                        """
                    UPDATE account SET balance = (?) WHERE account_number = (?);
                    """,
                        (balance - amount, account_number),
                    )
                    self.conn.commit()
                else:
                    raise InsufficientFundException
            elif type == "Current":
                overdraftlimit = -1000
                if (balance - amount) > overdraftlimit:
                    self.cursor.execute(
                        """
                    UPDATE account SET balance = (?) WHERE account_number = (?);
                     """,
                        (balance - amount, account_number),
                    )
                    self.conn.commit()
                else:
                    print("Overdraft Limit Exceeded")
        except Exception as e:
            print(e)

    def transfer(self, from_account_number, to_account_number, amount):
        try:
            self.cursor.execute(
                "UPDATE Account SET Balance = Balance - ? WHERE account_number = ?",
                (amount, from_account_number),
            )

            # Add amount to the receiver's account
            self.cursor.execute(
                "UPDATE Account SET Balance = Balance + ? WHERE account_number = ?",
                (amount, to_account_number),
            )

            self.conn.commit()

            print("Transaction Successful")
        except Exception as e:
            print(e)

    def get_account_details(self, account_number):
        try:
            self.cursor.execute(
                "Select * from account WHERE account_number = ?", (account_number)
            )
            details = self.cursor.fetchall()
            headers = [column[0] for column in self.cursor.description]
            print(tabulate(details, headers=headers, tablefmt="psql"))
        except Exception as e:
            print(e)

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
    def withdraw(self, account_number, amount):
        try:
            balance = self.account_balance(account_number)
            if balance > amount and amount > 500:
                self.cursor.execute(
                    """
                UPDATE account SET balance = (?) WHERE account_number = (?);
                """,
                    (balance - amount, account_number),
                )
                print("Successful withrawal")
                self.conn.commit()
            else:
                raise InsufficientFundException
        except Exception as e:
            print(e)


class CurrentAccount(ICustomerServiceProviderImpl):

    def withdraw(self, account_number, amount):
        try:
            balance = self.account_balance(account_number)
            overdraftlimit = -1000
            if (balance - amount) > overdraftlimit:
                self.cursor.execute(
                    """
                UPDATE account SET balance = (?) WHERE account_number = (?);
                    """,
                    (balance - amount, account_number),
                )
                self.conn.commit()
            else:
                raise OverDraftLimitExceededException
        except Exception as e:
            print(e)

class ZeroBalance(ICustomerServiceProviderImpl):            
    def withdraw(self, account_number, amount):
        try:
            balance = self.account_balance(account_number)
            if amount > 0:
                self.cursor.execute(
                    """
                UPDATE account SET balance = (?) WHERE account_number = (?);
                """,
                    (balance - amount, account_number),
                )
                print("Successful withrawal")
                self.conn.commit()
            else:
                raise InsufficientFundException
        except Exception as e:
            print(e)