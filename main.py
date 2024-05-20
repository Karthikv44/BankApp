from DAO import IBankRepositoryImpl

# Main menu for the Banking Operation

def main():

    bank = IBankRepositoryImpl()

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
            amount = int(input("Enter amount to withdraw: "))
            bank.Withdraw(account_number, amount)
        elif choice == '7':
            from_account_number = int(input("Enter from account number: "))
            to_account_number = int(input("Enter to account number: "))
            amount = int(input("Enter amount to transfer: "))
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
            bank.close()
            break
        else:
            print("Invalid choice. Please try again.")

    
    
if __name__ == "__main__":

    print("Welcome to the Bank")
    main()
    
        