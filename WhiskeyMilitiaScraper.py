import requests
from bs4 import BeautifulSoup
import pickle,shelve
import smtplib,time

fromaddr = 'redmen31@gmail.com'
toaddrs  = 'redmen31@gmail.com'


# Credentials (if needed)
username = 'redmen31'
password = ''#remember to re-add pw for functionality 

def scrape():
    
    r=requests.get('http://www.whiskeymilitia.com/')
    soup =BeautifulSoup(r.content)
    
    data=str(soup.html.head.title)
    
    print(data.lower())
    keywords=['fishbowl']#keyword bank
    for item in keywords:
        if item in data.lower():
            print('item found: the item is a '+item)
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.login(username,password)
            msg = 'An item in the keyword list is on sale: Hurry and check '+item
            server.sendmail(fromaddr, toaddrs, msg)
            server.quit()
        else:
            print('FAILURE NO ITEMS FOUND')
        
    
    

while True:
   scrape()
   print('loop completed sleeping for 60 seconds')
   time.sleep(30)

    



