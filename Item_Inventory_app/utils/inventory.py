class Inventory:
    def __init__(self):
        self.cart = {}

    def add_item(self, item):
        self.cart[item.id] = item.value()

    def remove_item(self, item):
        del self.cart[item.id]

    def total(self):
        self.sum = 0
        for n in self.cart.values():
            self.sum += n
        return self.sum

    def display(self):
        print(f"Your total payment is: {self.sum}")

    def __str__(self):
        items_cart = ''
        for prod in self.cart.keys():
            items_cart += ' ' + prod.__str__()
        return 'The cart has:' + items_cart

