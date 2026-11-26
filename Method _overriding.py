class Bird():
    def speak(self):
        print("Bird is chirping")

class Parrot(Bird):
    def speak(self):
        print("Parrot says,hello!")

b=Bird()
p=Parrot()

b.speak()
p.speak()