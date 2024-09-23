import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_medical_symptoms'
response = requests.get(url)
soup = BeautifulSoup(response, "html.parser")
print(soup)