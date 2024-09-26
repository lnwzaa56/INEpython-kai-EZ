class Dog:
    species = "mamma"

    def calAge(self, age):
        print("dog age is {}".format(age*3))

class SomeBread(Dog):
    pass

class SomeOtherBread(Dog):
    species = " reptile"
    def calAge(self, age):
        print("Dog Age is {}". format(age*4))

frank = SomeBread()
print(frank.species)
frank.calAge(5)

bean = SomeOtherBread
print(bean.species)
bean.calAge(5)