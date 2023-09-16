# Creating a DataFrame:

import pandas as pd

# Create a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40]}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)


# Reading Data from a CSV File:

import pandas as pd

# Read data from a CSV file
df = pd.read_csv('data.csv')

# Display the first few rows of the DataFrame
print(df.head())

# Data Selection and Filtering:

# Select and filter rows based on a condition
young_people = df[df['Age'] < 35]

# Display the filtered DataFrame
print(young_people)


# Basic Data Aggregation:

# Calculate the average age
average_age = df['Age'].mean()

# Display the average age
print("Average age:", average_age)


# Sorting Data:

# Sort the DataFrame by age in descending order
df_sorted = df.sort_values(by='Age', ascending=False)

# Display the sorted DataFrame
print(df_sorted)


#  Grouping and Aggregation:

# Group the data by age and calculate the count in each group
age_groups = df.groupby('Age').size()

# Display the grouped data
print(age_groups)


# Adding and Removing Columns:

# Add a new column to the DataFrame
df['Salary'] = [50000, 60000, 70000, 80000]

# Display the DataFrame with the new column
print(df)

# Remove a column from the DataFrame
df = df.drop('Salary', axis=1)

# Display the DataFrame after removing the column
print(df)


# Handling Missing Data:

# Fill missing values with a specific value (e.g., 0)
df_filled = df.fillna(0)

# Display the DataFrame with filled missing values
print(df_filled)

# Merging DataFrames:

# Merge two DataFrames based on a common column
data1 = {'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']}
data2 = {'ID': [2, 3, 4], 'Age': [25, 30, 35]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

merged_df = pd.merge(df1, df2, on='ID', how='inner')

# Display the merged DataFrame
print(merged_df)
