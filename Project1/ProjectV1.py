#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Load the dataset
data = pd.read_csv(r'C:\Users\mohdz\OneDrive\Documents\GitHub\Python-prep\Project1\realtor-data.csv')


# In[3]:


# Display the first few rows of the dataset
print(data.head())


# In[4]:



# Get information about the dataset
print(data.info())


# In[5]:



# Summary statistics
print(data.describe())


# In[6]:


# Check for missing values
print(data.isnull().sum())


# In[7]:


# Drop rows with missing values (if appropriate)
data = data.dropna()

# Impute missing values (if appropriate)
# For numerical columns: data['column_name'].fillna(mean_or_median, inplace=True)
# For categorical columns: data['column_name'].fillna(most_frequent_value, inplace=True)


# In[8]:


# Visualize outliers (e.g., using box plots)
import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(x=data['price'])
plt.show()

# Remove outliers based on a certain criterion (e.g., using z-scores)
from scipy import stats

z_scores = stats.zscore(data['price'])
data = data[(z_scores < 3)]


# In[9]:


# Encoding categorical variables
data = pd.get_dummies(data, columns=['neighborhood'], drop_first=True)

# Scaling numerical features (e.g., using Min-Max scaling or Standardization)
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
data[['square_footage', 'bedrooms', 'bathrooms']] = scaler.fit_transform(data[['square_footage', 'bedrooms', 'bathrooms']])


# In[ ]:




