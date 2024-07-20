#!/usr/bin/env python
# coding: utf-8

# #  Exploratory Data Analysis(EDA)

# In[1]:


#Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[2]:


#Loading the dataset 
mpg_df=pd.read_csv('D:\\Tsed\\Python\\Projects\\Mile Per Gallon\\Dataset\\mpg.csv')
mpg_df.head(3)


# ## 2. Data Cleaning

# ### 2.1 Handling missing values:  
# 

# In[3]:


# detecting null values in horsepower
mpg_df.isna().sum()


# In[4]:


# Calculating the threshold (5%) missing value is tolerable to drop them out
threshold=len(mpg_df)*0.05
print('Minimum threshold value:',threshold)
print('Number of missing horsepower values:', mpg_df['horsepower'].isna().sum())


# In[5]:


# lets print the missing values out
mpg_df[mpg_df['horsepower'].isna()]


# #### INSIGHT:
#     :number of missing value(6) is less than the threshold value(19.9).So we can drop them out

# In[6]:


# Dropping the missing values
mpg_df.dropna(inplace=True)
mpg_df.tail(3)


# #### INSIGHTS: 
#     : The index is still up to 397. Cross checking if the missing values is removed. 
#     : If they have been removed, we have to reset the index

# In[7]:


# Cross checking if the missing values is removed
mpg_df.isna().any().sum()


# In[8]:


# Resetting the index to remove empty rows
mpg_df.reset_index(inplace=True)


# In[9]:


# Drop index column of the original data 
mpg_df.drop('index',axis=1,inplace=True)


# In[10]:


# Cross checking if it the empty rows are removed
mpg_df.tail(3)


# #### INSIGHTS: 
#      We are good to go!

# ### 2.2. Formatting & standardizing 

# In[11]:


# Standardizing & Converting data types into the proper format
mpg_df['weight']=mpg_df['weight'].astype(float)
mpg_df['model_year']=mpg_df['model_year']+1900
#mpg_df['model_year']=pd.to_datetime(mpg_df['model_year'],errors='coerce').dt.year
print(mpg_df['weight'].dtype)
mpg_df.sample(3)


# ### 2.3 Generating new feature from model year

# In[12]:


# Generating new feature from model_year column called age
mpg_df.insert(6,'age',datetime.now().year-mpg_df['model_year'])
mpg_df.sample(3)


# ### 2.4 Handling Outliers

# In[25]:


upper_threshold={}
lower_threshold={}

for i in mpg_df.select_dtypes('number').columns:
    upper_threshold[i]=(mpg_df[i].quantile(0.75)+(1.5*(mpg_df[i].quantile(0.75)-mpg_df[i].quantile(0.25))))
    lower_threshold[i]=(mpg_df[i].quantile(0.25)-(1.5*(mpg_df[i].quantile(0.75)-mpg_df[i].quantile(0.25))))

outliers_dfs=outliers_df.append(upper_threshold,ignore_index=True,)
outliers_dfss=outliers_dfs.append(lower_threshold,ignore_index=True)

outliers_dfss.index=['min','Q1','Q2','Q3','max','upper_threshold','lower_threshold']

print('INSGIHTS: The data has taken for ',mpg_df['model_year'].nunique(),' model years')
print('From',mpg_df['model_year'].min(),'To',mpg_df['model_year'].max())
outliers_dfss.iloc[:,:]


# INSIGHTS: 
# 
#           :For categorical variable outlier theshold values shouldnt be used eg: cylinders column the thresholds doesnt make 
# 
#           sense there couldnt be vehicles with -2 or 14 cylinders.
# 
#           : The upper threshold value of horsepower is lower than the max value of hp so there is outlier
#           
#           : There is outliers in acceleration explanatory variable in both direction

# In[34]:


print('number of outliers above threshold:',len(mpg_df[mpg_df['horsepower']>202.5]))
mpg_df[mpg_df['horsepower']>202.5]


# In[62]:


#mpg_df[mpg_df.duplicated('name')]['name'].value_counts()


# In[73]:


#print('Number of outliers above& below threshold:',len((mpg_df[(mpg_df['acceleration']>21) | (mpg_df['acceleration']<8.9)])))
print('Total number of outliers:',len(mpg_df[((mpg_df['acceleration']>21) | (mpg_df['acceleration']<8.9) )|(mpg_df['horsepower']>202.5)]))
outliers=mpg_df[((mpg_df['acceleration']>21) | (mpg_df['acceleration']<8.9) )|(mpg_df['horsepower']>202.5)]
outliers


# Let's remove these outliers

# In[77]:


mpg_df_cleaned=mpg_df.drop(outliers.index)
mpg_df_cleaned


# In[ ]:




