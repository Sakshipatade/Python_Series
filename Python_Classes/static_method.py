class Car:
    def __init__(self, brand, year):
        self.__brand = brand
        self.year = year

    def get_brand(self):
        return f'brand is {self.__brand} with year {self.year}'
    

    @staticmethod
    def getCarInfo():
        return 'Car is good for transportation.'
    
class ElectricCar(Car):
    def __init__(self, brand, year, batter_size):
        super().__init__(brand, year)
        self.battery_size = batter_size

# 1. method is called using main class name
Car('suzuki', 2023)
print(Car.getCarInfo())

# 2. method is called using object of main class
car = Car('suzuki', 2023)
print(car.getCarInfo())

# 3. method is called using child class name
ElectricCar('tesla', 2025, '60kWH')
print(ElectricCar.getCarInfo())

# 4. method is called using object of child class
electric = ElectricCar('tesla', 2025, '80kWH')
print(electric.getCarInfo())


'''
1. It belongs to the class.
2. It is inherited by subclasses.
3. It can be called using the class.
4. It can also be called using any object of that class or its subclasses.
5. The only special behavior is that Python does not automatically pass self (or cls).

'''