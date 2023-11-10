from Accounts import Account
from Customer_Dict import gen_numbers, gen_pins, gen_amounts, gen_names
import random


def display_menu():
    print("\nBanking System Menu:")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")


class Bank:
    def __init__(self):
        self.accounts = {}

        for x in range(10):
            self.accounts[gen_numbers[x]] = Account(gen_numbers[x], gen_names[x], gen_pins[x], gen_amounts[x])

    def create_account(self, account_number, account_holder, account_pin, balance=0):
        if account_number not in self.accounts:
            account = Account(account_number, account_holder, account_pin, balance)
            self.accounts[account_number] = account
            print(f"Account created for {account_holder} with account number {account_number}.")
        else:
            print("Account number already exists. Please choose a different account number.")

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def run_system(self):
        while True:
            display_menu()
            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                account_number = "".join([str(random.randint(1, 10)) for x in range(10)])
                account_holder = input("Enter Account Name: ")
                while True:
                    account_pin = input("Enter Account 4-Digit Pin: ")
                    if not account_pin.isnumeric():
                        print('Input should be numbers, try again!...')
                    elif not len(account_pin) == 4:
                        print('Input only 4 numbers!...')
                    elif account_pin.isnumeric() and len(account_pin) == 4:
                        self.create_account(account_number, account_holder, account_pin, 0)
                        break

            elif choice == "2":
                account_number = input("Enter account number: ")
                amount = float(input("Enter deposit amount: "))
                account = self.get_account(account_number)
                if account:
                    account.deposit(amount)
                else:
                    print("Account not found!")

            elif choice == "3" or choice == "4":
                attempts = 3
                while attempts > 0:
                    account_number = input("Enter 10-Digit account number: ")
                    account = self.get_account(account_number)
                    if account and choice == '4':
                        print(f"Account balance: ${account.get_balance()}")
                        break
                    elif account and choice == '3':
                        amount = float(input("Enter withdrawal amount: "))
                        account.withdraw(amount)
                        break
                    else:
                        attempts -= 1
                        print(f">>> Account not found!, {attempts} Attempts Left!...")
            elif choice == "5":
                print("Exiting the banking system. Goodbye!")
                break

            elif choice == "9":
                print('All Customers Account Details')
                for key, acct in self.accounts.items():
                    print(f'Account Number: {acct.account_number}, Account Holder: {acct.account_holder},'
                          f' Account Balance: {acct.balance}, Pin: {acct.account_pin}')

            else:
                print("Invalid choice. Please enter a number between 1 and 5.")


# Run the banking system
bank_system = Bank()
bank_system.run_system()
