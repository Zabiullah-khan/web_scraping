import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
url = 'https://sunnah.com/bukhari:2215'

if  requests.get(url).status_code == 200:
	result = requests.get(url)
	soup = BeautifulSoup(result.content,'html.parser')
	
	page_number = str(soup.find('div',class_='book_page_number').get_text()).replace('\xa0','')
	topic=str(soup.find('div',class_='book_page_english_name').get_text()).replace('\n','').replace('\t','')
	narrator = str(soup.find('div',class_='hadith_narrated').get_text())
	hadith = str(soup.find('div',class_='text_details').get_text())
	
	data=[[page_number,topic,narrator,hadith]]
	excel = pd.DataFrame(data,columns=['page','topic','narrator','hadith'])
	excel.to_csv('scaraped.csv')
else:
	print(False)
