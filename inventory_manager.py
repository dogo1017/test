#Should end up here after a character has been selected and they wanna make/edit a certain inventory

saved_inventorys = {}

from menu import menu


def add_items(items, characters, selected_character):
    print(f"\nThis is what your inventory looks like right now:\n")

    # Find the character object
    current_character = None
    for char in characters:
        if char["name"] == selected_character:
            current_character = char
            break
    
    if current_character is None:
        print("Character not found!")
        input("Press Enter to continue...")
        return

    if "inventory" not in current_character:
        current_character["inventory"] = []

    # Print available items from the items list passed from main
    if len(items) == 0:
        print("No items available.")
    else:
        for item in items:
            print(f"{item['name']}: {item}")

    item_choice = input('Which item would you like to add to your inventory? (type "return" if you want to go back to menu):  ')

    if item_choice.lower() == "return":
        return

    # Find the item in the items list
    found_item = None
    for item in items:
        if item["name"] == item_choice:
            found_item = item
            break
    
    if found_item:
        current_character["inventory"].append(found_item)
        print(f"{item_choice} added to inventory.")
        input("Press Enter to continue...")
    else:
        print("Item not found.")
        input("Press Enter to continue...")


def remove_items(characters, selected_character):
    # Find the character object
    current_character = None
    for char in characters:
        if char["name"] == selected_character:
            current_character = char
            break
    
    if current_character is None:
        print("Character not found!")
        input("Press Enter to continue...")
        return

    if "inventory" not in current_character or len(current_character["inventory"]) == 0:
        print("No inventory to remove.")
        input("Press Enter to continue...")
        return

    item_names = [item["name"] for item in current_character["inventory"]]
    item_names.append("Return")
    
    result = menu(item_names)
    selected = result['index']
    
    if selected < len(current_character["inventory"]):
        removed = current_character["inventory"].pop(selected)
        print(f"Removed {removed['name']}")
        input("Press Enter to continue...")


def inventory_menu(items, characters, selected_character):
    options = ["Add items", "Remove items", "Return to Menu"]
    while True:
        choice = menu(options)
        if choice.get('index') == 0:
            add_items(items, characters, selected_character)
        elif choice.get('index') == 1:
            remove_items(characters, selected_character)
        elif choice.get('index') == 2:
            return characters, selected_character