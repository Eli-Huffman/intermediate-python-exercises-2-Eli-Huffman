class bankAccount:
    def __init__(self, account_name, starting_balance):
        self.account_name = account_name
        self.starting_balance = starting_balance
    
    #Getters
    def get_balance(self):
        return (self.account_name+" has a balance of "+str(self.starting_balance))

    #Setters
    def withdraw_balance(self, amount):
        self.starting_balance -= amount
    
    def deposit_balance(self, amount):
        self.starting_balance += amount