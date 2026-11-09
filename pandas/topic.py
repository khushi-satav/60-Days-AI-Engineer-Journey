#how big ur dataset
#what are name of column
#shaoe and columnv
import pandas as pd
data={
    "name":['ram','shyam','ghoa','ash','uv','hj','asn','khushi','kch'],
    "age":[41,23,5,3,5,5,5,66,9],
    "salary":[2000,21321,454,5464,546,898,463,232,8989]
}

df=pd.DataFrame(data)
print(f'shape:{df.shape}')
print(f'Column Name:{df.columns}')