import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, np.nan, 28, 'unknown'],
    'Salary': [50000, 60000, 75000, np.nan, 90000],
    'Join_Date': ['2020-01-15', '2019-05-20', '2018-08-10', np.nan, '20220201'],
    'Department': ['HR', 'IT', 'Finance', 'Sales', 'Marketing']
}
df=pd.DataFrame(data)
df.iloc[1,2]=''
df.iloc[2, 3] = 'wrong_format'
df.iloc[3, 4] = 'Sales'
df.iloc[4, 0] = 'Bob'  # Incorrect name

df.to_csv("example.csv", index=False)

# print(df.to_string())

df=pd.read_csv('example.csv')
# replace salary w mean salary
# replace bob with david
# express dates in correct format
# insert bobs age by removing wrong format
x=df['Salary'].mean()

df['Salary'].fillna(int(x),inplace=True)

mean_age=int(np.ceil((25+30+28)/3))
df.iloc[2,1]=mean_age
df.iloc[4,1]=mean_age

df.iloc[2,3]='NaN'
df.iloc[4,3]=pd.to_datetime(df.iloc[4,3]).strftime('%Y-%m-%d')

df.iloc[4,0]=df.iloc[4,0].replace('Bob', 'Eve')

print(df)