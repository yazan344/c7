import termcolor
# Shopping List

# Your shopping list should keep asking for new items until nothing is entered
# (no input followed by enter/return key).
# The program should then print a menu for the user to choose one of the following options:
# (A)dd - To add a new item to the list.
# (F)ind - To search for an item in the list.
# (P)rint - To pretty print the list.
# (S)ort - To sort the list.
# (C)lear - To clear all items in the list.
# (Q)uit - To exit your program.

shopping_list = []

common_list = ['A', 'F', 'P', 'S', 'C', 'Q']


def show_menu():
    print(termcolor.colored("""
    (A)dd - To add a new item to the list.
    (F)ind - To search for an item in the list.
    (P)rint - To pretty print the list.
    (S)ort - To sort the list.
    (C)lear - To clear all items in the list.
    (Q)uit - To exit your program.""", color="green"))


def add_item():
    item = the_item()
    shopping_list.append(item)
    print(shopping_list)


def find_item():
    item = the_item()
    if str(shopping_list).find(item) > 0:
        print(f"your item is in the list")
    else:
        print("your item is not in the list")


def print_list():
    print("\t * ", end="")
    tabbed = "\n \t * ".join(shopping_list)
    print(tabbed)


def sort_list():
    shopping_list.sort()


def clear_list():
    shopping_list.clear()


def quit():
    print("Goodbye! Hope to see you again soon :).")
    exit()


def the_item():
    return input("enter the item: ")


def ask_input():
    options = {'A': add_item, 'F': find_item, 'P': print_list, 'S': sort_list, 'C': clear_list, 'Q': quit}
    choice = input("Please enter a valid letter: ").upper()
    if choice in common_list:
        options[choice]()
    else:
        print("your input is invalid")


while True:
    show_menu()
    ask_input()