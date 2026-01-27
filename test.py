import os
import msvcrt

"""
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

"""
"""def menu2(options, writable):
    desc = []
    for i in writable:
        desc.append([])
    index = 0
    while True:
        os.system('cls')
        for i, option in enumerate(options):
            prefix = "> " if i == index else "  " 
            if i in writable:
                print(f"{prefix}{option}: {''.join(desc[i])}")
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
            if index in writable:
                pass 
            else:
                return index
        elif key == b'\b':
            if index in writable and desc[index]:
                desc[index].pop()
        else:
            if index in writable:
                desc[index].append(key.decode('utf-8'))

menu2(["description", "effect", "target", "return"], [0,1,2])"""
"""
def menu(options, **mod):
    writable = mod.get('writable', [])
    toggle = mod.get('toggle', [])
    default_TF = mod.get('default_vals', [])
    states = {i: 0 for i in toggle} 
    text_data = {i: [] for i in writable}
    index = 0
    while True:
        os.system('cls')
        for i, option in enumerate(options):
            prefix = "> " if i == index else "  " 
            if i in writable:
                print(f"{prefix}{option}: {''.join(text_data[i])}")
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
            if index in writable:
                return {'index': index, 'writable': text_data}
            elif index in toggle:
                states[index] *= -1
            else:
                return index
        elif key == b'\b':
            if index in writable and text_data[index]:
                text_data[index].pop()
        else:
            if index in writable:
                text_data[index].append(key.decode('utf-8'))
input = menu(["Hi", "bored", "Dont know"], writable = [1,2])

stuff = input['writable'][1]
print(stuff)
"""

def menu(options, **mod):
    number = mod.get('number', [])
    writable = mod.get('writable', [])
    toggle = mod.get('toggle', [])
    default_TF = mod.get('default_vals', [])
    states = {i: 0 for i in toggle} 
    text_data = {i: [] for i in writable}
    index = 0
    num = {}
    for i in number:
        num[i] = 1
        tog = {}
    for i in toggle:
        tog[i] = True
    if not toggle:
        tog = {'empty'}
    while True:
        os.system('cls')
        for i, option in enumerate(options):
            prefix = "> " if i == index else "  " 
            if i in writable:
                print(f"{prefix}{option}: {''.join(text_data[i])}")
            elif i in toggle:
                status = "True" if tog[i] else "False"
                print(f"{prefix}{option}: {status}")
            elif i in number:
                print(f"{prefix}{option} <{num[i]}>")
            else:
                print(f"{prefix}{option}")

        key = msvcrt.getch()

        if key in (b'\x00', b'\xe0'):
            key = msvcrt.getch()
            if key == b'H': 
                index = (index - 1) % len(options)
            elif key == b'P':
                index = (index + 1) % len(options)
        elif key == b"K":
            if index in number:
                num[index] -= 1
            elif index in toggle:
                tog[index] = not tog[index]
        elif key == b"M":
            if index in number:
                num[index] += 1
            elif index in toggle:
                tog[index] = not tog[index]
        elif key == b'\r':
            if index in writable:
                return {'index': index, 'numbers': num, 'toggles': tog, 'writable': text_data}
            elif index in toggle:
                states[index] *= -1
            else:
                return {'index': index, 'numbers': num, 'toggles': tog, 'writable': text_data}
        elif key == b'\b':
            if index in writable and text_data[index]:
                text_data[index].pop()
        else:
            if index in writable:
                text_data[index].append(key.decode('utf-8'))
input = menu(["Hi", "bored", "Dont know"], writable = [1], toggle = [2])

stuff = input['writable'][1]
print(stuff)