
# coding: utf-8

# In[283]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[284]:


#quote_page1 = 'http://www.gradesource.com/reports/7/29142/categoryscores.html'
#page = requests.get(quote_page1)


# In[285]:


#soupYo = BeautifulSoup(page.content, 'html.parser')


# In[286]:


def getGradeSource(URL):
    arrTotal = []

    quote_page = URL
    page = requests.get(quote_page)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    table = soup.find_all('tr')
    arr = []

    for i in range(len(table)):
        arr.append(table[i].find_all('td'))

    for i in range(len(arr)):
        if i >= 5 and i <= len(arr)-2:     
            arrHolder = []
            for k in range(len(arr[i])):
                if arr[i][k].find("b") != None:
                    arrHolder.append(arr[i][k].find("b").text) # getting the course id
                elif arr[i][k].find("font") != None:
                    arrHolder.append(arr[i][k].find("font").text) # getting the rank
            arrTotal.append(arrHolder)
    return arrTotal


# In[287]:


CSE110 = getGradeSource('http://www.gradesource.com/reports/7/29889/cs126276.html')
cse15L = getGradeSource('http://www.gradesource.com/reports/7/29142/categoryscores.html')


# In[288]:


for i in CSE110:
    print(i)


# In[289]:


for i in cse15L:
    print(i)

