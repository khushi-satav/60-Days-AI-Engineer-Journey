import pandas as pd

data1 = {
    "emp_id": [1, 2, 3, 4],
    "name": ["Ram", "Khushi", "Raj", "Shyam"]
}

df1 = pd.DataFrame(data1)
data2 = {
    "emp_id": [1, 2, 3, 5],
    "salary": [20000, 50000, 30000, 40000]
}

df2 = pd.DataFrame(data2)
result = pd.merge(df1, df2, on="emp_id")

print(result)