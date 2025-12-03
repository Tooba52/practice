class Animal:
    def __init__(self, name: str, birth_year: int):
        self._name = name
        self._birth_year = birth_year

    def _getAge(self):
        return (2025 - self._birth_year)
    
    def __str__(self):
        return (f"Animal Name: {self._name}, Birth Year: {self._birth_year}, Animal Age: {self._getAge()}")
    
class Cat(Animal):
    def __init__(self, name: str, birth_year: int, breed: str):
        super().__init__(name, birth_year)
        self.__breed = breed

    
    

animal = Animal("bob", 2018)
cat = Cat("angel", 2021, "tabby")
print(animal)
print(cat)

    
