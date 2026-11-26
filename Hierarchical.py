class Vehicle():
    def start(self):
        print("Starting Vehicle....")

class Car(Vehicle):
    def Car_feature(self):
        print("This is Car")

class Bike(Vehicle):
    def bike_feature(self):
        print("This is Bike.")

c=Car()
b=Bike()

c.start()
b.start()