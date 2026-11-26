class Animal():
    def __init__(self,name):
        self.name=name

    def make_sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Bark! Bark!")

class Cat(Animal):
    def make_sound(self):
        print("Meow! Meow!")

dog=Dog("Buddy")
cat=Cat("Whiskers")

dog.make_sound()
cat.make_sound()