import pandas as pd

# Working with Date and Time in Pandas
# Pandas provides powerful tools for handling date and time data. The to_datetime() function is commonly used to convert strings or other formats into datetime objects.
# datetime objects are essential for time series analysis and manipulation.

data = {
    'Event': ['Event1', 'Event2'],
    'Date': ['2023-01-01', '2023-03-10']
}  # Sample data with different date formats 
dataframe = pd.DataFrame(data)
print("Original DataFrame:\n", dataframe)

# Converting to datetime
dataframe['Date'] = pd.to_datetime(dataframe['Date'])
print("\nDataFrame after Converting to datetime:\n", dataframe)
print("\nData Types after Conversion:\n", dataframe.dtypes)

# Extracting date components
dataframe['Year'] = dataframe['Date'].dt.year
dataframe['Month'] = dataframe['Date'].dt.month
dataframe['Day'] = dataframe['Date'].dt.day
print("\nDataFrame with Extracted Date Components:\n", dataframe)