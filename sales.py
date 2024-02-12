import pandas as pd
'''Extend the sales dataset challenge by incorporating 
data from external sources. For example, include 
weather data and correlate it with sales to 
analyze if weather conditions impact sales. 
Clean and preprocess the additional data for 
integration.'''

sales_data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
    'Product': ['A', 'B', 'A', 'C', 'B'],
    'Quantity': [100, 150, 120, 80, 200],
    'Revenue': [5000, 7500, 6000, 4000, 10000]
}

sales_df = pd.DataFrame(sales_data)
sales_df["Date"]=pd.to_datetime(sales_df["Date"])
# print(sales_df)

weather_data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
    'Temperature': [25, 30, 35, 40, 45],
    'Humidity': [50, 55, 60, 65, 70],
    'Wind_Speed': [10, 15, 20, 25, 30],
    'Cloud_Cover': [20, 30, 40, 50, 60]
}

weather_df = pd.DataFrame(weather_data)
weather_df["Date"]=pd.to_datetime(weather_df["Date"])


new_df=pd.merge(sales_df, weather_df, on="Date")
correlation_quantity = new_df[['Quantity', 'Temperature', 'Humidity', 'Wind_Speed', 'Cloud_Cover']].corr()['Quantity']
correlation_revenue = new_df[['Revenue', 'Temperature', 'Humidity', 'Wind_Speed', 'Cloud_Cover']].corr()['Revenue']

print("Correlation with Sales Quantity:")
print(correlation_quantity)

print("\nCorrelation with Revenue:")
print(correlation_revenue)
