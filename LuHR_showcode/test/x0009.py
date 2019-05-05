from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://www.cnblogs.com/jasondan/p/3497757.html'
r = urlopen(url).read()

soup = BeautifulSoup(r)

for i in soup.find_all('a'):
    print(i.get('href'))
