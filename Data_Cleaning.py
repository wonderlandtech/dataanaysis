#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[63]:


mydata = pd.read_csv('datalog.csv')
mydata


# In[6]:


mydata.columns


# In[7]:


mydata.values


# In[8]:


mydata.info


# In[9]:


mydata.describe


# In[ ]:


#furst 30 of my data set


# In[11]:


mydata.head(10)


# ## DATA CLEANING

# In[12]:


mydata.loc[110:160]


# In[24]:


calories = mydata['Calories'].loc[118]
calories


# In[22]:


mydata['Calories'].dropna(inplace=True)
mydata.loc[110:118]


# In[19]:


mydata.loc[118]


# In[35]:


mydata.dropna()


# In[37]:


mydata['Calories'].fillna(130, inplace=True)
mydata.loc[118]


# In[39]:


mydata.loc[141]


# In[42]:


x = mydata['Calories'].mean()
x


# In[45]:


mymean = round(x)
mymean


# In[47]:


mydata['Calories'].loc[110:118]


# In[48]:


mydata.dropna()


# In[52]:


caloriesreplace = mydata['Calories']
caloriesreplace


# In[56]:


mycalories = mydata['Calories'].fillna(mymean, inplace=True)
mycalories


# In[58]:


mydata['Calories'].loc[118]


# In[59]:


mydata['Calories'].loc[141]


# In[60]:


mydata['Calories'].median()


# In[61]:


mydata['Calories'].mode()


# In[62]:


mydata


# In[64]:


mydata.head(4)


# In[69]:


fi = round(mydata['Duration'].mean())
fi


# In[71]:


mydata['Duration'].loc[1] = fi
mydata


# In[73]:


#for duplicated Data
mydata.duplicated()


# In[74]:


# DATA CLEANING IS COMPLETE

df = pd.read_csv('https://www.w3schools.com/python/pandas/data.csv.txt')
df

