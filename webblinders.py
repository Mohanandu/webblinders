#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_excel("global_superstore_2016.xlsx")
df.head()


# In[2]:


df.shape, df.columns, df.dtypes


# In[3]:


df.info()


# In[4]:


df.describe(include='all')


# In[5]:


df.isnull().sum().sort_values(ascending=False)


# In[13]:


sns.histplot(df['Sales'], kde=True)
plt.title('Sales Distribution')
plt.show()



# In[12]:


sns.histplot(df['Profit'], kde=True, color='orange')
plt.title('Profit Distribution')
plt.show()


# In[15]:


plt.figure(figsize=(10,4))
sns.boxplot(data=df, x='Category', y='Profit')
plt.title("Profit by Category")
plt.show()



# In[14]:


plt.figure(figsize=(12,5))
sns.boxplot(data=df, x='Sub-Category', y='Profit')
plt.title("Profit by Sub-Category")
plt.xticks(rotation=45)
plt.show()


# In[9]:


top_countries = df['Country'].value_counts().head(10)
top_countries.plot(kind='bar', title="Top 10 Countries by Orders", figsize=(10,4))
plt.show()


# In[10]:


region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
region_sales.plot(kind='bar', title="Sales by Region", color='green')
plt.show()


# In[11]:


plt.figure(figsize=(8,6))
sns.heatmap(df[['Sales', 'Quantity', 'Discount', 'Profit', 'Shipping Cost']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()


# In[ ]:




