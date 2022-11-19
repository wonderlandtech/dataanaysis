#!/usr/bin/env python
# coding: utf-8

# # PANDAS

# In[7]:


#this is a python library that is used for working with data sets. It has functions for analysing and exploring, 
#clearing and manipulating  of datas. Pandas is useful and important because it is used for ananlysing of big data's and
#make conclusion based on statistical theories.


# In[8]:


import pandas as pd


# In[9]:


#SERIES is just one column
student  = pd.Series(['tomiwa','ade','lola', 'bayo'])
gender = pd.Series(['Female','Male','Female','Male'])
matric = pd.Series(['Hcsf/20/0020','Hcsf/20/0021','Hcsf/20/0022','Hcsf/20/0023'])

#Usng print statement
print(student)
print(gender)
print(matric)


# In[10]:


student_data = pd.DataFrame({'student':student, 'gender':gender,'matric':matric})
student_data


# In[11]:


#IMPORT DATA IN JUPYTER NOTEBOOK


# In[12]:


student_grade = pd.read_csv('Studentdata.csv')
student_grade


# In[13]:


student_grade.head(30)


# In[14]:


#last 30 rows
student_grade.tail(30)


# In[15]:


student_grade.describe()


# In[16]:


student_grade.groupby(['Name']).mean()


# In[17]:


for Karim in student_grade['Name']:
    if Karim == 'Karim':
          Karim.count('Karim')
        #print('Karim')
   
  


# In[18]:


x = student_grade['Name'] =='Karim'
x.sum()


# In[19]:


student_grade['newDate'] = student_grade['Day'] + ', ' + student_grade['Date']
student_grade


# In[20]:


z = student_grade[['Day', 'newDate']]
z


# In[21]:


student_grade.drop('Day',axis = 1,inplace=True)
student_grade


# In[22]:


#student_grade['Date'] = student_grade.drop('Date', axis=1)
student_grade


# In[23]:


student_grade


# In[30]:


data = student_grade['weekend'].fillna(student_grade['weekend'].mean(), inplace=True)
student_grade


# In[32]:


#student_grade['Your gender?'].tail(30)


# In[33]:


#Note - Once there is space its not gonna work

student_grade.weekend


# In[ ]:


#SUM
student_grade.weekend.sum() 


# In[ ]:


#AVERAGE
#NOTE MEAN IS THE AVERAGE
student_grade.weekend.mean()


# In[ ]:


student_grade.weekend.mode()


# In[ ]:


student_grade.weekend.max()


# In[ ]:


student_grade.weekend.std()


# In[ ]:


student_grade.weekend.median()


# In[ ]:


student_grade['study hour'].tail(50)


# In[ ]:


fifa19 = pd.read_csv('fifa19.csv')
fifa19


# In[ ]:


fifa19.columns


# In[ ]:


#Using the sort_values to sort the dataset 
fifa19.sort_values(by='Age', ascending=False).head(10)


# In[ ]:


# fifa19[fifa19['Nationality', 'Age']].head(10)
fifa19[fifa19['Nationality']=='Mexico']


# In[ ]:


fifa19['Nationality']=='Mexico'


# In[ ]:


fifa19.columns


# In[ ]:


fifa19.Club


# In[ ]:


fifa19[fifa19['Club']=='Manchester United']


# In[ ]:


fifa19.drop('Unnamed: 0', axis=1, inplace=True)


# In[ ]:


fifa19


# In[ ]:


fifa19['Release Clause'].dtypes


# In[ ]:


fifa19.sort_values(by='Release Clause', ascending=False).head(1)


# ### Handling Missing Data

# In[ ]:


## DATA CLEANING

fifa19.isnull().sum()


# In[ ]:


# we can fill the null value with the mean of the entire data
#all null values will be replace by the mean


# In[ ]:


fifa19[fifa19['GKHandling'].isnull()]


# In[ ]:


fifa19.fillna(fifa19.mean(), inplace=True)

fifa19.isnull().sum()


# In[ ]:


#mean will only work for integers not text
fifa19['GKReflexes'].sum()


# ### Removing Currency Symbol

# In[ ]:


#another way of making changes 
fifa19['Release Clause'] = fifa19['Release Clause'].str.replace('€','')
fifa19['Release Clause']


# In[ ]:


fifa19


# In[ ]:


fifa19['Release Clause'] = fifa19['Release Clause'].str.replace('M','')


# In[ ]:


fifa19


# In[ ]:


fifa19['Release Clause'] = fifa19['Release Clause'].str.replace('K','')
fifa19['Release Clause']


# In[ ]:


fifa19['Release Clause'] = fifa19['Release Clause'].astype(float)
fifa19['Release Clause']


# In[ ]:


fifa19['Release Clause'].dtype


# In[ ]:


fifa19['Release Clause'].isnull().sum()


# In[ ]:


fifa19['Release Clause'] = fifa19['Release Clause'].fillna(fifa19['Release Clause'].mean())
fifa19['Release Clause']


# In[ ]:


fifa19['Release Clause'].isnull().sum()


# In[ ]:


fifa19.isnull().sum()


# In[ ]:


import numpy as np


# In[ ]:


x = np([1,2,3,4,5])
x


# In[31]:


import fractions
import numpy as np
a = fractions.Fraction(1/2)
b = fractions.Fraction(1/3)
d = fractions.Fraction(a+b)
print(np.mean(d))


# In[38]:


#tuple
fruit = ('Orange','Mango','Cherry')
print('fruit in tuple ', fruit)
newfruit = list(fruit)
print('fruit now changed to list ', newfruit)

newfruit[2] = 'Apple'
# Converted to list and index 2 changed to Apple
newfruit

# now reconverted to tuple
print(' Fruit Now Converted to tuple ', tuple(newfruit))


# In[46]:


def multipliers(): 
    return (lambda x : i * x for i in range(4))
print (m(2) for m in multipliers())


# In[ ]:




