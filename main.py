# Import the library used to query a website
import urllib.request
import urllib.error

# Import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup

# Specify the url
wiki = "http://www.dota2.com/heroes/"

# Query the website and return the html to the variable 'page'
page = urllib.request.urlopen(wiki)

# Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page, 'html.parser')

# print(soup.prettify())

print(soup.find_all("div", class_="heroColLeft"))
print(soup.find_all("div", class_="heroColMiddle"))
print(soup.find_all("div", class_="heroColRight"))

