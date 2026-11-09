import pandas as pd
data={
    "name":['ram','khushi','raj'],
    "age":[12,56,8],
    "city":['indore','aaahu','ratlam']
}
df=pd.DataFrame(data)
print(df)
#save in csv file
#df.to_csv("output.csv",index=False)

#save in excelfile
#df.to_excel("pandas/output.xlsx", index=False)

#json
df.to_json("out.json")
