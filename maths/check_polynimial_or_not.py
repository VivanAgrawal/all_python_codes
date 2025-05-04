def is_polynomial(expression):
    try:
        # Remove whitespaces
        expression = expression.replace(" ", "")
        
        # Split expression into terms
        terms = expression.replace("-", "+-").split('+')  # Handle subtraction correctly
        max_degree = 0  # Track highest degree
        
        for term in terms:
            if 'x' in term:
                if '/' in term:
                    return False  # Variable in denominator detected
                
                parts = term.split('*')
                for part in parts:
                    if 'x' in part and '**' in part:
                        base, exp = part.split('**')
                        if '/' in exp or '.' in exp or float(exp) < 0:
                            return False  # Fractional or negative exponent detected
                        max_degree = max(max_degree, int(float(exp)))
                    elif part == 'x':
                        max_degree = max(max_degree, 1)  # x without exponent means degree 1
        
        return True
    except:
        return False  # If there's an error in processing, it's not a polynomial

# Game loop
def polynomial_game():
    print("Welcome to the Polynomial Checker Game!")
    print("Enter an expression, and I'll tell you if it's a polynomial.")
    print("Type 'exit' to quit.")
    
    while True:
        expression = input("Enter an expression: ")
        
        if expression.lower() == "exit":
            print("Thanks for playing! Goodbye!")
            break
        
        if is_polynomial(expression):
            print("Yes! This is a polynomial expression.\n")
        else:
            print("No! This is NOT a polynomial expression.\n")

# Run the game
if __name__ == "__main__":
    polynomial_game()
