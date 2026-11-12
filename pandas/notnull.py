import pandas as pd
df = pd.read_csv("pandas/pandas_practice_100_rows.csv")

print(df.head())
#find and replcae not null with true

resDF=df.notnull()
print(resDF.to_string)