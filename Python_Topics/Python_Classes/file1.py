class Car:
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model

    def carInfo(self):
        print(f'brand is {self.brand} and model is {self.model}')


tigor: Car = Car('Tigor', '2023')
tigor.carInfo()

bmw = Car('BMW', '2026')
bmw.carInfo()