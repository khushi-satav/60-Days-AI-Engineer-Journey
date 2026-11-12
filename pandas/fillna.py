#replce null value irh specifiic value
#drop ad remoove row wirh null value
import pandas as pd

df = pd.read_csv("pandas/pandas_practice_100_rows.csv")

print(df.head())

#find replace null
resDF=df.fillna(1111)
print(resDF.to_string())