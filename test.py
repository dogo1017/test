import os
import msvcrt

def menu(options):
    desc = []
    index = 0
    while True:
        os.system('cls')
        for i, option in enumerate(options):
            prefix = "> " if i == index else "  " 
            if i == 0:
                print(f"{prefix}{option}: {''.join(desc)}")
            else:
                print(f"{prefix}{option}")

        key = msvcrt.getch()

        if key in (b'\x00', b'\xe0'):
            key = msvcrt.getch()
            if key == b'H': 
                index = (index - 1) % len(options)
            elif key == b'P':
                index = (index + 1) % len(options)
        elif key == b'\r':
            if index == 0:

                pass 
            else:
                return index
        elif key == b'\b':
            if index == 0 and desc:
                desc.pop()
        else:
            if index == 0:
                desc.append(key.decode('utf-8'))

menu(["one", "two"])