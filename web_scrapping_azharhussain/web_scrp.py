# web scrapping tutorial by Azhar Hussain
# web link: https://www.bankbazaar.com/reviews.html
# tutorial link: https://www.youtube.com/watch?v=2T7rpd_Q7wE


# import necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd


# send request
url = 'https://www.bankbazaar.com/reviews.html'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')
#print(soup.prettify())


# read review text
review_text = []
review_text_element = soup.find_all(class_='text_here review-desc-more')
#review_text_element = soup.find_all('div', {'itemprop':'description'})
#review_text_element = soup.find_all('div', {'class':'text_here review-desc-more'})
#print(review_text_element)

for item in review_text_element:
	review_text.append(item.get_text())
#print(review_text)


# read author name
user_name = []
user_name_element = soup.find_all(class_='js-author-name')
#print(user_name_element)

for item in user_name_element:
	user_name.append(item.text)
#print(user_name)


# read bank name
bank_name = []
bank_name_element = soup.find_all('div', {'class':'review-bank-title'})
#print(bank_name_element)

for item in bank_name_element:
	bank_name.append(item.find('img').get('alt'))
#print(bank_name)


# read user review comment
review_comment = []
review_comment_element = soup.find_all('a', class_='user-review-comment js-individual-title')
#print(review_comment_element)
 
for item in review_comment_element:
	review_comment.append(item.get('title'))	
#print(review_comment)




 

# final array
final_array = []

for user, bank, text, r_comment in zip(user_name, bank_name, review_text, review_comment):	
	final_array.append({
		'username':user, 
		'bank_name':bank, 
		'review_text':text,
		'review_comment':r_comment,
		
	})
#print(final_array)	

# store all the data into dataframe of panda
df = pd.DataFrame(final_array)
print(df)

# export data in csv file
df.to_csv('bankbazar_customer_reviews.csv')













