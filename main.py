import scraper
import csvReader
import re
import time

from scraper import getPrice
from csvReader import main

start = time.time() #starts a timer
print("Time Started")

URLs = main() #sets URLs to the list of URLs from csvReader

prices = [] #list of prices
bad=[] #list of bad urls

counter = 0

#goes through list of URLs, calls the scraper and adds it to the prices list
for url in URLs:
    counter+=1
    print(str(counter)+' out of '+str(len(URLs)))
    price = getPrice(url)
    if(price!=''):
        prices.append(price)
    else:
        bad.append(url)

print(bad)
print(len(bad))

sum = 0 #total value of cards
numbers = [] #stores the prices as floats

#converts prices to floats
for p in prices:
    string = re.findall('[0-9]?[0-9]+', str(p))
    number = ''
    for num in string:  
        number+=num
    numbers.append(round(float(number)*0.01, 2))

#print(numbers)

#adds all the numbers
for n in numbers:
    sum+=n
    #print(sum)
    
print('$'+str(sum))

end = time.time() #ends timer
print('Total Time Elapsed: '+str(round(end - start, 2))+' seconds') #displays runtime
