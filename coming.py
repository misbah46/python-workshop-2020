import requests
from requests_html import HTMLSession
import csv

session = HTMLSession()

r = session.get('https://www.imdb.com/movies-coming-soon/?ref_=nv_mv_cs')

content = r.html.find('.list',first=True)
#print(content)

Title = content.find('.overview-top',first=True)
#print(Title.text)

name = Title.find('h4 a',first=True)
print(name.text)

time = Title.find('time',first=True)
print(time.text)

genre = Title.find('span')
for g in genre:
    print(g.text)

disc = Title.find('.outline',first=True)
print(disc.text)

star= Title.find('.txt-block')
for s in star:
    print(s.text)

img= content.find('.hover-over-image img',first=True)
print(img.attrs['src'])
    



