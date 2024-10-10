
import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)

# Filtering based on a condition (young people with age < 30)
young_people = df[df['Age'] < 30]

print("Original DataFrame:")
print(df)

print("\nYoung People (Age < 30):")
print(young_people)
