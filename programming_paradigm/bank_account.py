class BankAccount:
    def __init__(self, balance=0 ):
        self.balance = balance

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
    return f"Current balance: {self.balance:.2f}" if self.balance >= 0 else "Balance is negative"