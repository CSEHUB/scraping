
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
#from tabulate import tabulate
import requests
import pandas as pd
import collections


# In[2]:


# Set website and user-agent or page will obfuscate datea
cape_website = "http://www.cape.ucsd.edu/responses/Results.aspx?Name=&CourseNumber=cse"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


# In[3]:


# Set up requests BeautifulSoup scraper
request = requests.get(cape_website, headers=headers)
soup = BeautifulSoup(request.content, 'html.parser')


# In[4]:


table = soup.find_all('table')[0]


# In[5]:


listOfValue = {}
counter = 0
tableList =  table.find_all('tbody')[0]
ClassList = tableList.find_all('tr')


# In[6]:


for i in ClassList:
    listOfValue[i.find('a').text] = []
    
for i in ClassList:
    listOfValue[i.find('a').text].append(i.find_all('td')[2].text)
    


# In[7]:


# convert unicode encoding to ascii

def convert(data):
    if isinstance(data, str):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.items()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data
    
listOfValue = convert(listOfValue)
listOfValue.pop('No CAPEs submitted', None)


# In[8]:


# convert dict to string, format and replace string, convert back to dict

import json
jsonFormattedString = json.dumps(listOfValue, indent=4, sort_keys=True)
jsonFormattedString = jsonFormattedString.replace("/", "／")
jsonFormattedString = jsonFormattedString.replace(".", "．")

with open("DATA.json", "w") as outputFile:
    outputFile.write(jsonFormattedString)

jsonDict = json.loads(jsonFormattedString)


# In[9]:


# modify databaseURL for testing

import pyrebase

config = {
  "apiKey": "apiKey",
  "authDomain": "projectId.firebaseapp.com",
  "databaseURL": "https://[DATABASE_NAME].firebaseio.com/",
  # example: "databaseURL": "https://python-to-firebase.firebaseio.com/",
  "storageBucket": "projectId.appspot.com",
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
db.update(jsonDict)

