# You will have class Bank. This bank will have instance variable name and class variable clients list.
#  Initially this list will be empty.
# This class will have method add_client method which appends the client object to the list
# And lastly this class will have authentication method which takes name and account_number as 
# parameters and authenticates the client

class Bank:
    clients=[]

    def __init__(self,name):
        self.name=name
    
    def add_client(self,client):
        # self.client=client
        # Bank.clientlist.append(self.client)
        self.clients.append(client)
        print(f'''
Account created succesfully!Your Account number is :{client.get_account_number()}        
        ''')

    def authentication(self,name,account_number):
        
        for client in self.clients:
            if client.name==name and client.get_account_number()==account_number:
                print('''
Authentication succesfull!                
                ''')
                return client
        print('''
Authentication failed!
Reason:Account not found.        
        ''')
        return None
    
