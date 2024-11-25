import requests
from bs4 import BeautifulSoup
"""
url = 'http://140.127.74.143/normalrender.html'
web = requests.get(url)
soup = BeautifulSoup(web.text,"html.parser")
p = soup.find_all('p')
print('normal:')
print(p[0])
print('-------------------')


url = 'http://140.127.74.143/jsrender.html'
web = requests.get(url)
soup = BeautifulSoup(web.text,"html.parser")
p = soup.find_all('p')
print('js:')
print(p[0])
"""
url = 'https://24h.pchome.com.tw/search/?q=macbook%20air'
web = requests.get(url)
soup = BeautifulSoup(web.text,"html.parser")
father = soup.select("#ItemContainer")
h5 = father[0].find_all('h5')
for i in h5:
    print(i.text)
print(h5)
print('done')
