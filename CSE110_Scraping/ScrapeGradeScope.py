
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests
from lxml import html
import lxml.html
import pandas as pd
import re
from robobrowser import RoboBrowser


# In[3]:


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


# In[4]:


def getGrades(email,password):
    session = (cas_login('https://gradescope.com/login', email, password))
    temp = session.get('https://gradescope.com/account')
    banana = BeautifulSoup(temp.content, 'html.parser')
    
    links = banana.find_all('a', {'class': 'courseBox'})
    listOfClasses = banana.find_all('div', {'class': 'courseList'})
    value = 0
    if len(listOfClasses) == 2:
        value = 1
    dictValue = {}
    for i in listOfClasses[value].find_all('a'):
        #print(i['href'])
        dictValue[i.find('h3').text] = []
        firstCourse = session.get( 'https://gradescope.com' + i['href'])
        secondBeauty = BeautifulSoup(firstCourse.content, 'html.parser')
        listClass = secondBeauty.find_all('tr')
        
        for k in range(len(listClass)-1):
            scores = listClass[k+1].find_all('td')[0].text
            if listClass[k+1].find('th').find('a')!= None:
                course = listClass[k+1].find('th').find('a').text
                dictValue[i.find('h3').text].append({course: scores})
           
    return dictValue


# In[12]:


#dictionary = getGrades('GRADESCOPE_EMAIL', 'GRADESCOPE_PASSWORD')
dictionary = getGrades('USERNAME@ucsd.edu', 'PASSWORD')


# In[13]:


#display the data as a json
for (key, value) in dictionary.items():
    print("{", key, ":")
    for i in value:
        print("\t", i)
    print("}")
    print()


# In[14]:


#exporting your grades as a json LOL
import json
with open('grade.json', 'w') as fp:
    json.dump(dictValue, fp)

