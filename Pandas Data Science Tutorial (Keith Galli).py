#!/usr/bin/env python
# coding: utf-8

# # Importing data frame

# In[63]:


import pandas as pd

#df = pd.read_csv('pokemon_data.csv')


#df_xlsx = pd.read_excel('pokemon_data.xlsx')


#df_txt = pd.read_csv('pokemon_data.txt', delimiter='\t')


# # Reading data in Pandas

# ### Read headers:

# In[14]:


#print(df.columns)


# ### Read each Column

# In[19]:


#print(df['Name'])

#print(df['Name'][0:5])

#print(df.Name)  #(dont work in 2 words)

#print(df[['Name', 'Type 1', 'HP']])


# ### Read each Row

# In[35]:


#print(df.head)

#print(df.head(4))

#print(df.iloc[1])

#print(df.iloc[1:4])

#for index, row in df.iterrows():
#    print(index, row['Name'])

#df.loc[df['Type 1'] == "Fire"]


# ### Read a especific location (R,C)

# In[29]:


#print(df.iloc[2,1])


# # Sorting/Describing data

# In[37]:


#df.describe()


# In[41]:


#df.sort_values('Name', ascending=False)


# In[48]:


#df.sort_values(['Type 1', 'HP'], ascending=[1,0])


# # Making changes to the data

# ### insert new colum

# In[88]:


#df['Total'] = df['HP'] + df['Attacl'] + etc

#df['Total'] = df.iloc[:,4:10].sum(axis=1)

#df.head(5)


# ### re-ordering Column titles:

# In[87]:


#cols = list(df.columns.values)
#df = df[cols[0:4] + [cols[-1]]+ cols[4:12]]

#df.head(5)


# ### erase columns:

# In[67]:


#df = df.drop(columns=['Total'])


# ### Saving our data (CSV, Excel, TXT, etc)

# In[71]:


# df.to_csv('modified.csv', index=False)

# df.to_excel('modified.xlsx', index=False)

#df.to_csv('modified.txt', index=False, sep='\t')


# # Filtering Data

# ### Filter by column

# In[86]:


#df.loc[df['Type 1'] == 'Grass']

#AND:

#df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')]

#OR:

#df.loc[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Poison')]


# ### with conditions:

# In[ ]:


#df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]


# ### Strain Filtering

# In[ ]:


# contain: 

#df.loc[df['Name'].str.contains('Mega')]

# not contain:

#df.loc[~df['Name'].str.contains('Mega')]


# ### regular expressions filtering

# In[97]:


import re

#df.loc[df['Type 1' ].str.contains('fire|grass', flags=re.I, regex=True)]

#df.loc[df['Name' ].str.contains('^pi[a-z]*', flags=re.I, regex=True)]


# # Conditoinal Changes

# change all type of pok??mons from fire to flamer:

# In[ ]:


#df.loc[fd['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'



# Change all fire pokemons to legendary:

# In[98]:


#df.loc[fd['Type 1'] == 'Fire', 'Legendary'] = True


# multiples cond. changes:

# In[ ]:


#df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = ['Test 1', 'Test 2']


# # Aggregate Statistics (Groupby)

# grouping all pokemons by type 1, masuring the mean by type and sorting by defense (top first):

# In[115]:


df = pd.read_csv('modified.csv')

#df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False)


# sum all stats by type 1:

# In[117]:


#df.groupby(['Type 1']).sum()


# Counting by type 1:

# In[122]:


#df['count'] = 1

#df.groupby(['Type 1']).count()['count']


# Counting Multiples parameters:

# In[124]:


#df.groupby(['Type 1', 'Type 2']).count()['count']


# # Working with large amounts of data

# Chunking data in small sets:

# In[127]:


#for df in pd.read_csv('modified.csv', chunksize=5):
#    print("CHUNK DF")
#    print(df)


# Creating a ner data frame from a chuncky set:
# 

# In[ ]:


# new_df = pd.DataFrame(columns=df.columns)

# for df in pd.read_csv('modified.csv', chunksize=5):
#     results = df.groupby(['Type 1']).count()
    
#     new_df = pd.concat([new_df])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




