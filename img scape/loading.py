import os
import requests
from bs4 import BeautifulSoup

	
result = requests.get('https://unsplash.com/s/photos/guns')
soup = BeautifulSoup(result.content,'html.parser')

imgs = soup.find_all('img',class_='YVj9w')
links = []

for link in imgs:
	links.append(link.get('src'))
	
c = os.getcwd()
try :
	os.mkdir(ref:='images')
except:
	print('directory already exits skipping')
os.chdir(c+'/'+ref)

x=1
for save in links:
	with open('image'+str(x)+'.jpg','wb') as foo:
		bins = requests.get(save)
		foo.write(bins.content)
		print("Ssved Image"+"=>"+str(x))
		x+=1

	
