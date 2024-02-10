import pandas as pd
import numpy as np

'''Question:

You have a DataFrame containing a 'Price' column, 
but some values are negative due to errors. 
Write a program to replace negative prices with 
the absolute values.'''

def removing_negative_values(df, column_name):
    df_copy=df.copy()
    df_copy[column_name]=np.absolute(df_copy[column_name])
    return df_copy

df=pd.DataFrame({"Price":[80000, 12000, -3000,45000, 500, -1000]})
fixed_values=removing_negative_values(df, "Price")
print(fixed_values.to_string())