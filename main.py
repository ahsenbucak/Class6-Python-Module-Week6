# This class initially will create a bank object with a name you choose and then will print the 
# following menu (it should print this menu, until user says exit) [hint: use while loop]:
# Welcome to ING!

# Choose an option:

#     1. Open new bank account
#     2. Open existing bank account
#     3. Exit
from bank import Bank
from client import Client

bank=Bank('ING')

while True:
    print(f'''
Welcome to {bank.name}!    
Choose an option:
       1-Open new bank account
       2-Open existing bank account
       3=Exit
    ''')
    user_input=int(input())

    if user_input==1:
        print('To create an account,please fill in the information below')
        client_name=input('Name:')
        deposit_amount=int(input('Deposit Amount:'))
        client=Client(client_name,deposit_amount)
        bank.add_client(client)
    elif user_input==2:
        print('To access your account,please enter your credentials below.')
        client_name=input('Name:')
        account_number=int(input('Account Number:'))
        client=bank.authentication(client_name,account_number)
        if client:
            valid=True
            while valid:
                print('''
Choose an option:
        1-Withdraw
        2-Deposit
        3-Balance
        4-Exit

                ''')
                choice=int(input(''))
                if choice==1:
                    withdraw_amount=int(input('Withdraw amount:'))
                    client.withdraw(withdraw_amount)
                elif choice==2:
                    deposit_amount=int(input('Deposit amount:'))
                    client.deposit(deposit_amount)
                elif choice==3:
                    client.balance()
                elif choice==4:
                    valid=False
                else:
                    print('Please enter a valid input (1,2,3 or 4)')
        elif user_input==3:
            break
        else:
            print('Please enter a valid input(1,2 or  3)')

