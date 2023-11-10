class Account:
    def __init__(self, account_number, account_holder, account_pin, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.account_pin = account_pin
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        pin_attempts = 3
        while pin_attempts > 0:
            pin = input("Enter your withdrawal pin: ")
            if pin == self.account_pin:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Withdrew ${amount}. New balance: ${self.balance}")
                    break
                else:
                    print("Insufficient funds!")
                    break
            else:
                pin_attempts -= 1
                print(f'Invalid pin, try again!...{pin_attempts} Attempts Left!')

    def get_balance(self):
        return self.balance