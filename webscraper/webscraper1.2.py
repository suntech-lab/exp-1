import requests #requests library
from bs4 import BeautifulSoup

URL = "https://www.youtube.com/" #the site that the get method will use
page = requests.get(URL)
soup = BeautifulSoup(open(page))

print(soup)