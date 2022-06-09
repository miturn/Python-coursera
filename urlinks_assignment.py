# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

x = 0
position_link = 0
url = input('Enter URL - ')
count = input('Enter count: ')
try:
    count = int(count)
except:
    print('Please enter a numeric number')
position = input('Enter position: ')
try:
    position = int(position) 
except:
    print('Please enter a numeric number')

while x < count:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
    countlink = 0
    
    tags = soup('a')
    for tag in tags:
        if countlink < position:
            new_line = tag.get('href', None)
            print(new_line)
            countlink = countlink +1
    x =  x + 1
    url = new_line     
        

last_tag = soup('a')
for a in last_tag:
    if position_link < position:
        a_tag = soup.a.extract()
        name = a_tag.string.extract()
        position_link = position_link + 1
print(name)
    
    
   
   
    #sample file http://py4e-data.dr-chuck.net/known_by_Fikret.html
    #Actual Problem file  http://py4e-data.dr-chuck.net/known_by_Teiyib.html