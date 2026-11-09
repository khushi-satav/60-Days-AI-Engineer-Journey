import pandas as pd

data = {
    "name": ['ram', None, 'ghoa', 'ash', 'uv', 'hj', 'asn', 'khushi', 'kch'],
    "age": [41, None, 5, 3, 5, 5, 5, 66, 9],
    "salary": [2000, None, 454, 5464, 546, 898, 46341543, 232, 8989]
}
df=pd.DataFrame(data)
print(df)

df.dropna(inplace=True)
print(df)