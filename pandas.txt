# Import Pandas
import pandas as pd

# Create a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Basic DataFrame operations
print("Number of rows and columns:", df.shape)
print("Column names:", df.columns)
print("Data types of columns:")
print(df.dtypes)

# Accessing columns and rows
names_column = df['Name']
print("Names column:")
print(names_column)

first_row = df.iloc[0]
print("First row:")
print(first_row)

# Filtering and querying
young_people = df[df['Age'] < 35]
print("People under 35:")
print(young_people)

# Grouping and aggregation
age_groups = df.groupby('Age').size()
print("Grouped by age:")
print(age_groups)

average_age = df['Age'].mean()
print("Average age:", average_age)

# Adding and removing columns
df['Salary'] = [50000, 60000, 70000, 80000]
print("DataFrame with Salary column:")
print(df)

df = df.drop('City', axis=1)
print("DataFrame after dropping City column:")
print(df)

# Handling missing values
data_with_missing = {'A': [1, 2, None, 4],
                     'B': [None, 6, 7, 8]}
df_missing = pd.DataFrame(data_with_missing)

filled_df = df_missing.fillna(0)
print("DataFrame with missing values filled:")
print(filled_df)

# Merging DataFrames
data1 = {'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']}
data2 = {'ID': [2, 3, 4], 'Age': [25, 30, 35]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

merged_df = pd.merge(df1, df2, on='ID', how='inner')
print("Merged DataFrame:")
print(merged_df)

# Reading and writing data from/to files
df.to_csv('data.csv', index=False)
loaded_df = pd.read_csv('data.csv')
print("Loaded DataFrame from CSV:")
print(loaded_df)
