import requests
from bs4 import BeautifulSoup

url = 'https://cafe.naver.com/jellozon'
html = requests.get(url).text.strip()
print(html[0:100])

soup = BeautifulSoup(html, 'html5lib')
for link in soup('a'):  # anchor tav
    print(link.get('href'))