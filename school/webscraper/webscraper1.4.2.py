import requests
from bs4 import BeautifulSoup
import csv

listofattributes = []

def menu():
    badminton = [
        {'item': 'shoes', 'url': 'https://www.yonex.com/badminton/footwear?p=1'},
        {'item': 'racquets', 'url': 'https://www.yonex.com/badminton/racquets?p=1'},
        {'item': 'apparel', 'url': 'https://www.yonex.com/badminton/apparel?p=1'},
        {'item': 'strings', 'url': 'https://www.yonex.com/badminton/strings?p=1'},
        {'item': 'bags', 'url': 'https://www.yonex.com/badminton/bags?p=1'},
        {'item': 'grips', 'url': 'https://www.yonex.com/badminton/accessories/grip-tape?p=1'},
        {'item': 'towels', 'url': 'https://www.yonex.com/badminton/accessories/towels?p=1'},
        {'item': 'bands', 'url': 'https://www.yonex.com/badminton/accessories/wristbands-headbands?p=1'},
    ]

    for opt in badminton:
        print(f"Type '{opt['item']}' for yonex badminton {opt['item']}")

    global choice
    choice = input('Enter your choice: ')

    for opt in badminton:
        if choice == opt['item']:
            global url
            url = opt['url']

def gettitle(itemname, attributedict):
    if itemname:
        name = str(itemname.text.strip()).replace("’", "'")
        print(name)
        attributedict['Name'] = name

def getdescription(itemdescription, attributedict):
    if itemdescription:
        description = str(itemdescription.text.strip()).replace("’", "'")
        description = ' '.join(description.split())
        print(description)
        attributedict['Description'] = description

def getattributes(itemattributes, attributedict):
    for element in itemattributes:
        attributename = element.find('td').get('data-th')
        attribute = element.find('td', class_='col data')
        attributeinfo = str(attribute.text.strip()).replace("～", "-").replace("、", ",").replace("™", "TM")
        print(f'{attributename}: {attributeinfo}')
        attributedict[attributename] = attributeinfo

def writecsv():
    filename = f'yonex_{choice}.csv'
    global fieldnames
    fieldnames = {
        'shoes': ['Name', 'Description', 'Color(s)', 'Surface', 'Upper', 'Midsole', 'Outsole', 'Size', 'Material', 'Item Code'],
        'racquets': ['Name', 'Flex', 'Frame', 'Shaft', 'Joint', 'Length', 'Weight/Grip', 'Stringing advice', 'Color(s)', 'Made In', 'Item Code'],
        'apparel': ['Name', 'Color(s)', 'Material', 'Item Code'],
        'strings': ['Name', 'Description', 'Color(s)', 'Gauge', 'Length', 'Core', 'Outer', 'Coating', 'Made In', 'Item Code'],
        'bags': ['Name', 'Description', 'Color(s)', 'Size (LxWxH)', 'Item Code'],
        'grips': ['Name', 'Description', 'Width', 'Length', 'Thickness', 'Material(s)', 'Quantity', 'Item Code'],
        'towels': ['Name', 'Color(s)', 'Material(s)', 'Made In', 'Item Code'],
        'bands': ['Name', 'Color(s)', 'Material(s)', 'Item Code']
    }
    
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames[choice])
        writer.writeheader()
        for itemdict in listofattributes:
            filleditem = {field: itemdict.get(field, '') for field in fieldnames[choice]}
            writer.writerow(filleditem)

menu()

while True:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find('ol', class_="products list items product-items")
    items = results.find_all('li', class_="item product product-item")

    for item in items:
        attributedict = {}

        href = item.find('a').get('href')
        itemresponse = requests.get(href)
        itemsoup = BeautifulSoup(itemresponse.content, 'html.parser')
        
        itemname = itemsoup.find('span', class_='base')
        itemdescription = itemsoup.find('div', class_='value')
        itemattributes = itemsoup.find_all('tr')

        gettitle(itemname, attributedict)
        getdescription(itemdescription, attributedict)
        getattributes(itemattributes, attributedict)

        listofattributes.append(attributedict)
        print()

    next_page_button = soup.find('li', class_="item pages-item-next")
    if not next_page_button:
        break

    url = next_page_button.find('a').get('href')

writecsv()
