class BankAccount():
    def __init__(self, balance=0 ):
        self.balance = 0;

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False
    def display_balance(self):
        return self.balance
    def __str__(self):
        return f"BankAccount(balance = {self.balance})"        