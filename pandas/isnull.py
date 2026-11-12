import pandas as pd

df = pd.read_csv("pandas/pandas_practice_100_rows.csv")

print(df.head())

#find replace null
resDF=df.isnull()
print(resDF.to_string())