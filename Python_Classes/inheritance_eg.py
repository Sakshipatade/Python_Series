class Car:
    def __init__(self, model, year):
        self.modelname = model
        self.yearValue = year
    
    def carInfo(self):
        return f'Model is {self.modelname} with {self.yearValue} year'


class ElectricCar(Car):
    def __init__(self, model, year, batter_size):
        super().__init__(model, year)
        self.batterySize = batter_size

    def electricCarInfo(self):
        super().carInfo()

electric = ElectricCar('tesla', 2025, '90kWH')
print(electric.electricCarInfo())
