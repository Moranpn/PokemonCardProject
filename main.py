import scraper
import csvReader

from scraper import getPrice
from csvReader import main

URLs = main() #sets URLs to the list of URLs from csvReader

prices = [] #list of prices

#goes through list of URLs, calls the scraper and adds it to the prices list
for url in URLs:
    prices.append(getPrice(url))


print(prices)

