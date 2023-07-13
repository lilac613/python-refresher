class Bank:
    def __init__(self,balance,name,accountnum):
        self.balance = balance
        self.name = name
        self.accountnum = accountnum
    def withdraw(self,amount):
        '''withdraws money from bank account'''
        if amount > self.balance:
            print("Insufficient funds. Cannot withdraw")
        else:
            self.balance -= amount
    def deposit(self, amount):
        '''deposits money into bank account'''
        self.balance += amount
    def print_balance(self):
        '''prints balance of bank account'''
        print(self.balance)
