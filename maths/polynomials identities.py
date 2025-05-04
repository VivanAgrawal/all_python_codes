def square_identity():
    print("Choose an identity:")
    print("1: (a + b)^2 = a^2 + 2ab + b^2")
    print("2: (a - b)^2 = a^2 - 2ab + b^2")
    print("3: a^2 - b^2 = (a + b)(a - b)")
    print("4: (a + b)(a + c) = a^2 + (b + c)a + bc")
    print("5: (a + b + c)^2 = a^2 + b^2 + c^2 + 2ab + 2bc + 2ca")
    choice = input("Enter 1 to 5: ")
    a = int(input("Enter value for a: "))
    b = int(input("Enter value for b: "))
    c = 0
    if choice == '5':
        c = int(input("Enter value for c: "))
    print(f"Values: a = {a}, b = {b}, c = {c}")
    side = input("Do you want to compute LHS or RHS? (Enter 'LHS' or 'RHS'): ").strip().upper()
    
    if choice == '1':
        lhs = (a + b) ** 2
        rhs = a ** 2 + 2 * a * b + b ** 2
    elif choice == '2':
        lhs = (a - b) ** 2
        rhs = a ** 2 - 2 * a * b + b ** 2
    elif choice == '3':
        lhs = a ** 2 - b ** 2
        rhs = (a + b) * (a - b)
    elif choice == '4':
        lhs = (a + b) * (a + c)
        rhs = a ** 2 + (b + c) * a + b * c
    else:
        lhs = (a + b + c) ** 2
        rhs = a ** 2 + b ** 2 + c ** 2 + 2 * a * b + 2 * b * c + 2 * c * a
    
    user_answer = int(input(f"Enter your calculated value for {side}: "))
    correct_answer = lhs if side == "LHS" else rhs
    
    if user_answer == correct_answer:
        print("Correct! Well done.")
    else:
        print(f"Incorrect. The correct answer was {correct_answer}.")

def cubic_identity():
    print("Choose an identity:")
    print("1: (a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3")
    print("2: (a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3")
    print("3: a^3 + b^3 = (a + b)(a^2 - ab + b^2)")
    print("4: a^3 - b^3 = (a - b)(a^2 + ab + b^2)")
    print("5: a^3 + b^3 + c^3 - 3abc = (a + b + c)(a^2 + b^2 + c^2 - ab - bc - ca)")
    choice = input("Enter 1 to 5: ")
    a = int(input("Enter value for a: "))
    b = int(input("Enter value for b: "))
    c = 0
    if choice == '5':
        c = int(input("Enter value for c: "))
    print(f"Values: a = {a}, b = {b}, c = {c}")
    side = input("Do you want to compute LHS or RHS? (Enter 'LHS' or 'RHS'): ").strip().upper()
    
    if choice == '1':
        lhs = (a + b) ** 3
        rhs = a ** 3 + 3 * a ** 2 * b + 3 * a * b ** 2 + b ** 3
    elif choice == '2':
        lhs = (a - b) ** 3
        rhs = a ** 3 - 3 * a ** 2 * b + 3 * a * b ** 2 - b ** 3
    elif choice == '3':
        lhs = a ** 3 + b ** 3
        rhs = (a + b) * (a ** 2 - a * b + b ** 2)
    elif choice == '4':
        lhs = a ** 3 - b ** 3
        rhs = (a - b) * (a ** 2 + a * b + b ** 2)
    else:
        lhs = a ** 3 + b ** 3 + c ** 3 - 3 * a * b * c
        rhs = (a + b + c) * (a ** 2 + b ** 2 + c ** 2 - a * b - b * c - c * a)
    
    user_answer = int(input(f"Enter your calculated value for {side}: "))
    correct_answer = lhs if side == "LHS" else rhs
    
    if user_answer == correct_answer:
        print("Correct! Well done.")
    else:
        print(f"Incorrect. The correct answer was {correct_answer}.")

def main():
    print("Polynomial Identity Revision Game")
    print("Choose the type of identity:")
    print("1: Square Identities")
    print("2: Cubic Identities")
    choice = input("Enter 1 or 2: ")
    
    if choice == '1':
        square_identity()
    elif choice == '2':
        cubic_identity()
    else:
        print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
