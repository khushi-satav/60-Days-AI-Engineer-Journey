import pandas as pd

data = {
    "name": ['ram', 'khushi', 'raj', 'shyam', 'riya'],
    "age": [12, 56, 8, 23, 35],
    "salary": [20000, 50000, 15000, 30000, 40000]
}

df = pd.DataFrame(data)
grouped =df.groupby("age")["salary"].sum()
print(grouped)
