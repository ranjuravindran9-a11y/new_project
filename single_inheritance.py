class Parent():
    def greet(self):
        print("Hello from parent!")


class Child(Parent):
    pass

c=Child()
c.greet()