from OOP import Car

class ElectricCar(Car):
    def __init__(self,brand,model,year,battery):
        super().__init__(brand,model,year)
        self.battery=battery

    def battery_info(self):
        print(f"Battery capacity: {self.battery} kWh")

tesla=ElectricCar("Tesla","Model S",2023,100)
tesla.disply_info()
tesla.battery_info()