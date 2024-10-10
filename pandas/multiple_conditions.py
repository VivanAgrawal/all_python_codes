import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)

# Filtering using the isin method (selecting rows with specific cities)
selected_cities = df[df['City'].isin(['New York', 'Los Angeles'])]

print("Original DataFrame:")
print(df)

print("\nSelected Cities (New York or Los Angeles):")
print(selected_cities)