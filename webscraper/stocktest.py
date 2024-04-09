'''
made this for fun
it finds the current price of the S&P 500 and the price change
uses the yahoo finance website
ill test out how it fares when the price changes, when it changes
'''
import time
from datetime import datetime
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

while True:
    time.sleep(600)
    print('Stock Increase:', stock_increase)
    print('Current Stock Value:', stock_price)
    print(datetime.now())
    print()
