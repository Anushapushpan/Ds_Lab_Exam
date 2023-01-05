import requests
from bs4 import BeautifulSoup
url="http://www.ajce.in"
r = requests.get(url)
soup=BeautifulSoup(r.content, 'html.parser')
print(soup)