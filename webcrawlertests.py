import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
url = ''
page = requests.get(url)
print(page.text)
