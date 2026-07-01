class Computer:
    def __init__(self, maxPrice):
        self.__maxPrice = maxPrice
        print(f'Already set price is {self.__maxPrice}')

    def sell(self):
        print(f'current selling price is {self.__maxPrice}')

    def setMaxPrice(self, price):
        self.__maxPrice = price

    def discount(self, amount):
        self.__maxPrice -= amount


class Comp(Computer):
    def __init__(self, maxPrice, model):
        super().__init__(maxPrice)
        self.model = model

    def compInfo(self):
        return f'price is {self.__maxPrice} and model is {self.model}'  
        '''here we can't access maxprice because we make it private using (__)double underscore and 
           only accessible to that class only where the maxPrice get created. this is called as encapsulation.
         '''


comp = Comp(2000, 'dell')
comp.compInfo()
# comp.sell()
# comp.setMaxPrice(1500)
# comp.sell()
# comp.discount(300)
# comp.sell()



# comp = Computer(1200)
# comp.sell()
# comp.setMaxPrice(1500)
# comp.sell()
# comp.discount(500)
# comp.sell()
