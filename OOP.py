class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year

    def disply_info(self):
        print(f"{self.brand} {self.model} ({self.year})")

# car1=Car("Toyota","Corolla",2022)
# car1.disply_info()