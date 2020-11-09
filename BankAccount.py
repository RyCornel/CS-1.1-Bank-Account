class BankAccount:
    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = str
        self.account_number = int
        self.routing_number = int
        self.balance = int 

    def print_statement(self):
        print(f"Hello {self.full_name}! Your balance for account {self.account_number} is: {self.balance}. Don't forget our Routing Number: {self.routing_number}, in order to deposit or withdraw funds in the future.")

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        print("Amount Withdrawn: ${amount}")
        return self.balance

    def get_balance(self, balance):
        print(self.balance)
        return self.balance
