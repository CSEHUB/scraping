import requests
from bs4 import BeautifulSoup

cape_website = "http://www.cape.ucsd.edu/responses/Results.aspx?Name=cse+110&CourseNumber="

request = requests.get(cape_website)

soup = BeautifulSoup(request.text, 'html.parser')

prettyString = soup.prettify().encode('utf-8').strip()

print (prettyString)
