class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance

    #creating the getter method for safety view the method
    def get_balance(self):
        return self.__balance

    #setter method
    def deposit(self,amount):
        if amount>0:
            self.__balance += amount
        else:
            print("error because the is less then 0 ")

account = BankAccount("sandeep",1000)
print(account.name)
print(account.get_balance())
account.deposit(500)
print(account.get_balance())
account.deposit(-100)  # This will trigger the error message
print(account.get_balance())



        