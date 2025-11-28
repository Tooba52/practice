class Book:
    def __init__(self, name: str, author:str, publication: int):
        self.__name = name
        self.__author = author
        self.__publication = publication
    
    def __str__(self):
        #string representation
        return f"{self.__name} was written by {self.__author} and published on {self.__publication}"
    
    def __repr__(self):
        #official representation, for debugging and console
        return (f"Book({self.__name}, {self.__author}, {self.__publication})")
    
    def __eq__(self, other):
        # defines behaviour for ==
        return self.__publication == other.__publication

    def __lt__(self, other):
        # defines behaviour for <
        return self.__publication < other.__publication
    
    def __ne__(self, other):
        # defines behaviour for !=
        return self.__publication != other.__publication

    def __gt__(self, other):
        # defines behaviour for >
        return self.__publication > other.__publication


class Wallet:
    def __init__(self, money:float):
        self.__money = money
    
    def __add__(self, other):
        # defines behaviour for + operator
        return self.__money + other.__money

    def __sub__(self,other):
        # defines behaviour for - operator
        return self.__money - other.__money

class Item:
    def __init__(self, name:str, price:int):
        self.__name = name
        self.__price = price

    def __str__(self):
        return f"{self.__name} = {self.__price}"
    
class ShoppingCart:
    def __init__(self):
        self.__items = []

    def add_item(self,item:Item):
        self.__items.append(item)

    def __len__(self):
        # defines behaviour for len()
        return len(self.__items)

    def __iter__(self):
        # allows for looping 
        return iter(self.__items)


    def __getitem__(self, index):
        # allows for obj[key] (indexing)
        return self.__items[index]



#extras

#     def __le__(self):
#         # defines behaviour for <=
#         pass

#     def __ge__(self):
#         # defines behaviour for >=
#         pass

book1 = Book("Hunters", "Amy M", 2018)
book2 = Book("Princess", "Jasmin B", 2014)
print(book1)
print(book1 == book2)
print(book1 < book2)
print(book1 != book2)
print(book1 > book2)
    
wallet1 = Wallet(560)
wallet2 = Wallet(32)
print(wallet1 + wallet2)
print(wallet1 - wallet2)


shoppingcart = ShoppingCart()
print(len(shoppingcart))
item1 = Item("banana", 1.5)
item2 = Item("apple", 1.2)
shoppingcart.add_item(item1)
shoppingcart.add_item(item2)
print(len(shoppingcart))
for item in shoppingcart:
    print(item)
print(shoppingcart[1])

