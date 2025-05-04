category = input("Enter category (fruit, animal, color): ").lower()
item = input("Enter name: ").lower()

match category:
    case 'fruit':
        match item:
            case 'apple' | 'banana' | 'mango':
                print(f"{item.capitalize()} is a tasty fruit!")
            case _:
                print(f"{item.capitalize()} is not in our fruit list.")
    case 'animal':
        match item:
            case 'dog' | 'cat' | 'lion':
                print(f"{item.capitalize()} is a great animal!")
            case _:
                print(f"{item.capitalize()} is not in our animal list.")
    case 'color':
        match item:
            case 'red' | 'blue' | 'green':
                print(f"{item.capitalize()} is a beautiful color!")
            case _:
                print(f"{item.capitalize()} is not in our color list.")
    case _:
        print("Invalid category entered.")
