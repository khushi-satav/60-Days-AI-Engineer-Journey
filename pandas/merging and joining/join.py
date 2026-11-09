import pandas as pd

data1 = {
    "name": ["Ram", "Khushi", "Raj", "Shyam"]
}

data2 = {
    "salary": [20000, 30000, 40000, 50000]
}

df1 = pd.DataFrame(data1, index=[1, 2, 3, 4])
df2 = pd.DataFrame(data2, index=[1, 2, 3, 4])

print(df1)
print(df2)
result = df1.join(df2)

print(result)