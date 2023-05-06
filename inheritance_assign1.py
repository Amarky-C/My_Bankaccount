#Create a method that will add, debit a user and delete a function
#Parent class = BankAccount
#create a bank account 
#add user with  initial balance 
#debit from the balance
#delete account

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def add(self, amount):
        self.balance += amount
    def debit(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Insufficient funds')
    def delete(self):
        self.balance = 0
        print('account deleted')


account = BankAccount(1000)
account.add(500)
print(account.balance)

account.debit(200)
print(account.balance)

account.delete()
print(account.balance)
