import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import os

#add file path
file_path =  r'C:\Users\DELL\Desktop\Task1 for internship\data.csv'
df = pd.read_csv(file_path)

#check for missing values
print(df.isnull().sum())

#handling missing values using drop
df = df.dropna()

#get the duplicates
print("Number of duplicates: ", df.duplicated().sum())

#remove duplicates
df = df.drop_duplicates()

#explore outliers
#box plot for outlier detection
sns.boxplot(data = df)


#remove outliers using z-score
from scipy.stats import zscore
z_scores = zscore(df.select_dtypes(include=[np.number]))
abs_z_scores = np.abs(z_scores)
df_no_outliers = df[(abs_z_scores < 3).all(axis= 1)]

#save the cleaned dataset
df.to_csv('cleaned_dataset.csv', index=False)

#view the cleaned data
cleaned_df = pd.read_csv('cleaned_dataset.csv')
