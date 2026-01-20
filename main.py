# Main run file. Holds the user interface
import sys
import termios
import tty
import os

def get_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch1 = sys.stdin.read(1)
        if ch1 == '\x1b':
            ch2 = sys.stdin.read(1)
            ch3 = sys.stdin.read(1)
            return ch1 + ch2 + ch3
        return ch1
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def menu(options):
    index = 0
    while True:
        os.system("clear")
        for i, option in enumerate(options):
            prefix = "> " if i == index else "  "
            print(prefix + option)
        key = get_key()
        if key == '\x1b[A':
            index = (index - 1) % len(options)
        elif key == '\x1b[B':
            index = (index + 1) % len(options)
        elif key == "\r":
            return index
    
def add():
    print("you have entered the add function") #Joseph
    input("Press Enter to continue...")

def skills():
    print("you have entered the skill managment function") #Douglas
    input("Press Enter to continue...")

def inventory():
    print("you have entered the inventory managment function") #Govenor
    input("Press Enter to continue...")

def attributes():
    print("you have entered the attribute managment function") #Darin
    input("Press Enter to continue...")

def search():
    print("you have entered the search function") #Joseph
    input("Press Enter to continue...")

def main():
    selected_character = ""
    options = ["Add Character", "Manage Skills", "Manage Inventory", "Manage Attributes", "Search for Character"]
    while True:
        choice = menu(options)
        if choice == 0:
            add()
        elif choice == 1:
            if selected_character != "":
                skills()
            else:
                print("Please select a character before entering this function.")
                input("Press Enter to continue...")
                main()
        elif choice == 2:
            if selected_character != "":
                inventory()
            else:
                print("Please select a character before entering this function.")
                input("Press Enter to continue...")
                main()
        elif choice == 3:
            if selected_character != "":
                attributes()
            else:
                print("Please select a character before entering this function.")
                input("Press Enter to continue...")
                main()
        else:
            selected_character = search()

main()