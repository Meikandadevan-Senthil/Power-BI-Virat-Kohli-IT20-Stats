#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt # importing required packages
import numpy as np
import pandas as pd
import math 
import seaborn as sns


# In[2]:


import warnings
warnings.filterwarnings('ignore')


# In[3]:


from sklearn.model_selection import train_test_split


# In[4]:


from sklearn.linear_model import LinearRegression


# In[5]:


from sklearn.metrics import accuracy_score,r2_score,mean_squared_error


# In[6]:


virat = pd.read_csv("D:/Datasets/virat.csv") # loading dataset 


# In[7]:


virat.head() # preprocessing the data


# In[8]:


virat.info()


# In[9]:


virat.columns


# In[10]:


virat = virat[['Runs', 'Mins', 'BF', '4s', '6s', 'SR', 'Position',
       'Dismissal','Start Date','Opposition','Ground']]


# In[11]:


virat.head()


# In[12]:


virat = virat.dropna()


# In[13]:


virat.info()


# In[14]:


virat['Dismissal'].unique()


# In[15]:


virat['Dismissal'] = virat['Dismissal'].replace(to_replace=['not out', '-', 'bowled', 'caught', 'lbw', 'run out', 'stumped'],value=[1,0,0,0,0,0,0])


# In[16]:


virat['4s'].unique()


# In[17]:


virat['4s'] = virat['4s'].replace(to_replace='-',value='0')


# In[18]:


virat['4s'] = pd.to_numeric(virat['4s'])


# In[19]:


virat['6s'] = virat['6s'].replace(to_replace='-',value='0')


# In[20]:


virat['6s'] = pd.to_numeric(virat['6s'])


# In[21]:


virat['Mins'] = virat['Mins'].replace(to_replace='-',value='0')


# In[22]:


virat['Mins'] = pd.to_numeric(virat['Mins'])


# In[23]:


virat['BF'] = virat['BF'].replace(to_replace='-',value='0')


# In[24]:


virat['BF'] = pd.to_numeric(virat['BF'])


# In[25]:


virat['SR'] = virat['SR'].replace(to_replace='-',value='0')


# In[26]:


virat['SR'] = pd.to_numeric(virat['SR'])


# In[27]:


virat['Position'] = virat['Position'].replace(to_replace='-',value='0')


# In[28]:


virat['Position'] = pd.to_numeric(virat['Position'])


# In[29]:


virat['Runs'].unique()


# In[30]:


runs = virat['Runs']


# In[31]:


Run = []
for i in runs:
    i = i[0:2]
    Run.append(i)


# In[32]:


virat['Run'] = Run


# In[33]:


virat['Run'] = virat['Run'].replace(to_replace=['DN','TD','2*'],value=['0','0','2'])


# In[34]:


virat['Run'] = pd.to_numeric(virat['Run'])


# In[35]:


start_date = virat['Start Date']


# In[36]:


year = []
for i in start_date:
    i = i[7:]
    year.append(i)


# In[37]:


virat['year'] = year


# In[38]:


virat['year'] = pd.to_numeric(virat['year'])


# In[39]:


virat = virat.drop(columns=['Runs','Start Date'])


# In[40]:


virat.to_csv("D:/Cricket/Orange_data/T20/ViratT20.csv",index = False)


# In[40]:


virat = pd.get_dummies(virat,prefix=None)


# In[41]:


virat.info()


# In[43]:


virat.to_csv("D:/Cricket/T20/Virat_T20.csv",index = False)


# In[158]:


columns = virat.columns
columns


# In[ ]:




