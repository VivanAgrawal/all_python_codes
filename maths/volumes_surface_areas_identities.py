import math

def cuboid():
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    h = float(input("Enter height: "))
    print("Choose a formula:")
    print("1: Surface Area = 2(lb + bh + lh)")
    print("2: Lateral Surface Area = 2(l + b)h")
    print("3: Volume = lbh")
    choice = input("Enter 1, 2, or 3: ")
    
    if choice == '1':
        answer = 2 * (l * b + b * h + l * h)
    elif choice == '2':
        answer = 2 * (l + b) * h
    else:
        answer = l * b * h
    
    print(f"Result: {answer}")

def cube():
    l = float(input("Enter length: "))
    print("Choose a formula:")
    print("1: Surface Area = 6 * l^2")
    print("2: Lateral Surface Area = 4 * l^2")
    print("3: Volume = l^3")
    choice = input("Enter 1, 2, or 3: ")
    
    if choice == '1':
        answer = 6 * l ** 2
    elif choice == '2':
        answer = 4 * l ** 2
    else:
        answer = l ** 3
    
    print(f"Result: {answer}")

def cylinder():
    r = float(input("Enter radius: "))
    h = float(input("Enter height: "))
    print("Choose a formula:")
    print("1: Lateral Surface Area = 2πrh")
    print("2: Total Surface Area = 2πr(h + r)")
    print("3: Volume = πr^2h")
    choice = input("Enter 1, 2, or 3: ")
    
    if choice == '1':
        answer = 2 * math.pi * r * h
    elif choice == '2':
        answer = 2 * math.pi * r * (h + r)
    else:
        answer = math.pi * r ** 2 * h
    
    print(f"Result: {answer}")

def cone():
    r = float(input("Enter radius: "))
    h = float(input("Enter height: "))
    l = math.sqrt(r ** 2 + h ** 2)  # Calculating slant height automatically
    print(f"Calculated slant height: {l}")
    print("Choose a formula:")
    print("1: Lateral Surface Area = πrL")
    print("2: Total Surface Area = πr(L + r)")
    print("3: Volume = 1/3 πr^2h")
    choice = input("Enter 1, 2, or 3: ")
    
    if choice == '1':
        answer = math.pi * r * l
    elif choice == '2':
        answer = math.pi * r * (l + r)
    else:
        answer = (1/3) * math.pi * r ** 2 * h
    
    print(f"Result: {answer}")

def sphere():
    r = float(input("Enter radius: "))
    print("Choose a formula:")
    print("1: Surface Area = 4πr^2")
    print("2: Volume = 4/3 πr^3")
    choice = input("Enter 1 or 2: ")
    
    if choice == '1':
        answer = 4 * math.pi * r ** 2
    else:
        answer = (4/3) * math.pi * r ** 3
    
    print(f"Result: {answer}")

def hemisphere():
    r = float(input("Enter radius: "))
    print("Choose a formula:")
    print("1: Base Area = πr^2")
    print("2: Total Surface Area = 3πr^2")
    print("3: Volume = 2/3 πr^3")
    choice = input("Enter 1, 2, or 3: ")
    
    if choice == '1':
        answer = math.pi * r ** 2
    elif choice == '2':
        answer = 3 * math.pi * r ** 2
    else:
        answer = (2/3) * math.pi * r ** 3
    
    print(f"Result: {answer}")

def main():
    print("Volume, Surface Area, and Lateral Surface Area Game")
    print("Choose a shape:")
    print("1: Cuboid")
    print("2: Cube")
    print("3: Cylinder")
    print("4: Cone")
    print("5: Sphere")
    print("6: Hemisphere")
    choice = input("Enter 1 to 6: ")
    
    if choice == '1':
        cuboid()
    elif choice == '2':
        cube()
    elif choice == '3':
        cylinder()
    elif choice == '4':
        cone()
    elif choice == '5':
        sphere()
    elif choice == '6':
        hemisphere()
    else:
        print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
