from random import randint

class BankAccount:
    def __init__(self, full_name):
        self.full_name = full_name
        self.account_number = randint(1000000, 9999999)
        self.routing_number = 123456789
        self.balance = 0.00
        self.display_number = ""

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit Amount: ${amount}")
        print(f"Updated Balance: ${self.balance}")
        

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawl Amount: ${amount}")
            print(f"Updated Balance: ${self.balance}")
        else:
            print(f"Insufficient Funds: ${self.balance}. You will be penalized $10")
            self.balance -= amount + 10
            print(f"New Balance: ${self.balance}")

    def get_balance(self):
        print(f"Current Account Balance: ${self.balance}")
        return self.balance

    def add_interest(self):
        interest = self.balance * 0.00083 
        self.balance += interest
        return interest
    
    def display_num(self):
        acct_num = range(len(str(self.account_number)))
            
        for i in acct_num:
            if i <= 4:
                self.display_number += "*"
            else:
                self.display_number += str(self.account_number)[i]

    def print_statement(self):
        print(f"Hello {self.full_name}! Your balance for account '{self.account_number}' is: ${self.balance}. Don't forget our Routing Number: {self.routing_number}, in order to deposit or withdraw funds in the future.")
    


ryan = BankAccount("Ryan Cornel")
ryan.account_number
print(ryan.account_number)
ryan.routing_number
ryan.get_balance()
ryan.deposit(1000)
ryan.withdraw(150)
print(ryan.get_balance)
ryan.add_interest
print(ryan.get_balance)
print(ryan.print_statement())
