
def divide_numbers():
    try:
        dividend = int(input("Enter the dividend: "))
        divisor = int(input("Enter the divisor: "))
        result = dividend / divisor
    except ZeroDivisionError:
        print("Error: Division by zero")
    except ValueError:
        print("Error: Invalid input - Please enter valid numbers")
    else:
        print(f"Result of {dividend} / {divisor} is {result:.2f}")

divide_numbers()