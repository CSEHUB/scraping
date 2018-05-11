
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
from lxml import html
import lxml.html
import pandas as pd
import re
from robobrowser import RoboBrowser


# In[77]:


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
    form['session[email]'] = username
    form['session[password]'] = password

    # Finally, login and return the session.
    session.post(LOGIN_URL, data=form, params=params)
    return session


# In[78]:


session = (cas_login('https://gradescope.com/login', 'username@ucsd.edu', 'password'))
temp = session.get('https://gradescope.com/account')


# In[79]:


banana = BeautifulSoup(temp.content, 'html.parser')
links = banana.find_all('a', {'class': 'courseBox'})


# In[110]:


print(links[0]['href'])
listOfClasses = banana.find_all('div', {'class': 'courseList'})
print(type(links[2]))


# In[155]:

value = 0
if len(listOfClasses) == 2:
    value = 1
for i in listOfClasses[value].find_all('a'):
    #print(i['href'])
    print(i.find('h3').text)
    firstCourse = session.get( 'https://gradescope.com' + i['href'])
    secondBeauty = BeautifulSoup(firstCourse.content, 'html.parser')
    listClass = secondBeauty.find_all('tr')
    
    for i in range(len(listClass)-1):
        scores = listClass[i+1].find_all('td')[0].text
        if listClass[i+1].find('th').find('a')!= None:
            course = listClass[i+1].find('th').find('a').text
            print(course, scores)


# In[107]:


firstCourse = session.get( 'https://gradescope.com' + links[2]['href'] )

for i in links:
    print(i)


# In[85]:


secondBeauty = BeautifulSoup(firstCourse.content, 'html.parser')
secondBeauty


# In[88]:


listClass = secondBeauty.find_all('tr')
    
for i in range(len(listClass)-1):
    scores = listClass[i+1].find_all('td')[0].text
    course = listClass[i+1].find('th').find('a').text
    print(course, scores)


# In[73]:


for i in links:
    print(i.find('h3').text)


# In[60]:


print(superSoup)

