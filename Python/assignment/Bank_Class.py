
class BankAccount:

    # Class variable
    total_accounts = 0

    # __init__ method
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

        BankAccount.total_accounts += 1

    # Instance methods
    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print("Money deposited successfully.")
        else:
            print("Invalid deposit amount.")

    
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Not enough balance.")
        else:
            self.balance = self.balance - amount
            print("Money withdrawn successfully.")

    
    def check_balance(self):
        print("Balance:", self.balance)

    
    def display_details(self):
        print("Name:", self.name)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

    # Class method
    @classmethod
    def show_total_accounts(cls):
        print("Total accounts:", cls.total_accounts)

 
# objects creation
account1 = BankAccount("AK", "A001", 5000)
account2 = BankAccount("PR", "A002", 8000)
account3 = BankAccount("PK", "A003", 10000)

#Initial Account Details
account1.display_details()
print()
account2.display_details()
print()
account3.display_details()
print()

#Bank transcations
print("Banking Operations on Account 1: \n")
account1.deposit(2000)
account1.withdraw(1000)
account1.check_balance()
print()

print("Banking Operations on Account 2: \n")
account2.deposit(1000)
account2.withdraw(500)
account2.check_balance()
print()

print("Banking Operations on Account 3: \n")
account3.deposit(500)
account3.withdraw(2000)
account3.check_balance()

# Account Data shown after transactions
print("Account 1 balance:", account1.balance)
print("Account 2 balance:", account2.balance)
print("Account 3 balance:", account3.balance)
print()

BankAccount.show_total_accounts()
print()

# Error cases
account1.deposit(0)
print()
account2.withdraw(-200)
print()
account3.withdraw(50000)
print()

