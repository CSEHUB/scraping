
# coding: utf-8

# In[22]:


from piazza_api import Piazza
from bs4 import BeautifulSoup
import requests
from lxml import html
import lxml.html
import pandas as pd
import re
p = Piazza()


# In[23]:


def cas_login(service, username, password):
    # GET parameters - URL we'd like to log into.
    params = {'service': service}
    LOGIN_URL = service

    # Start session and get login form.
    session = requests.session()
    login = session.get(LOGIN_URL)
    #print(login.text)
    # Get the hidden elements and put them in our form.
    login_html = lxml.html.fromstring(login.text)
    hidden_elements = login_html.xpath('//form//input[@type="hidden"]')
    form = {x.attrib['name']: x.attrib['value'] for x in hidden_elements}

    # "Fill out" the form.
    form['email'] = username
    form['password'] = password

    # Finally, login and return the session.
    session.post(LOGIN_URL, data=form, params=params)
    return session



# In[24]:


session = cas_login('https://piazza.com/account/login', 'USERNAME@ucsd.edu', 'PASSWORD')


# In[25]:


temp = session.get('https://piazza.com/class/')


# In[26]:


soup = BeautifulSoup(temp.content, 'html.parser')


# In[30]:


soup.prettify()

temp = soup.find_all('div')
#notificationNumber = soup.find('div', {'id': 'global_notifications_indicator'})


# In[28]:


print(notificationNumber)


# In[4]:


p.user_login('kvn033@ucsd.edu', 'Angler139710')
user_profile = p.get_user_profile()
CSE110 = p.network("jebhpmejaa92vh")

CSE110.get_post(10)

posts = CSE110.iter_all_posts(limit=1)
for post in posts:
    for i in post:
        print(i)


# In[3]:


for i in post:
    print(i)


# In[16]:


print(type(post['history'][1]))

print(post['history'][1])

for i in post['history'][1]:
    print(i)
print(post['history'][1]['subject'])
print(post['history'][1]['content'])

