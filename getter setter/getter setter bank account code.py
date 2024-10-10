
class BankAccount:
    def __init__(self):
        self._balance = 0

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            print("Insufficient balance.")

# Using the class
account = BankAccount()
print(account.get_balance())  # Output: 0

account.deposit(1234567890)
print(account.get_balance())  # Output: 100

account.withdraw(1234567890)
print(account.get_balance())  # Output: 50

account.withdraw(1234567890)  # Output: Insufficient balance.
print(account.get_balance())