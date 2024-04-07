import requests
from bs4 import BeautifulSoup

url = 'https://ca.finance.yahoo.com/quote/%5EGSPC'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

where_its_at = soup.find('div', class_='D(ib) Mend(20px)')

price_element = where_its_at.find('span')
price = where_its_at.find('fin-streamer')

stock_price = price.text
stock_increase = price_element.text

print('Stock Increase:', stock_increase)
print('Current Stock Value:', stock_price)


