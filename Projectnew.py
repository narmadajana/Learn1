#!/usr/bin/env python
# coding: utf-8

# In[21]:


import numpy as np
import pandas as pd
from pandas import Series
from pandas import DataFrame
import seaborn as sns
import matplotlib.pyplot as plt


# In[68]:


dfo = pd.read_csv('vgsales.csv')
dfo.head()


# In[71]:


## dfo is our original data set before cleaning.
dfo
dfo.dtypes


# In[73]:


np.count_nonzero(dfo.isnull())        


# In[92]:


### All null values are dropped to clean the dataframe. 329 rows are removed here.
dfc=dfo.dropna().reset_index()
dfc


# In[93]:


### Dropping duplicate rows.Looks like no row is duplicated here.
dfc.drop_duplicates(inplace = True)
dfc


# In[95]:


## Converting Year data type to integer 
dfc['Year'] = dfc['Year'].astype(int)
dfc = df
df


# In[96]:


### Sales data for each Genre
df1=df.groupby('Genre')
df1


# In[97]:


##Sales details for Racing Games
racing = df1.get_group('Racing') .reset_index()
racing


# In[132]:


## Bar Plot showing Sales of Racing genre of games in each year

plt.figure(figsize=(15, 10))
sns.countplot(racing, x="Year")
plt.xticks(rotation=90)
plt.title= ('Count of Racing Games Sold in each Year')


# In[46]:


## which Genre of games were released the most? Action was the most popular genre
df['Genre'].value_counts()


# In[139]:


## Which genre of games made the maximum amount of sales in Million? Action is the clear winner in terms of global sales.
gen = df.groupby(by=['Genre'])['Global_Sales'].sum()
gen = gen.reset_index()
gen = gen.sort_values(by=['Global_Sales'], ascending=False)
gen                            


# In[145]:


plt.figure(figsize=(15, 10))
sns.barplot(x="Genre", y="Global_Sales", data=gen)
plt.xticks(rotation=90)
        


# In[150]:


## Area wise sales of each publisher
dfpub= df[['Publisher','NA_Sales','EU_Sales', 'NA_Sales','Other_Sales']]
pdetails = dfpub.groupby(by=['Publisher']).sum()
pdetails


# In[160]:


## Area wise sales of each Genre
dfg= df[['Genre','NA_Sales','EU_Sales', 'JP_Sales','Other_Sales']]
gdetails = dfg.groupby(by=['Genre']).sum()
gdetails


# In[161]:


plt.figure(figsize=(15, 10))
sns.heatmap(gdetails, annot=True, fmt = '.1f')
plt.show()


# In[154]:


### Total Sales by each publisher
salesbyp = data[['Publisher', 'Global_Sales']]
salesbyp = salesbyp.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False)
salesbyp = pd.DataFrame(salesbyp).reset_index()
salesbyp


# In[155]:


##Filter top 10 publishers by total sales
salesbyp = salesbyp.head(10)
salesbyp


# In[157]:


sns.barplot(x='Publisher', y='Global_Sales', data=salesbyp)
plt.xticks(rotation=90)


# In[158]:


### Histograms by different area sales
sns.histplot(data=gdetails, x="EU_Sales")


# In[162]:


sns.histplot(data=gdetails, x="NA_Sales")


# In[163]:


sns.histplot(data=gdetails, x="JP_Sales")


# In[164]:


sns.histplot(data=gdetails, x="Other_Sales")


# In[ ]:




