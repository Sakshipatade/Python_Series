class Fruit:

    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def totalCost(self):
        self.total_cost = self.price * self.quantity
        return self.total_cost
    
mango = Fruit(50, 3)
apple = Fruit(20,6)
mango.totalCost()
apple.totalCost()

print(mango.__dict__)
# print(mango.total_cost)
# print(apple.total_cost)
# print(mango.total_cost)
