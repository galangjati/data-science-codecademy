#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


wood = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')


# In[4]:


print(wood.head())
print(steel.head())


# In[6]:


def plot_rankings(name, park, df):
    ranking = df[(df['Name'] == name) & (df['Park'] == park)]
    ax = plt.subplot()
    plt.plot(ranking['Year of Rank'], ranking['Rank'])
    ax.set_xticks(ranking['Year of Rank'].values)
    ax.set_yticks(ranking['Rank'].values)
    ax.invert_yaxis()
    plt.title('{} Rankings' .format(name))
    plt.ylabel('Rank')
    plt.xlabel('Year')
    plt.show()
    
plot_rankings('El Toro', 'Six Flags Great Adventure', wood)
plt.clf()


# In[9]:


def plot_2rankings(name1, park1, name2, park2, df):
    ranking1 = df[(df['Name'] == name1) & (df['Park'] == park1)]
    ranking2 = df[(df['Name'] == name2) & (df['Park'] == park2)]
    ax = plt.subplot()
    plt.plot(ranking1['Year of Rank'], ranking1['Rank'], label = name1)
    plt.plot(ranking2['Year of Rank'], ranking2['Rank'], label = name2)
    ax.invert_yaxis()
    plt.title('{} & {} Rankings' .format(name1, name2))
    plt.ylabel('Rank')
    plt.xlabel('Year')
    plt.legend()
    plt.show()
    
plot_2rankings('El Toro', 'Six Flags Great Adventure', 'Boulder Dash', 'Lake Compounce', wood)
plt.clf()


# In[20]:


def plot_nrank(n, df):
    top_nrank = df[df['Rank'] < n]
    f, ax = plt.subplots(figsize=(10, 8))
    for coaster in set(top_nrank['Name']):
        coaster_rank = top_nrank[top_nrank['Name'] == coaster]
        ax.plot(coaster_rank['Year of Rank'], coaster_rank['Rank'], label = coaster)
    ax.set_yticks([i for i in range(1,(n+1))])
    ax.invert_yaxis()
    plt.title('Top {} Rankings' .format(n))
    plt.xlabel('Year')
    plt.ylabel('Rank')
    plt.legend()
    plt.show()
    
plot_nrank(10, steel)
plt.clf()


# In[24]:


coasters = pd.read_csv('roller_coasters.csv')

print(coasters.head())


# In[35]:


def hist_coaster(df, column):
    plt.hist(df[column].dropna())
    plt.title('{} Roller Coaster Histogram' .format(column))
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.legend(column)
    plt.show()
    
hist_coaster(coasters, 'speed')
hist_coaster(coasters, 'height')
plt.clf()


# In[46]:


def bar_inversion(df, park):
    park_coaster = df[df['park'] == park]
    park_coaster = park_coaster.sort_values('num_inversions', ascending = False)
    name_coaster = park_coaster['name']
    num_inversion = park_coaster.num_inversions
    ax = plt.subplot()
    plt.bar(range(len(num_inversion)), num_inversion)
    ax.set_xticks(range(len(name_coaster)))
    ax.set_xticklabels(name_coaster, rotation = 90)
    plt.title('Number of Inversions Coaster in {}' .format(park))
    plt.xlabel('Coaster')
    plt.ylabel('Count of Inversion')
    plt.show()
    
bar_inversion(coasters, 'Six Flags Great Adventure')
plt.clf()


# In[49]:


def pie_status(df):
    operating = df[df.status == 'status.operating']
    close = df[df.status == 'status.closed.definitely']
    num_operating = len(operating)
    num_close = len(close)
    count = [num_operating, num_close]
    ax = plt.subplot()
    plt.pie(count, labels = ['Operating', 'Closed'], autopct = '%0.1f%%', explode = (0.1, 0))
    plt.axis('equal')
    plt.show()
    
pie_status(coasters)
plt.clf()


# In[56]:


def scatter(df, column_x, column_y):
    plt.scatter(df[column_x], df[column_y])
    plt.title('Scatter Plot of {} and {}' .format(column_x, column_y))
    plt.xlabel(column_x)
    plt.ylabel(column_y)
    plt.show()
    
scatter(coasters, 'height', 'speed')

