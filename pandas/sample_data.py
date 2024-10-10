import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Alice', 'Bob'],
'Age': [12, 13, 12, 13, 12, 13],
'TestScore': [85, 90, 88, 92, 89, 94]}

df=pd.DataFrame(data)
print("original DataFrame:")
print(df)

mean_scores= df.groupby('Name')['TestScore'].mean()
print("\nMean TestScore by Name:")
print(mean_scores)