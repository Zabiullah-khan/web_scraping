import requests
from bs4 import BeautifulSoup

url = 'https://apilist.fun/'

result = requests.get(url)

soup = BeautifulSoup(result.content,'html.parser')

box = soup.find_all('div','sm:mb-4 mb-1 sm:text-xl text-md flex flex-wrap items-center -mx-1')

apis=[]
for links in box:
	c = links.find_all('a')
	for i in c:
		g = i.get('href')
		apis.append('https://apilist.fun'+g)

file = open('Apis.txt','a')
x=1
for itr in apis:
	file.write(str(x)+'.'+itr+'\n')
	x+=1
file.close

