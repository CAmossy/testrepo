# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
times = input('Enter count - ')
position = input('Enter the position you would like to go to - ')

try :
    count = int(times)
except :
    print('Enter an integer for number of times to perform task')
    quit

try :
    pos = int(position)
except :
    print('Enter an integer position')
    quit

#number of times I want to follow links
for i in range(count) :
    html = urlopen(url, context=ctx).read() #opens the web page and reads it
    soup = BeautifulSoup(html, "html.parser") #creates an object from the html on webpage
    tags = soup('a') #creates a list of anchor tags
    n = 0
    for tag in tags :
        #this will make sure I pull the right position
        n = n + 1 #We are stuck in this loop until we get to the position we want, then we drop below
        if n >= pos :
            break
    url = tag.get('href', None) #takes the href/link from the anchor tag
    print(tag.get('href', None))
    name = tag.contents[0] #sets the name as the name associated with that link

print(name)

#sum = 0
#span = soup('span')
#for item in span :
    #print('TAG:', item)
    #print('URL:', item.get('href', None))
    #print('Contents:', item.contents[0])
    #print('Attrs:', item.attrs)
    #sum = sum + int(item.contents[0])
#print(sum)
