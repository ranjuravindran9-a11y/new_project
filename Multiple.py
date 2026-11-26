class Mother():
    def mother_trait(self):
        print("caring nature")

class Father():
    def father_trait(self):
        print("Strong personality")

class Child(Mother,Father):
    pass

c=Child()
c.mother_trait()
c.father_trait()