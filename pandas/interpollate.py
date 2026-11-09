# Interpolation is a method used to estimate and fill missing values
# in a dataset based on existing values.
# In Pandas, we use the interpolate() method.


import pandas as pd

data = {
    "marks": [10, 20, None, 40, 50]
}

df = pd.DataFrame(data)

print(df)
df.interpolate(inplace=True)

print(df)