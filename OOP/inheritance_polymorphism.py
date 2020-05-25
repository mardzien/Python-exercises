class Animal():

    def __init__(self):
        print("Animal created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")


myanimal = Animal()


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self) # creating an instance od animal class
        print("Dog created")

    def who_am_i(self):
        print("I am a dog!")

mydog = Dog()
mydog.who_am_i()


class Dog(object):

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"


class Cat(object):

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"


niko = Dog("niko")
felix = Cat("felix")


for pet in [niko, felix]:
    print(type(pet))
    print(type(pet.speak()))


def pet_speak(pet):
    print(pet.speak())


pet_speak(niko)
pet_speak(felix)