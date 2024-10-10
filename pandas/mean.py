import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Alice', 'Bob'],
        'Age': [12, 13, 12, 13, 12, 13],
        'TestScore': [85, 90, 88, 92, 89, 94]}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
# Grouping by 'Name' and calculating the mean test score
mean_scores = df.groupby('Name')['TestScore'].mean()
print("\nMean Test Scores by Name:")
print(mean_scores)