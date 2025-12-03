class Bank:
    exchange_rate = 1.25 #static attribute

    def statement(): #static method 
        print(f"Th exchange rate is {Bank.exchange_rate}")

    def __init__(self, amount: int, name : str):
        self.__name = name #instance attribute
        self.__amount = amount #instance attribute

    def convert(self): #instance method
        return self.__amount * Bank.exchange_rate
        
        
    
bob = Bank(1000, "bob")
Bank.statement()
print(bob.convert())