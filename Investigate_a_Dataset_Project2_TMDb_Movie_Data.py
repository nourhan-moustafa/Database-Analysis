#!/usr/bin/env python
# coding: utf-8

# 
# # Project: Investigating TMDb Movie Dataset.
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
#     This project implements investigating TMDb movie dataset which consists of 10866 columns and 21 rows. This dataset contains details about a collection of movies that were released from 1960 till 2015. In our project, we will be analyzing the given data to come up with data general statistics and visualization.
#     
#     The investigated questions are:
#     
#         - Which Movie has the highest Revenue?
#         - Which Movie has the lowest Revenue?
#         - What is the most profitable movie?
#         - what is the least profitable movie?
#         - what are the most popular cinematic genres?
#         - which year has the highest number of movie releases?
#         - what is the kind of correlation between the two variables 'popularity' vs 'revenue'?
# 

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# >  In this section of the report, we will load the data, check for cleanliness, and then trim and clean our dataset for analysis. I showed the first five headlines of the dataset, the columns names, the shape of the data, the number of columns and rows, and some general statistics. After extracting the types of our data, I changed the release date column into the DateTime type instead of an object/string. Finally, the last thing in this phase is getting rid of any null data and duplicates.
# 
# ### General Properties

# In[3]:


data = pd.read_csv('tmdb-movies.csv')
data.head(5)


# In[28]:


print(list(data.columns.values))


# In[29]:


print(data.shape)


# ### Data Cleaning: General Statistics

# In[30]:


data.describe()


# ### Data Cleaning: Data Types

# In[31]:


data.info()


# In[ ]:


###changing the release date column into the DateTime type instead of an object/string.


# In[32]:


data['release_date'] = pd.to_datetime(data['release_date'], infer_datetime_format=True)
data.info()


# ### Data Cleaning: Removing Null Values

# In[33]:


data.isnull(). any(). sum()


# In[34]:


data.isnull(). any()


# In[ ]:


###validating null values are removed.


# In[35]:


data = data.dropna(how='any',axis=0)
data.isnull(). any()


# ### Data Cleaning: Removing Duplicated Values

# In[5]:


sum(data.duplicated())


# In[6]:


data.drop_duplicates(inplace = True)
print(data.shape)


# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
#  Now that you've trimmed and cleaned your data, you're ready to move on to exploration. Compute statistics and create visualizations with the goal of addressing the research questions that you posed in the Introduction section. It is recommended that you be systematic with your approach. Look at one variable at a time, and then follow it up by looking at relationships between variables.
# 
# ### Data Overview

# In[16]:


data.hist(figsize= (10,8));


# In[17]:


data.count()


# ### Which Movie has the highest & Lowest Revenue?

# In[18]:


hightest_movie_revenue = data["revenue"].max()
print(hightest_movie_revenue)


# In[19]:


print(data.original_title[data['revenue'] == data['revenue'].max()])


# In[5]:


lowest_movie_revenue = data["revenue"].min()
print(lowest_movie_revenue)


# In[1]:


###the zero value in 'revenue' is not considered as an outlier, therefore it is not removed as dripping it would affect the accuracy of the analysis.


# In[6]:


print(data.original_title[data['revenue'] == data['revenue'].min()])


# ### Exploratory Data : Creating New Coulmn 'profit'

# In[50]:


data['profit'] = data['revenue'] -  data['budget']
data.head()


# ### Exploratory Data : Highest & Lowest Profiable Movies using the new created column 'profit'.

# In[21]:


hightest_movie_profit = data['profit'].max()
print(hightest_movie_profit)


# In[22]:


print(data.original_title[data['profit'] == data['profit'].max()])


# In[23]:


lowest_movie_profit = data['profit'].min()
print(lowest_movie_profit)


# In[24]:


print(data.original_title[data['profit'] == data['profit'].min()])


# In[51]:


#setting up the figure size and labels as the follwoing:
plt.figure(figsize=(5,10))

#making a list of comparison between the highest profitable movie and the lowest.
dd = data[(data.profit==data['profit'].max())|(data.profit==data['profit'].min())]

#formating the barplot by adding color, title, xlabel, ylabel.
sns.barplot(dd['original_title'], dd['profit'], palette = 'Blues')
plt.title('Highest & Lowest Profitable Movies', fontsize = 14)
plt.xlabel('original title')
plt.ylabel('profit')
plt.show()


# In[13]:


### The above barplot shows that the most profitable movie is Avatar and the least profitable movie is The Warrior’s Way.


# ### Exploratory Data :   Most Popular Genres

# In[14]:


dg = data['genres'].str.get_dummies(sep='|')
dg1 = dg.sum().reset_index()


# In[20]:


#setting up the figure size and labels as the follwoing:
plt.figure(figsize=(15,10))

#formating the barplot by adding color, title, xlabel, ylabel.
sns.barplot(x=dg.columns, y=dg.sum(), data = dg1)
plt.title('most pupolar genres', fontsize = 25)
plt.xlabel('genres', fontsize = 25)
plt.ylabel('No. of Movies')
plt.xticks(rotation = 90)
plt.show()


# In[16]:


### The above barplot shows that the most common genres are Drama, Comedy, Thriller followed by Action.


# ### Exploratory Data :   Years with the Most Released Movies

# In[17]:


#setting up the figure size and labels as the follwoing:
plt.figure(figsize=(20,10))

#formating the barplot by adding color, title, xlabel, ylabel.
sns.countplot(data['release_year'])
plt.title('Years with most movies', fontsize = 20)
plt.xlabel('Release Year', fontsize = 20)
plt.ylabel('No. of movies', fontsize = 20)
plt.xticks(rotation = 90)
plt.show()


# In[18]:


### The above barplot shows that the highest year with movie releases is in 2014 with almost 700 movies.


# In[5]:


#setting up the figure size and labels as the follwoing:
plt.scatter(data['popularity'], data['revenue'])

#formating the barplot by adding color, title, xlabel, ylabel.
plt.title('pupolarity vs revenue', fontsize = 20)
plt.xlabel('Revenue', fontsize = 20)
plt.ylabel('Popularity', fontsize = 20)
plt.show()


# In[10]:


###the above scatter plot shows that both popularity and revenue have a positive correlation which means that the more popular the movie, the more the revenue.


# <a id='conclusions'></a>
# ## Conclusions
# 
#     After investigating the previous dataset, we can conclude the following:
#     
#        -The highest revenue movie is avatar by 2781505847 $.
#        -The lowest revenue movie is wild card by 0 $.
#        -The highest profitable movie is avatar by 2544505847 $.
#        -The lowest profitable movie is worrier’s way by -413912431 $.
#        -The genre of drama is the most popular one, followed by action, comedy and thriller.
#        -Maximum number of movies releases is in 2014.
#        -popularity and revenue have a positive correlation.
# 
# 
# Limitations of this project:
# 
# The content in the classroom regarding the data visualization part is so limited & not enough which made me took a much longer time googling and learning new things from different platforms and other resources. The dataset also has two many unuseful columns but it has been taken care of in the data wrangling process. Moreover, the null data acted as a limitation to the investigating process due to the missing values which lead to dropping them for the analysis to work with no false or error incidents. Lastly, I could not use the mean to fill any missing data as it is not the best measure of center in this case.
# 

# In[11]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])

