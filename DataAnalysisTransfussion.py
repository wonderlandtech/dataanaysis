#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from spellchecker import SpellChecker


# In[7]:


spell = SpellChecker()
mispell = spell.unknown(['let', 'us', 'wlak','on','the','groun'])

for word in mispell:
    print(spell.correction(word))
    print(spell.candidates(word))


# In[10]:


df = pd.read_csv('transfusion.csv')
df


# In[15]:


ok = df[['Recency (months)','Frequency (times)']]
x = ok.loc[738:748]
x


# In[16]:


import matplotlib.pyplot as plt


# In[18]:


x


# In[20]:


x.plot(kind='hist')


# In[22]:


x.plot(kind='bar')


# In[23]:


x.plot(kind='line')


# In[27]:


x['Recency (months)'].plot()
plt.show()


# In[32]:


df['Recency (months)'].plot()
plt.show()


# In[56]:


x.plot.scatter(figsize=(10, 8), x = 'Recency (months)', y = 'Frequency (times)', alpha=0.7)


# In[55]:


df.plot(kind='box', figsize=(20, 8))


# ## ASSIGNMENT
# 
# 1. Get a dataset
# 2. Perform Datacleaning by checking for null values
# 3. get a subset of 20 rows using loc
# 4. Plot a graph of  4 columns
# 5. show relationship between two columns using scatter plot
# 6. what can you derive from your relationship of num(5) above
# 
# ##### SUBMITTED BEFORE 7:00PM WAT on TUESDAY

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




