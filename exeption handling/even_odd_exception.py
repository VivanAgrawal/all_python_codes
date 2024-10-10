try:
    num = int(input("Enter a positive number: "))
   
    if num <= 0:
        raise ValueError("Please enter a positive number.")
   
    if num % 2 == 0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")
except ValueError as e:
    print(f"Error: {e}")