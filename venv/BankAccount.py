class BankAccount:

    bank_accounts = {}

    def __init__(self, number, balance=0):
        self.number = number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f'Deposited {amount} PLN. New balance: {self.balance} PLN'
        else:
            return 'Invalid amount'

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return f'Withdrawn {amount} PLN. New balance: {self.balance} PLN'
        else:
            return 'Invalid amount or insufficient funds'

    def get_balance(self):
        return self.balance

    def transfer(self, target_account, amount):
        if self is not None and amount > 0 and self.balance >= amount and target_account is not None:
            self.balance -= amount
            target_account.balance += amount
            return f'Transferred {amount} PLN to account {target_account.number}. New balance: {self.balance} PLN'
        else:
            return 'Transfer failed. Check if both accounts exist and have sufficient funds.'



