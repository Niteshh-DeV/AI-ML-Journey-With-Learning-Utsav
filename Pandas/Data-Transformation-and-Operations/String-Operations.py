import pandas as pd 

# String Operations in Pandas
# Pandas provides a variety of string handling functions that can be applied to Series and DataFrame
# We use .str accessor to access string methods for Series

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'email': ['alice@gmail.com', 'bob@gmail.com', 'charlie@gmail.com','david@gmail.com', 'eve@gmail.com']
} # String Data

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Converting to Lowercase

df_lower = df['Name'].str.lower() # Convert all names to lowercase
print("\nNames in Lowercase:\n", df_lower)

# Uppercase
df_upper = df['City'].str.upper() # Convert all city names to uppercase
print("\nCity Names in Uppercase:\n", df_upper)

# Length of Strings in Series
df_name_length = df['Name'].str.len() # Get the length of each name
print("\nLength of Each Name:\n", df_name_length)

# Contains
df_contains = df['email'].str.contains('@gmail.com') 
print("\nEmails containing '@gmail.com':\n", df_contains)

# Replace 
df_replaced = df['City'].str.replace('o', '0') # Replace 'o' with '0' in city names
print("\nCity Names after Replacing 'o' with '0':\n", df_replaced)

# Extract
df_extracted = df['email'].str.extract(r'(@\w+\.\w+)') # Extract domain from email addresses .
# (r'(@\w+\.\w+)') is a regular expression pattern that matches the domain part of an email address.
print("\nExtracted Domains from Emails:\n", df_extracted)

# Split 
df_split = df['email'].str.split('@', expand=True) # Split email addresses into username and domain 
# expand=True returns a DataFrame with separate columns for username and domain
print("\nSplit Emails into Username and Domain:\n", df_split)