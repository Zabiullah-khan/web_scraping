import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/list/ls061331800/'

result = requests.get(url)

soup = BeautifulSoup(result.content,'html.parser')
box = soup.find_all('h3',class_='lister-item-header')
rating = soup.find_all('div',class_='ipl-rating-star small')

rate=[]
mrdr=[]
x=1
for lst in box:
	found = lst.find('a').get_text()
	mrdr.append(str(x)+'.'+found)
	x+=1
for rt in rating:
	fnd = rt.get_text()
	fnd = fnd.replace('\n','')
	rate.append(fnd)

file = open('murdermyst.txt','a')
for i in range(len(mrdr)):
	file.write(mrdr[i]+'::'+'Rating :: '+rate[i]+'\n')
file.close()




	
	
	
	

	