class Animal:
    def __init__(self, name: str, birth_year: int):
        self._name = name
        self._birth_year = birth_year

    def _getAge(self):
        return (2025 - self._birth_year)
    
    def speak(self):
        print("Animal Noise")

    def name(self):
        return self._name
    
    def birth_year(self):
        return self._birth_year
    
    def __str__(self):
        return (f"Animal Name: {self.name()}, Birth Year: {self.birth_year()}, Animal Age: {self._getAge()}")
    
class Cat(Animal):
    def __init__(self, name: str, birth_year: int, breed: str):
        super().__init__(name, birth_year)
        self.__breed = breed
    
    def speak(self):
        print("Meow")

    def breed(self):
        return self.__breed

    def __str__(self):
        return (f"Cat Name: {self.name()}, Birth Year: {self.birth_year()}, Cat Age: {self._getAge()}, Cat Breed: {self.breed()}")
    

animal = Animal("bob", 2018)
cat = Cat("angel", 2021, "tabby")
print(animal)
print(cat)
animal.speak()
cat.speak()
print(cat.name())
print(animal.birth_year())

    
