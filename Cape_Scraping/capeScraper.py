from bs4 import BeautifulSoup
from tabulate import tabulate
import requests
import pandas as pd


# Set website and user-agent or page will obfuscate datea
cape_website = "http://www.cape.ucsd.edu/responses/Results.aspx?Name=cse+110&CourseNumber="
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# Set up requests BeautifulSoup scraper
request = requests.get(cape_website, headers=headers)
soup = BeautifulSoup(request.content, 'html.parser')

# Generate table
table = soup.find_all('table')[0]
df = pd.read_html(str(table))


print(tabulate(df[0], headers='keys', tablefmt='psql'))

