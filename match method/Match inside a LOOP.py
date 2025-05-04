while True:
    choice = input("\nEnter your command (start, stop, exit): ").lower()

    match choice:
        case 'start':
            print("🚗 Car started...")
        case 'stop':
            print("🚦 Car stopped.")
        case 'exit':
            print("👋 Exiting program.")
            break
        case _:
            print("❗ Unknown command, try again.")