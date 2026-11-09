
import pandas as pd

data={
    "name":['ram','khushi','raj'],
    "age":[12,56,8],
    "city":['indore','aaahu','ratlam']
}
df=pd.DataFrame(data)
print('display the info')
print(df.info())