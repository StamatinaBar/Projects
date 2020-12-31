from utils.product import Product
from utils.inventory import Inventory
from utils.items import values

list_items = []
inv = Inventory()

def show_available_items():
    print("Available products are the following: ")
    count = 1
    for item, value in values.items():
        print(f"{count}) {item} costs: {value}")
        count += 1

def show_cart():
    inv.total()
    inv.display()
    print(inv)

def add_item():
    id = input("Choose new item")
    quantity = int(input("Choose quantity: 1-20"))
    product = Product(id, quantity)
    list_items.append(product)
    inv.add_item(product)
    show_cart()


def remove_item():
    x = input("Choose item to remove")
    for i in list_items:
        if i.id == x:
            inv.remove_item(i)
    show_cart()


def modify_item():
    n = input("Increase quantity of product: ")
    for i in list_items:
        if i.id == n:
            i.increase_quantity()
            inv.add_item(i)
    show_cart()


user_options = {'1': add_item,
              '2': remove_item,
              '3': modify_item,
              '4': show_available_items
              }
