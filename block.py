import time
from datetime import datetime as dt
#print(dt.now())
website_list=['www.youtube.com','youtube.com', 'www.facebook.com','facebook.com','www.instagram.com','instagram.com']
host_linux=r'/etc/hosts'
redirect = '127.0.0.1'
dt(dt.now().weekday) 

while True:
    if dt(dt.now().year,dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month, dt.now().day,18,30):
        print('COLLEGE TIME')
        with open(host_linux ,'r+') as file:
           content=file.read()
           #print(content)
           for website in website_list:
               if website not in  content:
                   file.write(redirect + "  " + website + "\n")

    else:
        with open(host_linux ,'r+') as file:
           content=file.readlines()
           file.seek(0)
           for line in content:
               if not any(website in line for website in website_list):
                file.write(line)
                file.truncate()   
        print('FUN TIME') 
     else if:
        int = input("Do you want to continue")        
    time.sleep(2)    