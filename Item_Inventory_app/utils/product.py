from utils.items import values

class Product:
    def __init__(self, id, quantity):
        self.id = id
        self.price = values[id]
        self.quantity = quantity

    def __str__(self):
        return 'Your product is: ' + str(self.quantity) + ' ' + self.id

    def increase_quantity(self):
        self.quantity += 1

    def decrease_quantity(self):
        self.quantity -= 1

    def value(self):
        value = self.quantity * self.price
        return value
