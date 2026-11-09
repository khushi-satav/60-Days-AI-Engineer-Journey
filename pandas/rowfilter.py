import pandas as pd

data = {
    "name": ['ram', 'shyam', 'ghoa', 'ash', 'uv', 'hj', 'asn', 'khushi', 'kch'],
    "age": [41, 23, 5, 3, 5, 5, 5, 66, 9],
    "salary": [2000, 21321, 454, 5464, 546, 898, 46341543, 232, 8989]
}

df = pd.DataFrame(data)
high_salary=df[df['salary']>50000]
print('employee wirh salary >50000')
print(high_salary)