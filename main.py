#Web Scraping - Grabbing a Class

import bs4
import lxml #helps us process XML and HTML

from bs4 import BeautifulSoup

import requests

result = requests.get("https://realpython.github.io/fake-jobs/")
soup = bs4.BeautifulSoup(result.text,"lxml")

print('\n')

print("These are the locations: ")
print(soup.select('.location'))
