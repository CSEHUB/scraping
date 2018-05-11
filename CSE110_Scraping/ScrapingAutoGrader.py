
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
from lxml import html
import requests
import pandas as pd
import re
from robobrowser import RoboBrowser


# In[12]:


def loginWebsite(URLogin, Username, Password, URLPage):
    session_requests = requests.session()
    login_url = URLogin
    result = session_requests.get(login_url)
    #Made the session request to the get login

    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='authenticityToken']/@value")))[0]
    # get teh authenticity token
    payload = {
        "username": Username, 
        "password": Password, 
        "authenticityToken": authenticity_token
    }
    #data to login with
    superSoup = ''
    with requests.session() as sessions:
        result = sessions.post(
            login_url, 
            data = payload, 
            headers = dict(referer=login_url)
        )
        actualpage = URLPage
        #able to access pages within the login using the get command
        r = sessions.get(actualpage)
        superSoup = BeautifulSoup(r.content, 'html.parser')

    tree = html.fromstring(result.content)
    return superSoup


# In[13]:


superSoup = loginWebsite("https://autograder.ucsd.edu/login","username@ucsd.edu", "password", 'https://autograder.ucsd.edu/queue/248')
print(superSoup.find('div', {'class': 'queue-listing tab-content'}))


# In[5]:


print(superSoup.prettify())


# In[7]:


CourseList = superSoup.find_all('option')


# In[8]:


for i in range(len(CourseList)-1):
    print(CourseList[i]['title'])
    print(CourseList[i])



# In[7]:


peopleList= superSoup.find_all('a')


# In[18]:


for i in peopleList:
    print(i)


# In[9]:


superSoup.prettify()


# In[66]:


listOfLink = souppy.find_all('a')


# In[73]:


for i in listOfLink:
    print(i['href'])

