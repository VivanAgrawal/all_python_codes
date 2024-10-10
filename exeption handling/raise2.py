try:
    # Some code that might raise an exception
    x = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    # Handle the exception or add additional information
    print("A division by zero error occurred.")
    raise  # Re-raise the same exception
except Exception as e:
    # Handle other exceptions
    print(f"An exception occurred: {e}")
else:
    # Code to execute if no exceptions were raised
    print("No exceptions were raised.")
finally:
    # Cleanup code that always executes
    print("This will always be executed.")