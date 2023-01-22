import requests
from bs4 import BeautifulSoup as BS

r = requests.get('https://stopgame.ru/review/new/izumitelno/p1')
html = BS(r.content, "html.parser")

for el in html.select('.items > .arcticle-summary'):
    title  = el.select('.caption > a')
    print( title[0].text)