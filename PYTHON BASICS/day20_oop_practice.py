# Day 20: OOP Practice
# Real-life example using class and objects

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Account holder:", self.account_holder)
        print("Current balance:", self.balance)

# Creating objects
account1 = BankAccount("Vansh", 5000)
account2 = BankAccount("Aman", 3000)

account1.deposit(1000)
account1.withdraw(2000)
account1.show_balance()

print("-----")

account2.withdraw(4000)
account2.show_balance()
