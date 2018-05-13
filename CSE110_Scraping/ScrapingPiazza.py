
# coding: utf-8

# In[1]:


from piazza_api import Piazza
from bs4 import BeautifulSoup
import requests
from lxml import html
import lxml.html
import pandas as pd
import re
p = Piazza()


# In[2]:



person = p.user_login('USERNAME@ucsd.edu', 'PASSWORD')
user_profile = p.get_user_profile()
print()
user_classes= p.get_user_classes()
print(p)
CSE110 = p.network("jebhpmejaa92vh")
print(type(CSE110))
#CSE110.get_post(10)



#posts = CSE110.iter_all_posts(limit=1)
#for post in posts:
#    for i in post:
#        print(i)


# In[3]:


for i in CSE110.feed_filters:
    print(i)
print(type(CSE110.feed_filters))
#feed = CSE110.get_filtered_feed((CSE110.feed_filters[0],CSE110.feed_filters[1],CSE110.feed_filters[2]))


# In[4]:


#holder = FeedFilter(CSE110)
#filters = UnreadFilter(holder)


# In[5]:


#SEARCH FOR THE WORD QUIZ
temp = CSE110.search_feed('Quiz')

counter = 0
for i in temp:
    print()
    print()
    print(counter)
    counter += 1
    print("SUBJECT: ", i['subject'])
    print("CONTENT: ", i['content_snipet'] )
   # for key,value in i.items():
   #     print(key + ":", value)


# In[31]:


#ALL THE COURSES THE USER IS ASSIGNED IN WITH THE ID
for i in user_classes:
    print(i['name'], ":", i['nid'])
#Getting course numbers


# In[12]:


CSE110.get_statistics()


# In[13]:





# In[4]:


for i in post:
    print(i)


# In[16]:


print(type(post['history'][1]))

print(post['history'][1])

for i in post['history'][1]:
    print(i)
print(post['history'][1]['subject'])
print(post['history'][1]['content'])

