import termcolor
import pyfiglet
print((pyfiglet.figlet_format("Group_3")))

command_list = ["A", "F", "P", "S", "C", "Q"]
shopping_list = []


def show_menu():
    print(termcolor.colored("""
    What Do You Do?
    "A" - To add a new item to the list.
    "F" - To search for an item in the list.
    "P" - To pretty print the list.
    "S" - To sort the list.
    "C" - To clear all items in the list.
    "Q" - To exit your program.
    Choose Option : 
    """, 'green'))

def add_list():
    item = the_item()
    shopping_list.append(item)
    print(shopping_list)


def find_list():
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
    return shopping_list.sort()


def clear_list():
    shopping_list.clear()


def exit_list():
    print("Goodbye! Hope to see you again soon :) ")
    exit()


def the_item():
    return input("enter the item : ")


def ask_input():
    # check if command in my list
    choice = input("Please enter a valid letter: ").upper()
    # options = {'A':add_item, 'F':find_item, 'P':print_list, 'S':sort_list, 'C':clear_list, 'Q':quit}

    if choice in command_list:
        print(f"Command {choice} is Found")
        if choice == "A":
            add_list()

        elif choice == "S":
            sort_list()

        elif choice == "P":
            print_list()

        elif choice == "F":
            find_list()

        elif choice == "C":
            clear_list()
        else:
            exit()

    else:
        print(f"Sorry Command \"{choice}\" Is Not Found!")

while True:
    show_menu()
    ask_input()
