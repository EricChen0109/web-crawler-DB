import requests
from bs4 import BeautifulSoup

url = 'https://www.iana.org/domains'
web = requests.get(url)
soup = BeautifulSoup(web.text,"html.parser")
#title = soup.title
#titleText = title.text
#print(titleText)

#print(soup.select('#logo'))

"""
div = soup.find_all('div')
main = (div[3].find_all('main'))
a = main[0].find_all('a')

for i in a:
    print(i.text)
"""

id = soup.select('#sidenav')
father = id[0].find('ul')
txt = father.find_all('li')
a = []
a .append(txt[0].find('a'))
a .append(txt[1].find('a'))
a .append(txt[8].find('a'))
a .append(txt[12].find('a'))
a .append(txt[13].find('a'))
a .append(txt[16].find('a'))
a .append(txt[23].find('a'))

for i in a:
    print(i.text)
print("-------------------")
print(father.find_all('li')[12].find_previous_siblings())
print("--------------------")
print(father.find_all('li')[12].find_next_siblings())
 