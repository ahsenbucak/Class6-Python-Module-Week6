
# You will have class Client inside this file.
# Class Client will have account_number, name, total_amount attributes
# __init__ method will initialize these variables, it will take name and total_amount as parameters 
# and will assign a random 5 digit int to account_number
# Lastly this class will have withdraw, deposit and balance methods.

import random
class Client:
    existing_accounts=[]

    def __init__(self,name,total_amount):
        self.name=name
        self.total_amount=total_amount
        self.create_account()
    def create_account(self):
        self.__account_number=random.randint(10000,99999)
        while self.__account_number in self.existing_accounts:
            self.__account_number=random.randint(10000,99999)
        self.existing_accounts.append(self.__account_number)
    
    def get_account_number(self):
        return self.__account_number

    def withdraw(self,amount):
        if amount> self.total_amount:
            print("Not enough money!")
        else:
            self.total_amount-=amount
            print(f' The sum of {amount} has been withdrawn from your account balance.')
            self.balance()

    def deposit(self,amount):
        self.total_amount+=amount
        print(f'The sum of {amount }has been added to your account')
        self.balance()

    def balance(self):
        print (f'Your current account balance is:{self.total_amount}')
        return self.total_amount



