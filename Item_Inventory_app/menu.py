from app import user_options

print("======Welcome to Product Inventory Cart=====")


options='''Choose from the following:
        press 1 to new add item
        press 2 to remove item
        press 3 to increase/decrease quantity
        press 4 to show available items
        press q to exit
'''

def menu():
    while True:
        user_input = input(options)
        if user_input in ('1','2','3','4'):
            user_options[user_input]()
        elif user_input=='q':
            break
        else:
            print("Not valid option.Try again")
            continue

menu()
