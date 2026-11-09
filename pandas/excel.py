import pandas as pd

df = pd.read_excel("pandas/SampleSuperstore.xlsx", engine="xlrd")

print(df)