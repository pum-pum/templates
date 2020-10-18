import requests
from bs4 import BeautifulSoup as soup 
import re
from colorama import init, Fore 
init()
url = 'https://www.url.com'

peticion = requests.get(url, headers=headers)
print(peticion)
sopa = soup(peticion.content, 'html.parser')

criba = sopa.find_all('li', class_='')

print(len(criba))

for i in criba:
    a = i.find('div', class_='')
    b = i.find('h2', class_='')
    c = a.text.replace('\n', '')
    d = b.text.replace('\n', '')
    print(Fore.BLUE + d)
    print(Fore.RED + c)

criba = sopa.find('div', class_='pagination__results')
nuevo = criba.text.replace('\n', '')
print(nuevo)
criba = sopa.find('div', class_='pagination__container')
nuevo = nuevo = criba.text.replace('\n', '')
print(nuevo)
