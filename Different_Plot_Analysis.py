#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt
import plotly.express as px
from ipywidgets import widgets
from IPython.display import display


# In[97]:


studentName = pd.Series(['Adeyemi','Jude','Lukemon','Tunde'])
studentGrade = pd.Series([2.34,3.45,4.00,3.24])
studentMatric = pd.Series(['HCSF/20/0024','HCSF/20/0034','HCSF/20/0045','HCSF/20/0067'])

print(studentName)
print(studentGrade)
print(studentMatric)


# In[98]:


studentData = pd.DataFrame({'studentName': studentName, 'studentGrade':studentGrade, 'studentMatric':studentMatric})

studentData


# In[99]:


studentData = pd.read_csv('Studentdata.csv')
studentData


# In[100]:


studentData.head(30)


# In[101]:


luke = studentData.tail(30)
luke


# In[102]:


luked = luke.plot(kind="hist")


# In[103]:


breast_cancer = load_breast_cancer()


# In[104]:


print("Feature Names", breast_cancer.feature_names)
print("Target: ", breast_cancer.target_names)
print("Dataset Size", breast_cancer.data.shape)


breast_cancer_df = pd.DataFrame(breast_cancer.data, columns=breast_cancer.feature_names)
breast_cancer_df['Target'] = breast_cancer.target
breast_cancer_df['Target'] = ['Malignant' if typ==0 else 'Benign' for typ in breast_cancer_df['Target']]
breast_cancer_df.head()                                                      


# ## CREATING INDIVIDUAL PLOT

# In[105]:


with plt.style.context(("seaborn","ggplot")):
    color = {"Malignant": "tab:red", "Benign":"tab:green"}
    plt.figure(figsize=(10,5))
    for tumor_typ in breast_cancer_df["Target"].unique():
        plt.scatter(breast_cancer_df[breast_cancer_df["Target"]==tumor_typ]["mean radius"],
                   breast_cancer_df[breast_cancer_df["Target"]==tumor_typ]["mean texture"],
                    c = color[tumor_typ],
                    s=200,
                    alpha = 0.6,
                    label = tumor_typ)
        plt.xlabel("mean radius")
        plt.ylabel("mean texture")
        plt.title("mean radius vs mean texture Scatter Plot")
        plt.legend(title = "Tumor Type", loc="best")


# In[106]:


with plt.style.context(("seaborn","ggplot")):
    avg_radius_per_tumor_typ = breast_cancer_df.groupby(by ="Target").mean()[["mean radius"]]
    
    plt.figure(figsize=(5,5))
    plt.bar(avg_radius_per_tumor_typ.index,
           avg_radius_per_tumor_typ["mean radius"],
           color="tab:blue",
           width=0.6)
    plt.ylabel("mean radius")
    plt.title("Average mean radius per tumor type")


# In[2]:


df = px.data.tips()
fig = px.pie(df, values='tip', names='day', color='day',
             color_discrete_map={'Thur':'lightcyan',
                                 'Fri':'cyan',
                                 'Sat':'royalblue',
                                 'Sun':'darkblue'})
fig.show()


# In[3]:


df = px.data.tips()
fig = px.pie(df, values='tip', names='day',color='day',
            color_discrete_map={'Thur':'lightgreen','Fri':'cyan'}
            )
fig.show()


# In[109]:


text = widgets.Text()
display(text)

def handle_submit(sender):
    print(text.value)
    
text.on_submit(handle_submit)


# In[110]:


btn = widgets.Button(description = "Click ME")

text = widgets.Text()
display(text)
display(btn)
def on_btn_click(b):
    print(''+text.value)
    #print(" Button Clicked")
# call back the function using .on_click method
text.on_submit(handle_submit)
btn.on_click(on_btn_click)


# In[114]:


from ipywidgets import *
from IPython.html.widgets import *


# In[4]:


t = arange(0.0, 1.0, 0.01)

def pltsin(f):
    plt.plot(x,sin(2*pi*t*f))
    plt.show()
    
interact(pltsin, f=(1,10,0.1))


# In[6]:


import numpy as np
import os
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# ## LINE GRAPH

# In[11]:


a = np.array([1,2,3,4,5])

plt.plot(a)
plt.show


# ### ploting two lines in a graph

# In[13]:


a = np.array([1,2,3,4,5])
b = np.array([2,2,1,4,10])

plt.plot(a)
plt.plot(b)
plt.show()


# #### Increase the size of the graph

# In[20]:


plt.figure(figsize = (10,5))
a = np.array([1,2,3,4,5])
b = np.array([2,2,1,4,10])

plt.plot(a)
plt.plot(b)
plt.show()


# ##### changing color of line

# In[22]:


plt.figure(figsize = (10,5))
a = np.array([1,2,3,4,5])
b = np.array([2,2,1,4,10])

plt.plot(a, color='green')
plt.plot(b, color='red')
plt.show()


# In[40]:


plt.figure(figsize = (10,5))
a = np.array([1,2,3,4,5])
b = np.array([2,2,1,4,10])
c = np.array([3,2,4,6,5])

plt.plot(a, color='green', linestyle = '--')
plt.plot(b, color='red')
plt.plot(c,  linewidth=3)

#endevour to put plt.show
plt.show()


# In[55]:


plt.title("Rent Per Month Somehow", fontsize=20, fontweight="bold")
plt.figure(figsize= (10,10))
a = np.array([1,2,3,4,5])
b = np.array([2,2,1,4,10])
c = np.array([3,2,4,6,5])

plt.plot(a, color='green', linestyle = '--', label = "Rent for all")
plt.plot(b, color='red', label = "Rent for Fy")
plt.plot(c,  linewidth=3, label = "Rent for FZ")

#set location of legend
plt.legend(loc = "upper left")
plt.xticks(range(0, len(a)),("", "","","",""))
#endevour to put plt.show
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




