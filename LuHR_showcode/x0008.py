
from urllib.request import urlopen
from bs4 import BeautifulSoup


url = 'https://www.cnblogs.com/jasondan/p/3497757.html'
r = urlopen(url).read()

soup = BeautifulSoup(r)

t = soup.find_all('body')

s = ''
for i in t[0].find_all(['p','li','h2','h3']):
    s += i.get_text() + '\n'

print(s)

