import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Alice', 'Bob'],
'Age': [12, 13, 12, 13, 12, 13],
'TestScore': [85, 90, 88, 92, 89, 94]}
df=pd.DataFrame(data)
print("Original DatFrame:")
print(df)
total_scores= df.groupby('Age')['TestScore'].sum()
print("\nTotal Test Score by Age:")
print(total_scores)
