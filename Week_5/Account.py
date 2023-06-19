class Account:

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return '有多少钱自己心里没点B数？'
        self.balance = self .balance - amount
        return self.balance