class animal:
    def __init__(self, name ) -> None:
        self.name = name 
    
    def speak(self):
        return "Some sound"
    
class Dog(animal):
    def speak(self):
        return f"{self.name} say woof!"
    
class Cat(animal):
    def speak(self):
        return f"{self.name} says meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())
print(cat.speak())