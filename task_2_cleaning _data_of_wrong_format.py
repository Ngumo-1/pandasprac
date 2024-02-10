'''
Identify and correct any outliers in a numerical
column by replacing them with a sensible value,
such as the median.
'''

import numpy as np
import pandas as pd

data={"values": [20,30,35,500,50,70,60,80,57,62]}
df=pd.DataFrame(data)
print(df.to_string())
# mediann=np.median(df["values"])
mediann=df["values"].median()
print('\n')
print(mediann)
print("\n")
#loc below takes in row_index and column_index
df.loc[df["values"]>100, "values"]=mediann

print(df.to_string())