# -*- coding: utf-8 -*-
"""hackathon.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1a_IojaNtuifuUdTNfi1yTWbRfVh0_O-o
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load your data (replace with your actual file path)
data = pd.read_csv('/content/MTA_Express_Bus_Capacity__April_2023_-_September_2023_20241128.csv')

# Encode categorical variables
encoder = OneHotEncoder(drop='first', sparse_output=False) # Set sparse_output=False
categorical_features = encoder.fit_transform(data[['Day Type', 'Borough', 'Route', 'Direction']])

# Scale numeric features
scaler = StandardScaler()
data['Load Percentage'] = data['Load Percentage']*data['Trips with APC']
data.drop('Trips with APC',axis=1,inplace=True)
numeric_features = scaler.fit_transform(data[['Hour', 'Load Percentage']])

# Combine encoded and scaled features
X = np.hstack([categorical_features, numeric_features])




# Perform K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
data['Cluster'] = kmeans.fit_predict(X)

crowded_hours = data.groupby(['Route', 'Hour'])['Load Percentage'].mean().reset_index()

# Sort the data by 'Route' and 'Load Percentage' to find the most crowded hours
crowded_hours = crowded_hours.sort_values(by=['Route', 'Load Percentage'], ascending=[True, False])

# Display the result


most_crowded_hours = crowded_hours.loc[crowded_hours.groupby('Route')['Load Percentage'].idxmax()]

# Display the result




# Create a pivot table for visualization
pivot_table = crowded_hours.pivot_table(values='Load Percentage', index='Hour', columns='Route')

# Plot the data
plt.figure(figsize=(12, 6))
pivot_table.plot(kind='line', marker='o')
plt.title('Average Load Percentage for Each Hour and Bus Route')
plt.xlabel('Hour of the Day')
plt.ylabel('Average Load Percentage')
#plt.legend(title='Bus Route')
plt.grid(True)
plt.show()

from google.colab import drive
drive.mount('/content/drive')



import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import numpy as np

# Load your data (replace with your actual file path)
data = pd.read_csv('/content/MTA_Express_Bus_Capacity__April_2023_-_September_2023_20241128.csv')

# Encode categorical variables
encoder = OneHotEncoder(drop='first', sparse_output=False) # Set sparse_output=False
categorical_features = encoder.fit_transform(data[['Day Type', 'Borough', 'Route', 'Direction']])

# Scale numeric features
scaler = StandardScaler()
numeric_features = scaler.fit_transform(data[['Hour', 'Load Percentage', 'Trips with APC']])

# Combine encoded and scaled features
X = np.hstack([categorical_features, numeric_features])
display(X)