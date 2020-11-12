from random import random

class BankAccount:
    def __init__(self, full_name):
        self.full_name = full_name
        self.account_number = random(1000000, 9999999)
        self.routing_number = int
        self.balance = 0.00

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit Amount: ${amount}")
        print(f"Updated Balance: ${self.balance}")
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawl Amount: ${amount}")
            print(f"Updated Balance: ${self.balance}")
        else:
            print(f"Insufficient Funds: ${self.balance}")
            self.balance -= + 10
            print(f"New Balance: ${self.balance}")

    def get_balance(self):
        print(f"Current Account Balance: $self.balance")
        return self.balance

    def add_interest(self):
        interest = self.balance * 0.00083 
        self.balance += interest
    
    def display_num(self):
        acct_num = range(len(str(self.account_number)))
            
        for i in acct_num:
            if i <= 4:
                self.display_num += "*"
            else:
                self.display_num += str(self.account_number)[i]

    def print_statement(self):
        print(f"Hello {self.full_name}! Your balance for account {self.account_number} is: {self.balance}. Don't forget our Routing Number: {self.routing_number}, in order to deposit or withdraw funds in the future.")
    

ryan = BankAccount("Ryan Cornel")