"""
import os
import msvcrt

def menu(options):
    desc = []
    index = 0
    while True:
        os.system('cls')
        for i, option in enumerate(options):
            prefix = "> " if i == index else "  "
            print(prefix + option)
        key = msvcrt.getch()
        if key in (b'\x00', b'\xe0'):
            key = msvcrt.getch()
        if key == b"H":
            index = (index - 1) % len(options)
        elif key == b"P":
            index = (index + 1) % len(options)
        elif key == b"\r" and index == 0:
            return index  
        if index == 0:
            text = input("Press enter to choose different option")
              
        
        
menu(["text","return"])
"""