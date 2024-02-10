import pandas as pd
import numpy as np
'''Question:

Load a dataset and find the correlation between 
two specific columns. Interpret the correlation 
value.'''


data = {
    'Income': [50000, 60000, 70000, 80000, 90000],
    'Expenditure': [25000, 28000, 30000, 35000, 40000],
    'Savings': [25000, 32000, 40000, 45000, 50000]
}

def checking_correlations(df):
    return df.corr()

df = pd.DataFrame(data)
results=checking_correlations(df)
print(results)
'''
Each column has a 1.0  correlation with itself
The columns have positive correlations as evidenced
by correlation values of 0.9.
This means that when value of one column goes up
then the value of the other column goes up too'''
