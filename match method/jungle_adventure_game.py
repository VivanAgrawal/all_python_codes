print("🌲 Welcome to the Jungle Adventure Game! 🌲")
print("You're standing at a fork in the road...")

print("\nChoose a direction:")
print("1. Go Left")
print("2. Go Right")

choice1 = input("Enter your choice (1/2): ")

match choice1:
    case "1":
        print("\nYou went left and found a river.")
        print("Do you:")
        print("a) Swim across")
        print("b) Look for a bridge")

        choice2 = input("Enter your choice (a/b): ")

        match choice2:
            case "a":
                print("🐊 Oh no! You were eaten by a crocodile. Game Over!")
            case "b":
                print("🌉 You found a bridge and safely crossed the river!")
                print("You win! 🎉")
            case _:
                print("Invalid choice.")
    case "2":
        print("\nYou went right and see a cave.")
        print("Do you:")
        print("a) Enter the cave")
        print("b) Walk past it")

        choice3 = input("Enter your choice (a/b): ")

        match choice3:
            case "a":
                print("👻 A ghost scared you! You ran away. Game Over!")
            case "b":
                print("☀ You walked safely and found treasure outside!")
                print("You win! 🏆")
            case _:
                print("Invalid choice.")
    case _:
        print("Invalid direction. Game Over.")