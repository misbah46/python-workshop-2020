import requests
from requests_html import HTMLSession
import csv

session = HTMLSession()

r = session.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')

listerList = r.html.find('.lister-list',first=True)

Title = listerList.find('.titleColumn')
#for t in Title:
    #print(t.text)

Rating = listerList.find('.ratingColumn strong')
#for r in Rating:
   # print(r.text)

img = listerList.find('.posterColumn a img')



header=['Title','rating','poster']

data = open ('moviedata.csv','w')
writer = csv.writer(data)
writer.writerow(header)

for i in range(0,len(Title)):
    li = [Title[i].text,Rating[i].text,img[i].attrs['src']]
    #print(Title[i].text)
    #print(Rating[i].text)
    #print(img[i].attrs['src'])
    #print(li)
    writer.writerow(li)

       
