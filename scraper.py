import requests
import re
from bs4 import BeautifulSoup
  
def getPrice(URL):
  
    #URL = "https://shop.tcgplayer.com/pokemon/sm-base-set/lurantis-gx-secret"
    r = requests.get(URL)

    soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
    #print(soup.prettify())

    line = soup.find('td', attrs = {'class':'price-point__data'}) #grabs the line that displays market price

    lineStr = str(line) #converts it to a string

    priceL = re.findall("\$[0-9]+\.[0-9]+", lineStr) #returns just the price from the string
    
    #converts list to str
    price = ''
    for p in priceL:
        price+=p
    
    return price

