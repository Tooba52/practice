class Animal:
    def __init__(self, name: str, birth_year: int):
        self.__name = name
        self.__birth_year = birth_year

    def _getAge(self):
        return (2025 - self.__birth_year)
    
    def __str__(self):
        return (f"Animal Name: {self.__name}, Birth Year: {self.__birth_year}, Animal Age: {self._getAge()}")
    

animal = Animal("bob", 2018)
print(animal)

    
