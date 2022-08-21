def show_menu():
    print("""
    (A)dd - To add a new item to the list.
    (F)ind - To search for an item in the list.
    (P)rint - To pretty print the list.
    (S)ort - To sort the list.
    (C)lear - To clear all items in the list.
    (Q)uit - To exit your program.""")


def add_item():
    item = the_item()
    shopping_list.append(item)
    print(shopping_list)


def find_item():
    item = the_item()
    return str(shopping_list).find(item)


def print_list():
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
    options[choice]()


while True:
    show_menu()
    ask_input()