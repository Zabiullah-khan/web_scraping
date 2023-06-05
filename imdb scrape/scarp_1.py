import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/search/title/?groups=top_250&sort=user_rating'

result = requests.get(url)

soup = BeautifulSoup(result.text,'html.parser')

box = soup.find_all('h3',class_='lister-item-header')

Toplist=[]
for movies in box:
	movies = movies.get_text()
	movies = movies.replace('\n','')
	Toplist.append(movies)

file = open('topmovies.txt','a')
for i in Toplist:
	file.write(i+'\n')
file.close()

