class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance.")

    def get_balance(self):
        return self.balance

# Example of creating a BankAccount object and performing operations
account = BankAccount("123456789", "T Dash", 1000.0)

# Depositing money
account.deposit(500.0)

# Withdrawing money
account.withdraw(200.0)

# Checking balance
print(f"Current balance: {account.get_balance()}")
