import pandas as pd

data={
    "name":['ram','khushi','raj'],
    "age":[12,56,8],
    "city":['indore','aaahu','ratlam']
}
df=pd.DataFrame(data)
df.sort_values(by=["age","city"],ascending=[True,False],inplace=True)
print("sorte in descending")
print(df)