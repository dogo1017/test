# DU p1 - Attribute Manager

from menu import menu

def attribute_menu(characters, selected_character):
    """
    Main attribute management menu
    Returns: (characters, selected_character) tuple
    """
    
    # If no character selected, let user select one
    if selected_character == "":
        char_names = [char["name"] for char in characters]
        char_names.append("Return")
        result = menu(char_names)
        selected_index = result['index']
        
        if selected_index >= len(characters):
            return characters, selected_character
        
        selected_character = characters[selected_index]["name"]
    
    # Find the selected character in the characters list
    current_character = None
    char_index = 0
    for i, char in enumerate(characters):
        if char["name"] == selected_character:
            current_character = char
            char_index = i
            break
    
    if current_character is None:
        print("Character not found!")
        input("Press Enter to continue...")
        return characters, ""
    
    # Main attribute management loop
    while True:
        # Build attribute options list
        attribute_options = [
            "Modify Level",
            "Modify Damage", 
            "Modify Dexterity",
            "Modify Intelligence",
            "Modify Constitution",
            "Modify Charisma",
            "View All Attributes",
            "Return"
        ]
        
        result = menu(attribute_options)
        choice = result['index']
        
        if choice == 0:
            # Modify Level
            modify_level(characters, char_index)
        elif choice == 1:
            # Modify Damage
            modify_attribute(characters, char_index, 0, "Damage")
        elif choice == 2:
            # Modify Dexterity
            modify_attribute(characters, char_index, 1, "Dexterity")
        elif choice == 3:
            # Modify Intelligence
            modify_attribute(characters, char_index, 2, "Intelligence")
        elif choice == 4:
            # Modify Constitution
            modify_attribute(characters, char_index, 3, "Constitution")
        elif choice == 5:
            # Modify Charisma
            modify_attribute(characters, char_index, 4, "Charisma")
        elif choice == 6:
            # View All Attributes
            view_attributes(current_character)
        else:
            # Return
            break
    
    return characters, selected_character


def modify_level(characters, char_index):
    """Modify character level"""
    current_level = characters[char_index].get("level", 1)
    
    print(f"\nCurrent Level: {current_level}")
    print("Use Left/Right arrows to adjust level, Enter to save")
    
    result = menu(
        [f"New Level", "Save Changes", "Cancel"],
        number=[0],
        num_min=1,
        num_max=100
    )
    
    if result['index'] == 1:  # Save Changes
        new_level = result['numbers'][0]
        characters[char_index]["level"] = new_level
        print(f"\nLevel updated to {new_level}!")
        input("Press Enter to continue...")
    else:
        print("\nLevel change cancelled.")
        input("Press Enter to continue...")


def modify_attribute(characters, char_index, attr_index, attr_name):
    """Modify a specific attribute in the attributes list"""
    # Ensure attributes list exists and has enough elements
    if "attributes" not in characters[char_index]:
        characters[char_index]["attributes"] = [1.0, 1.0, 1.0, 1.0, 1.0]
    
    current_value = characters[char_index]["attributes"][attr_index]
    
    print(f"\nCurrent {attr_name}: {current_value}")
    print("Use Left/Right arrows to adjust (increment: 0.1), Enter to save")
    
    # Convert current value to increments of 0.1 for the number field
    current_increments = int(current_value * 10)
    
    result = menu(
        [f"New {attr_name}", "Save Changes", "Cancel"],
        number=[0],
        num_min=-100,
        num_max=100
    )
    
    if result['index'] == 1:  # Save Changes
        # Convert increments back to decimal value
        new_value = result['numbers'][0] / 10.0
        characters[char_index]["attributes"][attr_index] = new_value
        print(f"\n{attr_name} updated to {new_value}!")
        input("Press Enter to continue...")
    else:
        print(f"\n{attr_name} change cancelled.")
        input("Press Enter to continue...")


def view_attributes(character):
    """Display all character attributes"""
    print(f"\n{'='*50}")
    print(f"Character Attributes for: {character.get('name', 'Unknown')}")
    print(f"{'='*50}")
    print(f"Class: {character.get('class', 'N/A')}")
    print(f"Race: {character.get('race', 'N/A')}")
    print(f"Level: {character.get('level', 1)}")
    
    # Display attributes
    if "attributes" in character and character["attributes"]:
        attr_names = ["Damage", "Dexterity", "Intelligence", "Constitution", "Charisma"]
        print(f"\nAttributes:")
        for i, attr_name in enumerate(attr_names):
            if i < len(character["attributes"]):
                print(f"  {attr_name}: {character['attributes'][i]}")
    
    # Display skills if they exist
    if "skills" in character and character["skills"]:
        print(f"\nSkills: {len(character['skills'])} total")
        for skill_name in character["skills"]:
            print(f"  - {skill_name}")
    
    # Display inventory if it exists
    if "inventory" in character and character["inventory"]:
        print(f"\nInventory: {len(character['inventory'])} items")
        for item in character["inventory"]:
            if isinstance(item, dict) and "name" in item:
                print(f"  - {item['name']}")
            elif isinstance(item, dict):
                print(f"  - {list(item.keys())[0] if item else 'Unknown item'}")
    
    print(f"{'='*50}\n")
    input("Press Enter to continue...")