def view_menu(characters, selected_character, classes, races, items):
    import selecter
    import os

    labels = ["Damage", "Dexterity", "Intelligence", "Constitution", "Charisma"]

    chosen_names = [selected_character]

    while len(chosen_names) < len(characters):
        os.system('cls')
        print(f"Characters selected so far: {', '.join(chosen_names)}")
        print(f"\nAdd another character to compare? (you have {len(characters) - len(chosen_names)} remaining)")
        print("1. Yes")
        print("2. No, show me the comparison")
        choice = input("Choose an option: ").strip()

        if choice != "1":
            break

        result = selecter.selecter(characters)
        if result is None:
            continue
        new_char, characters = result
        new_name = new_char["name"]

        if new_name in chosen_names:
            print(f"'{new_name}' is already selected!")
            input("Press Enter to continue...")
            continue

        chosen_names.append(new_name)

    chosen = [next(c for c in characters if c["name"] == name) for name in chosen_names]

    # Recalculate attributes before displaying
    for c in chosen:
        c["attributes"] = c["base_attributes"].copy()

        race_data = next((r for r in races if r["name"] == c["race"]), None)
        class_data = next((cl for cl in classes if cl["name"] == c["class"]), None)

        for item_name in c["inventory"]:
            item = next((i for i in items if i["name"] == item_name), None)
            if item:
                if "dmg" in item: c["attributes"][0] *= item["dmg"]
                if "dex" in item: c["attributes"][1] *= item["dex"]
                if "int" in item: c["attributes"][2] *= item["int"]
                if "con" in item: c["attributes"][3] *= item["con"]
                if "cha" in item: c["attributes"][4] *= item["cha"]
        if race_data:
            c["attributes"][0] *= race_data["dmg"]
            c["attributes"][1] *= race_data["dex"]
            c["attributes"][2] *= race_data["int"]
            c["attributes"][3] *= race_data["con"]
            c["attributes"][4] *= race_data["cha"]
        if class_data:
            c["attributes"][0] *= class_data["dmg"]
            c["attributes"][1] *= class_data["dex"]
            c["attributes"][2] *= class_data["int"]
            c["attributes"][3] *= class_data["con"]
            c["attributes"][4] *= class_data["cha"]

    os.system('cls')

    title = "  VS  ".join(c["name"] for c in chosen)
    print("=" * len(title))
    print(title)
    print("=" * len(title))
    print()

    col_width = max(len(c["name"]) for c in chosen) + 4

    print("ATTRIBUTES")
    print("-" * (15 + col_width * len(chosen)))
    header = f"{'Stat':<15}" + "".join(f"{c['name']:<{col_width}}" for c in chosen)
    print(header)
    print("-" * (15 + col_width * len(chosen)))

    for i, label in enumerate(labels):
        row = f"{label:<15}" + "".join(f"{round(c['attributes'][i], 2):<{col_width}}" for c in chosen)
        print(row)

    print("\nSKILLS")
    print("-" * (15 + col_width * len(chosen)))
    for c in chosen:
        skills_str = ", ".join(c["skills"]) if c["skills"] else "None"
        print(f"{c['name']}: {skills_str}")

    print("\nINVENTORY")
    print("-" * (15 + col_width * len(chosen)))
    for c in chosen:
        inv_str = ", ".join(c["inventory"]) if c["inventory"] else "None"
        print(f"{c['name']}: {inv_str}")

    print("\n" + "=" * (15 + col_width * len(chosen)))
    input("Press Enter to continue...")
    return characters, selected_character