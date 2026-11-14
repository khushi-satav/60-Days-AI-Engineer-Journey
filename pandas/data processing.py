import pandas as pd

data = {
    'Name': ['Pavan', 'Kapil', 'Lalit', 'Ishan', 'Om'],
    'Age': [25, None, 44, 23, None],
    'Salary': [50000, 60000, 70000, None, None]
}

df = pd.DataFrame(data)

print("Original Data")
print(df)

print("\nMissing Values")
print(df.isnull().sum())

# Drop
df_drop = df.dropna()
print("\nAfter Drop")
print(df_drop)

# Fill
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

print("\nAfter Fill")
print(df)