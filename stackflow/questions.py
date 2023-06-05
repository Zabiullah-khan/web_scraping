import requests
from bs4 import BeautifulSoup

url ='https://stackoverflow.com/questions?tab=Bounties'

result = requests.get(url)

soup = BeautifulSoup(result.content,'html.parser')
htag = soup.find_all('a',class_='s-link')

ques_lin=[]
for l in htag:
	links = l.get('href')
	ques_lin.append('https://stackoverflow.com'+links)

print(ques_lin)

	