try:
    my_list = [1, 2, 3]
    index = int(input("Enter an index: "))
    value = my_list[index]
    print(f"Value at index {index}: {value}")
except IndexError as e:
    print(f"Error: Index out of range - {e}")
except ValueError as e:
    print(f"Error: {e}. Please enter a valid index.")