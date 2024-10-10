
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: The file 'nonexistent_file.txt' was not found.")
