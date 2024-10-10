import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)

# Slicing rows to select the first two rows
first_two_rows = df[:2]

print("Original DataFrame:")
print(df)

print("\nFirst Two Rows:")
print(first_two_rows)