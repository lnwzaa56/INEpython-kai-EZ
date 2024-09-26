class Dog: 

    species = "mamma"

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age 

    def description(self):
        return "{} is {} year old ".format(self.name, self.age)
    
    def speak(self, sound):
        return "{} says {}".format(self.name , sound)
mikey = Dog("mikey",6)

print(mikey.description())
print(mikey.speak("Gruff Gruff"))