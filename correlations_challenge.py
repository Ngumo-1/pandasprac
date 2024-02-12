import pandas as pd
import numpy as np
from correlations import checking_correlations

'''
Write a program to identify the top N correlated 
pairs of columns in a DataFrame, where N is a 
user-defined value.'''

data = {
    'Temperature': [25, 30, 35, 40, 45],
    'Humidity': [50, 55, 60, 65, 70],
    'Pressure': [1000, 950, 900, 850, 800],
    'Wind_Speed': [10, 15, 20, 25, 30],
    'Cloud_Cover': [20, 30, 40, 50, 60]
}

def calculate_correlations(df):
    correlation_matrix = df.corr()
    return correlation_matrix

def top_correlated_pairs(df,n):
    correlations=checking_correlations(df).abs()
    np.fill_diagonal(correlations.values, np.nan)
    sort_correlations=correlations.unstack().sort_values(ascending=False)
    return_n_pairs=sort_correlations.dropna().head(n).index.to_list()
    top_related_n_pairs_with_corr=[(pair[0], pair[1], correlations.loc[pair]) for pair in return_n_pairs]
    return top_related_n_pairs_with_corr


# Sample DataFrame
data = {
    'Temperature': [25, 30, 35, 40, 45],
    'Humidity': [50, 55, 60, 65, 70],
    'Pressure': [1000, 950, 900, 850, 800],
    'Wind_Speed': [10, 15, 20, 25, 30],
    'Cloud_Cover': [20, 30, 40, 50, 60]
}
df = pd.DataFrame(data)

n = int(input("Enter N to return top N correlated pairs of columns in a DataFrame: "))
top_pairs = top_correlated_pairs(df, n)
# print(top_pairs)

print(f"Top {n} Correlated Pairs:")
for pair in top_pairs:
   print(pair)