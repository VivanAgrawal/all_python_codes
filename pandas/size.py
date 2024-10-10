data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Alice', 'Bob'],
'Age': [12, 13, 12, 13, 12, 13],
'TestScore': [85, 90, 88, 92, 89, 94]}

df=pd.DataFrame(data)
print("Original DataFrame:")
print(df)
entry_counts=df.groupby('Name').size()
print("\nNumber of Entries by Name:")
print(entry_counts)