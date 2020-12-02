# web scrapping intellipaat

# import the libraries to query a website
import requests
from bs4 import BeautifulSoup
import pandas as pd


# specify the url
web_link = "https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area"
link = requests.get(web_link)
#print(link)

soup = BeautifulSoup(link.content, 'html.parser')
#print(soup.prettify())

print(soup.title)
print(soup.title.string)

"""
all_links = soup.find_all('a')
for link in all_links:
	print(link.get('href'))

all_tables = soup.find_all('table')
for table in all_tables:
	print(table)
"""	

desired_table = soup.find('table', class_='wikitable sortable')
#print(desired_table.prettify())

desired_table_links = desired_table.findAll('a')
#print(desired_table_links)

country_names = []
for link in desired_table_links:
	country_names.append(link.get('title'))
print(country_names)

# store data into pandas dataframe
df = pd.DataFrame()
df['Country'] = country_names
print(df)








