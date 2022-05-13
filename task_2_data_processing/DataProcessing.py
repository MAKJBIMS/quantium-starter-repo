"""
Following code merges transaction data for Soul Foods’s entire morsel line from 3 csv files into single file. Data from 3 csv files is filtered based on product named "Pink Morsels". Total sales for a given day is calculated using price and quantity data. Finally Sales,Date and Region data from 3 csv files is merged into a single csv file named "merged_daily_sales_data.csv".
"""

import pandas as pd

# Read data from csv file
daily_sales_data_0 = pd.read_csv('../data/daily_sales_data_0.csv', parse_dates=['date'], index_col="product")
daily_sales_data_1 = pd.read_csv('../data/daily_sales_data_1.csv', parse_dates=['date'], index_col="product")
daily_sales_data_2 = pd.read_csv('../data/daily_sales_data_2.csv', parse_dates=['date'], index_col="product")


# Function filters out sales data of "pink morsel" for all regions
def data_processing(daily_sales):
    daily_sales = daily_sales.loc["pink morsel"]
    # Copy of a dataframe created to avoid chained assignment warnings / exceptions
    daily_sales_copy = daily_sales.copy()
    daily_sales_copy.loc[:, 'price'] = daily_sales_copy.price.apply(lambda row: row.strip('$')).astype(float)
    # Calculating total sales for a given day by multiplying price and quantity
    daily_sales_copy.loc[:, 'sales'] = daily_sales_copy.apply(lambda row: (row['price'] * row['quantity']), axis=1)
    daily_sales_copy = daily_sales_copy[['sales', 'date', 'region']]
    return daily_sales_copy


# Merge data into single file
daily_sales_data = data_processing(daily_sales_data_0)
daily_sales_data = pd.concat([daily_sales_data, data_processing(daily_sales_data_1)])
daily_sales_data = pd.concat([daily_sales_data, data_processing(daily_sales_data_2)])

daily_sales_data.to_csv('merged_daily_sales_data.csv', index=False)
