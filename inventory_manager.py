from menu import menu


def add_item(items, character):
    result = menu(["Add Existing item", "Edit Existing item", "Add New item", "Return"])
    result = result['index']
    
    if result == 0:
        item_names = list(items.keys())
        item_result = menu([*item_names, "Return"])
        selected = item_result['index']
        if selected < len(item_names):
            selected_item = item_names[selected]
            if selected_item in character["items"]:
                print(f"{selected_item} is already in character's items!")
                input("Press Enter to continue...")
            else:
                character["items"].add(selected_item)
                print(f"Added {selected_item} to character!")
                input("Press Enter to continue...")
        return
    
    elif result == 1:
        if not character["items"]:
            print("No items to edit!")
            input("Press Enter to continue...")
            return
        item_list = list(character["items"])
        edit_result = menu([*item_list, "Return"])
        selected = edit_result['index']
        if selected < len(item_list):
            item_to_edit = item_list[selected]
            if item_to_edit in items:
                item_data = menu(
                    ["item Name", "item Description", "item Effect", "Effect Strength", "item Target", "Save Changes", "Return"],
                    writable=[0, 1],
                    toggle=[2, 4],
                    tog_opts=[["Attack", "Defense", "Health"], [["Enemy", "Self", "Ally"], [4]]],
                    number=[3]
                )
                if item_data['index'] == 5:
                    new_name = ''.join(item_data['writable'][0]) or item_to_edit
                    new_desc = ''.join(item_data['writable'][1]) or items[item_to_edit]["description"]
                    items[new_name] = {
                        "description": new_desc,
                        "effect": item_data['toggles'][2],
                        "amount": item_data['numbers'][3],
                        "target": item_data['toggles'][4]
                    }
                    if new_name != item_to_edit:
                        del items[item_to_edit]
                        character["items"].discard(item_to_edit)
                        character["items"].add(new_name)
                    print("item updated!")
                    input("Press Enter to continue...")
        return
    
    elif result == 2:
        item_data = menu(
            ["item Name", "item Description", "item Effect", "Effect Strength", "item Target", "Save item", "Return"],
            writable=[0, 1],
            toggle=[2, 4],
            tog_opts=[["Attack", "Defense", "Health"], [["Enemy", "Self", "Ally"], [4]]],
            number=[3]
        )
        
        if item_data['index'] == 5:
            item_name = ''.join(item_data['writable'][0])
            item_desc = ''.join(item_data['writable'][1])
            
            if item_name:
                if item_name in character["items"]:
                    print(f"{item_name} is already in character's items!")
                else:
                    items[item_name] = {
                        "description": item_desc,
                        "effect": item_data['toggles'][2],
                        "amount": item_data['numbers'][3],
                        "target": item_data['toggles'][4]
                    }
                    character["items"].add(item_name)
                    print(f"Created and added {item_name} to character!")
            else:
                print("item name cannot be empty!")
            input("Press Enter to continue...")
        return
def remove_item(character):
    if not character["items"]:
        print("No items to remove!")
        input("Press Enter to continue...")
        return
    
    item_list = list(character["items"])
    result = menu([*item_list, "Return"])
    selected = result['index']
    
    if selected < len(item_list):
        removed_item = item_list[selected]
        character["items"].discard(removed_item)
        print(f"Removed {removed_item} from character!")
        input("Press Enter to continue...")

def inventory_menu(items, characters, selected_character):
    item_manage = 1
    while item_manage == 1:
        result = menu(["Add item", "Remove item", "View Character items", "Return"])
        selected_index = result['index']
        if selected_index == 0:
            for i in characters:
                if selected_character in characters[i]:
                    item_index = i
            add_item(characters[i])
        elif selected_index == 1:
            remove_item()
        elif selected_index == 2:
            print(f"\n{selected_character['name']}'s items:")
            if characters["items"]:
                for item in selected_character["items"]:
                    if item in items:
                        item_info = items[item]
                        print(f"\n  {item}")
                        print(f"    Description: {item_info['description']}")
                        print(f"    Effect: {item_info['effect']}")
                        print(f"    Strength: {item_info['amount']}")
                        print(f"    Target: {item_info['target']}")
            else:
                print("  No items yet!")
            input("\nPress Enter to continue...")
        else:
            item_manage = 0
