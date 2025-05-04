def quadrilateral_properties(name):
    properties = {
        "square": "The lengths of all its four sides are equal.\nThe measurements of all its four angles are equal.\nThe two diagonals bisect each other at right angles, that is, 90°.\nThe opposite sides of a square are both parallel and equal in length.\nThe lengths of diagonals of a square are equal.",
        "rectangle": "The opposite sides are parallel and equal to each other.\nEach interior angle is equal to 90 degrees.\nThe sum of all the interior angles is equal to 360 degrees.\nThe diagonals bisect each other.\nBoth the diagonals have the same length.",
        "rhombus": "All four sides of the rhombus are equal in length.\nOpposite sides of a rhombus are parallel to each other.\nThe two opposite pairs of angles within the rhombus are equal to each other.\nAny two adjacent angles (angles next to each other) within the rhombus add up to 180°.\nA rhombus is also called a diamond.\nIf two diagonal lines are drawn across each pair of opposite corners, they will be perpendicular to and bisect (divide into equal halves) each other at an angle of 90°.\n These diagonal lines will also bisect the angles they pass through.",
        "parallelogram": "Two pairs of opposite sides are parallel.\nTwo pairs of opposite sides are equal in length.\nTwo pairs of opposite angles are equal in measure.\nThe diagonals bisect each other.\nOne pair of opposite sides is parallel and equal in length.\nAdjacent angles are supplementary.",
        "kite": "Kite has 2 diagonals that intersect each other at right angles.\nA kite is symmetrical about its main diagonal.\nAngles opposite to the main diagonal are equal.\nThe kite can be viewed as a pair of congruent triangles with a common base.\nThe shorter diagonal divides the kite into 2 isosceles triangles.",
        "trapezium": "In trapezium, exactly one pair of opposite sides are parallel.\nThe diagonals intersect each other.\nThe non-parallel sides in the trapezium are unequal except in isosceles trapezium.\nThe sum of adjecent angles is equal to 180 degrees.",
        "isosceles trapezium":"One pair of parallel sides.\nBase angles are congruent.\nThe legs are congruent.\nThe diagonals are congruent.\nOpposite angles are supplementary."
    }
    return properties.get(name.lower(), "Invalid quadrilateral name.")

def calculate_area(name):
    if name == "square":
        side = float(input("Enter side length: "))
        return side ** 2
    elif name == "rectangle":
        length = float(input("Enter length: "))
        breadth = float(input("Enter breadth: "))
        return length * breadth
    elif name == "rhombus":
        d1 = float(input("Enter first diagonal: "))
        d2 = float(input("Enter second diagonal: "))
        return (d1 * d2) / 2
    elif name == "parallelogram":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        return base * height
    elif name == "kite":
        d1 = float(input("Enter first diagonal: "))
        d2 = float(input("Enter second diagonal: "))
        return (d1 * d2) / 2
    elif name == "trapezium":
        a = float(input("Enter first parallel side: "))
        b = float(input("Enter second parallel side: "))
        h = float(input("Enter height: "))
        return ((a + b) / 2) * h
    elif name == "isosceles trapezium":
        a = float(input("Enter first parallel side: "))
        b = float(input("Enter second parallel side: "))
        h = float(input("Enter height: "))
        return ((a + b) / 2) * h
    else:
        return "Invalid quadrilateral name."

def main():
    print("Quadrilateral Properties and Area Calculator")
    name = input("Enter the quadrilateral name: ").strip().lower()
    print(f"Properties: {quadrilateral_properties(name)}")
    area = calculate_area(name)
    if isinstance(area, float):
        print(f"Area: {area}")
    else:
        print(area)

if __name__ == "__main__":
    main()
