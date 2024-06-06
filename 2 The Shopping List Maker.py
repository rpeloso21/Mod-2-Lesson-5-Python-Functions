#Tasks 1
def add_item():
    item = input("What would you like to add to your list?")
    shopping_list.append(item)
    print(f"Your shopping list not contains {shopping_list}")

# Task 2
def remove_item():
    item = input("What would you like to remove from your list?")
    shopping_list.remove(item)
    print(f"Your shopping list not contains {shopping_list}")

# Task 3
def print_list():
    print(f"Your shopping list containes: {shopping_list}")

shopping_list = []

while True:

    operation = input("Would you like to add an item, remove an item, or print your list? add/remove/print")

    if operation.lower() == "add":
        add_item()

    elif operation.lower() == "remove":
        remove_item()

    elif operation.lower() == "print":
        print_list()

    else:
        print("That is not a valid selection")

    quit = input("Are you done with your list?")
    if quit.lower() == "yes":
        break

print("Thank you for using our list creator.")