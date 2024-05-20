from DAO.customerservice import ICustomerServiceProviderImpl
from Util.dbconn import DBConnection
from tabulate import tabulate
from Entity.customer import Customer
from Interface import IBankServiceProvider


class IBankServiceProviderImpl(
    IBankServiceProvider, ICustomerServiceProviderImpl, DBConnection
):
    # Method for creating account
    def create_account(
        self, name, email, phone_number, address, credit_score, accounttype
    ):
        try:
            self.cursor.execute(
                """INSERT INTO Customer (name, email, phone_number, address, credit_score) VALUES 
                    (?,?,?,?,?)
                """,
                (name, email, phone_number, address, credit_score),
            )

            if accounttype == 1:
                self.cursor.execute(
                    """INSERT INTO Account (account_type, balance, customer_id)
                    VALUES
                   ('Savings', 500, (Select max(customer_id) from Customer))
                """,
                )
            elif accounttype == 2:
                self.cursor.execute(
                    """INSERT INTO Account (account_type, balance, customer_id)
                    VALUES
                   ('Current', 500, (Select max(customer_id) from Customer))
                """,
                )
            elif accounttype == 3:
                self.cursor.execute(
                    """INSERT INTO Account (account_type, balance, customer_id)
                    VALUES
                   ('ZeroBalance', 500, (Select max(customer_id) from Customer))
                """,
                )
            self.conn.commit()
            print("Successfully Created !!!")
        except Exception as e:
            print(e)

    # Method for displaying all accounts
    def list_Accounts(self):
        try:
            self.cursor.execute("Select * from account")
            details = self.cursor.fetchall()
            headers = [column[0] for column in self.cursor.description]
            print(tabulate(details, headers=headers, tablefmt="psql"))
        except Exception as e:
            print(e)

    # Method for getting account details
    def get_Account_Details(self, account_number):
        self.get_account_details(account_number)

    # Method for calculating interest
    def calculate_interest(self, account_number):
        try:
            type_account = self.type(account_number)
            if type_account == "Savings":
                interest_rate = 0.08
                balance = self.account_balance(account_number)
                interest = float(balance) * interest_rate
                print(f"Your interest is {interest}")
            else:
                print("It is not a savings account")
        except Exception as e:
            print(e)
