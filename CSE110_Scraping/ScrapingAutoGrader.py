
# coding: utf-8

# In[2]:


#file to scrape
from bs4 import BeautifulSoup

#files to login
from lxml import html
import lxml.html
import requests

import pandas as pd

import re
from robobrowser import RoboBrowser


# In[56]:


#used to log user into Grade
def getAutoGraderSession(loginURL, Email, Password):
    s = requests.session()
    login = s.get(loginURL)
    login_html = lxml.html.fromstring(login.text)
    hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')
    form= {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}
    #print(form)
    form['username'] = Email
    form['password'] = Password 
    response = s.post(loginURL, data=form)
    response.url
    return (response, s)
    #returns the urls response and the session


# In[86]:


(myAutoGrader, session) = getAutoGraderSession('https://autograder.ucsd.edu/login', 'USERNAME@ucsd.edu', 'PASSWORD')
souppy = BeautifulSoup(myAutoGrader.content, 'html.parser')
print(type(session))


# In[87]:


tempYo = souppy.find_all('a')

queue = ''
        
def findQueue(stringValue):
    for i in stringValue:
    
        if 'queue' in i['href']:
            return i
    return ''

queue = findQueue(tempYo)
print(queue['href'])


# In[88]:


queueRequest = session.get('https://autograder.ucsd.edu' + queue['href'] + '#pending-tab')


# In[89]:


queueSoup = BeautifulSoup(queueRequest.content, 'html.parser')


# In[91]:


queueSoup.find('div', {'id': 'news-feed-tab-container'})


# In[63]:


#print(souppy.prettify())
#TRYING TO FIND THE FRICKEN LIST FOR THE QUEUE
chicken = souppy.find_all('a')
history = ''
for i in chicken:
    if 'history' in i['href'] and 'queue' in i['href'] :
        history = i['href']
        
print(history)

requestHistory = session.get('https://autograder.ucsd.edu' + history)
prettyHistory = BeautifulSoup(requestHistory.content, 'html.parser')
print(prettyHistory)


# In[40]:


#list of courses currently enrolled
courses = souppy.find_all('option')
currentCourses = []
print(courses)


# In[41]:


# remote irrelvant courses that are disabled
for i in courses:
    if i['value'] != '-1':
        currentCourses.append(i.text)


# In[42]:


print(currentCourses)
#format
for i in range(len(currentCourses)):
    currentCourses[i] = currentCourses[i].replace('\n', '').strip()
#print courses on autograder
print(currentCourses)


# In[49]:


queue = souppy.find('div', {'class': 'queue-listing tab-content'})
print(queue)
print(queue.find('ul'))
temp = souppy.find_all('ul')
print(temp)

