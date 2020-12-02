# web scrapping tutorial
# by Clever Programming

from bs4 import BeautifulSoup
import requests
import pandas as pd

# los angeles weather page
#page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.099695000000054&lon=-118.33539999999999#.XprENvlxVwF')

# new york weather page
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=43.2281&lon=-76.0007#.XprYZvlxVwE')
soup = BeautifulSoup(page.content, 'html.parser')

#print the whole page
#print(soup)

#print all the a tag
#print(soup.find_all('a'))

#print all the week details
week = soup.find(id='seven-day-forecast-body')
items = week.find_all(class_='tombstone-container')

#print details of single item
#print(items[0])
#print(items[0].find(class_='period-name').get_text())
#print(items[0].find(class_='short-desc').get_text())
#print(items[0].find(class_='temp').get_text())

# listing details of each day's weather parameters
period_names = [item.find(class_='period-name').get_text() for item in items]
short_descriptions = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]

#print(period_names)
#print(short_descriptions)
#print(temperatures)

# store the weather parameters in panda data framework
weather_stuff = pd.DataFrame(
	{
		'period_names': period_names,
		'short_descriptions': short_descriptions,
		'temperatures': temperatures,
		
	}
)

print(weather_stuff)
# store the weather data into a csv file
#weather_stuff.to_csv('weather_los_angeles.csv')
weather_stuff.to_csv('weather_new_york.csv')





