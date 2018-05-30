
# coding: utf-8

# In[ ]:


from bs4 import BeautifulSoup
from firebase import firebase
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
# from apscheduler.schedulers.blocking import BlockingScheduler
# from tabulate import tabulate
import requests
import pandas as pd
import json


# In[ ]:


#course deleted
#HIST
#LIT

nameOfClass = ['ANTH', 'BENG', 'BIBC', 'CAT', 'CENG', 'CGS', 'CHEM', 'CHIN', 'COGS', 'COMM', 'CONT' , 'CSE' ,'DOC', 'ECE', 'ECON', 'EDS', 'ENVR', 'ERC', 'ESYS', 'ETHN', 'FILM', 'FPMU', 'HDP', 'HMNR', 'HUM', 'ICAM', 'INTL', 'JAPN', 'JUDA', 'LATI', 'LAWS', 'LIGN', 'MAE', 'MATH', 'MMW', 'MUIR', 'MUS', 'NANO', 'PHIL', 'PHYS', 'POLI', 'PSYC', 'RELI', 'REV','MGT', 'SDCC', 'SE','SIO', 'SOC', 'ENG', 'SXTH', 'TDAC', 'TDDM', 'TDGE', 'TMC', 'TWS', 'USP', 'VIS', 'WARR', 'WCWP']
firebase = firebase.FirebaseApplication('https://csehub-c4399.firebaseio.com/')
# nameOfClass = ['ANTH', 'BENG']
# firebase = firebase.FirebaseApplication('https://python-to-firebase.firebaseio.com/')
yearString = "17"
year = int(yearString)


# In[ ]:


def jsonDict(className):
    print(className)
    # Set website and user-agent or page will obfuscate datea
    cape_website = "http://www.cape.ucsd.edu/responses/Results.aspx?Name=&CourseNumber=" + className
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # Set up requests BeautifulSoup scraper
    request = requests.get(cape_website, headers=headers)
    soup = BeautifulSoup(request.content, 'html.parser')
    table = soup.find_all('table')[0]
    listOfValue = {}
    counter = 0
    tableList =  table.find_all('tbody')[0]
    ClassList = tableList.find_all('tr')
    
    for i in ClassList:
        if(i.find_all('td')[2].text[-2:] == yearString and "(A)" in i.find_all('td')[1].text):
            listOfValue[i.find('a').text] = {}
    for i in ClassList:
        if(i.find_all('td')[2].text[-2:] == yearString and "(A)" in i.find_all('td')[1].text):
            listOfValue[i.find('a').text][i.find_all('td')[2].text] = i.find_all('td')[7].text.replace("\n", "")
    return listOfValue


# In[ ]:


def scrapeCapes():
    global yearString
    global year
    # block 1
    allJSON = {}
    allJSON["Courses"] = {}
    for i in nameOfClass:
        schedule = jsonDict(i)
        allJSON["Courses"].update(schedule)

    # block 2
    courseList = json.dumps(allJSON, indent=4)
    courseList = courseList.replace("/", "／")
    courseList = courseList.replace(".", "．")

    jsonDictionary = json.loads(courseList)

    print(courseList)

    # block 3
    with open('Eric.json', 'w') as fp:
        fp.write(courseList)
        #json.dump(allJSON, fp)

    jsonDictionary = json.loads(courseList)
    
    result = firebase.patch('/', { "Course_"+str(year): jsonDictionary})
    getResult = firebase.get('/Course_'+str(year), None)
    print(getResult)
    
    year = year + 1
    yearString = str(year)


# In[ ]:


scheduler = BackgroundScheduler()
scheduler.add_job(scrapeCapes, 'interval', minutes=3, next_run_time=datetime.now())
# for yearly scraping
# scheduler.add_job(scrapeCapes, 'interval', years=1, next_run_time=datetime.now())
scheduler.start()

