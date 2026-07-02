class Car:
    def __init__(self, brand, year)-> None:
        self.__brand = brand
        self.year = year 

    def get_brand(self):
        return f'brand is {self.__brand} with year {self.year}'
    
    def fuel_type(self):
        return f'fuel type of diesel or petrol'
    
class ElectricCar(Car):
    def __init__(self,brand, year, battery_size):
        super().__init__(brand, year)
        self.batterySize = battery_size

    def fuel_type(self):
        return f'fuel type is electric charge'

electric = ElectricCar('tigor', 2023, '80kWH')
print(electric.fuel_type()) # fuel type is electric charge

car = Car('suzuki', 2025)
print(car.fuel_type()) #fuel type is diesel or petrol


''' here both parent and child class has same method name fuel_type(). but in both classes those methods
are printing diffrent statements according to its class. this is called as polymorphism.
when we called the method by child class's objects it calls the method which is present inside child class
and when we called the fuel_type() method using parent class object, the method inside that class gets called
hence once method is having same name but diffrent forms.

'''
