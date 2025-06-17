import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)#Example starting balance
    if len(sys.argv) > 2:
        print("Usage: python main-o.py <command>: <amount>")
        print("commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else 0

    if command == "deposit"and amount is not None:
         account.deposit(amount)
         print(f"Deposited{amount}.New balance: {account .display_balance()}")
    elif command =="withdraw" and amount is not None:
        if account.withdraw(amount)
            print(f"Withdrew{amount}")     
        else:
            print("insufficient funds")
    elif command =="display":
        print(f"Current balance: {account.display_balance()}")        


