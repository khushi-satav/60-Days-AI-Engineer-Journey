import pandas as pd

data = {
    "name": ['ram', 'shyam', 'ghoa', 'ash', 'uv', 'hj', 'asn', 'khushi', 'kch'],
    "age": [41, 23, 5, 3, 5, 5, 5, 66, 9],
    "salary": [2000, 21321, 454, 5464, 546, 898, 46341543, 232, 8989]
}
df=pd.DataFrame(data)

print (df)
df["Bonus"]=df['salary']*0.1
print(df)
#using insert method
#df.insert(loc,"column_name",sone_data)
df.insert(0,"employee id",[10,20,56,0,5,556,5,9,00])
print(df)