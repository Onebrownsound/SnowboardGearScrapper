""" Author: Dom Modica
Purpose: Monitor outdoor gear site and email myself when an item is on sale. Is important
to check frequently due to deals only lasting 10-15 minutes each """

import requests
from bs4 import BeautifulSoup
import pickle,shelve
import smtplib,time

fromaddr = 'redmen31@gmail.com'
toaddrs  = 'redmen31@gmail.com'
msg = 'An item in the keyword list is on sale: Hurry and check'

# Credentials (if needed)
username = 'redmen31'
password = ''#remember to re-enter pw for script to function

def scrape():
    
    r=requests.get('http://www.steepandcheap.com/current-steal')
    soup =BeautifulSoup(r.content)
    
    data=soup.findAll("div", { "class" : "buy-box-heading" })
    
    data=str(data)

    keywords=['686'] #keyword bank to monitor for desired item namebrands/description
    for item in keywords:
        if item in data.lower():
            print('item found: the item is a '+item)
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.login(username,password)
            server.sendmail(fromaddr, toaddrs, msg)
            server.quit()
        else:
            print('FAILURE NO ITEMS FOUND')
        
    
    

while True:
   scrape()
   print('loop completed sleeping for 60 seconds')
   time.sleep(30)

    
