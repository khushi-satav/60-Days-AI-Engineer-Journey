#how to explore rows
#head,tail

import pandas as pd

df = pd.read_json("pandas/Sample_Data.json")
print('display 10 row from first')
print(df.head(10))

print('display 10 row from last')
print(df.tail(10))

