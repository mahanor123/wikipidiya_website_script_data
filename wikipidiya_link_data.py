import requests
from bs4 import BeautifulSoup
from pprint import pprint

websiteUrl=requests.get("https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area").text
soup = BeautifulSoup(websiteUrl,'lxml')
# pprint(soup.prettify())

My_table = soup.find('table',{'class':'wikitable sortable'})
links=My_table.findAll('a')
countries=[]
for link in links:
    countries.append(link.getText('titel'))
    # countries_name = (link.getText('titel'))
    # print countries_name
    # countries.append(countries_name)
pprint (countries)
