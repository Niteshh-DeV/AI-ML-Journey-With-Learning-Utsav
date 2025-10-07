import pandas as pd

# Saving and Exporting Data in Pandas

# Sample Data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [24, 27, 22, 32, 29],
    'Score': [85, 90, 78, 92, 88],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Saving to CSV (Comma-Separated Values)
df.to_csv('data.csv', index=False) # index=False to avoid writing row indices
print("\nDataFrame saved to 'data.csv'")

# Saving to Excel
df.to_excel('data.xlsx', index=False) # Requires openpyxl or xlsxwriter
print("\nDataFrame saved to 'data.xlsx'")

# Saving to JSON (JavaScript Object Notation)
df.to_json('data.json', orient='records', lines=True) # Each record in a new line
print("\nDataFrame saved to 'data.json'")

# Saving to HTML
df.to_html('data.html', index=False) # Saves DataFrame as an HTML table
print("\nDataFrame saved to 'data.html'")

# Reading back the saved files to verify
df_csv = pd.read_csv('data.csv')
print("\nDataFrame read from 'data.csv':\n", df_csv)

df_excel = pd.read_excel('data.xlsx')
print("\nDataFrame read from 'data.xlsx':\n", df_excel)

df_json = pd.read_json('data.json', orient='records', lines=True)
print("\nDataFrame read from 'data.json':\n", df_json)

df_html = pd.read_html('data.html')[0] # read_html returns a list of DataFrames
print("\nDataFrame read from 'data.html':\n", df_html)
# [0] to get the first table