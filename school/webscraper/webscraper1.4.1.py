import requests
from bs4 import BeautifulSoup
import csv

badminton = [
    {'item': 'shoes', 'url': 'https://www.yonex.com/badminton/footwear?p=1'},
    {'item': 'racquets', 'url': 'https://www.yonex.com/badminton/racquets?p=1'},
    {'item': 'apparel', 'url': 'https://www.yonex.com/badminton/apparel?p=1'}
]
#the "?p=1" part of the urls arent actually needed it was just easier to change the page like that
#it defaults to the first page if there isnt a "?p=1"
nextpage = 1

listofattributes = []

for opt in badminton:
    print(f"type {opt['item']} for yonex badminton {opt['item']}")

choice = input(':')
for opt in badminton:
    if choice == str(opt['item']):
        url = opt['url']

while nextpage < 4:
    url = url[:-1] + str(nextpage)#changes the page of the site (new implementation)

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find('ol', class_="products list items product-items")
    items = results.find_all('li', class_="item product product-item")
    #above section of assignments are for the for loop below
    #results variable finds the section where there are the shoes

    for item in items:

        attributedict = {}

        href = item.find('a').get('href')#href(hypertext reference): the page of the specific shoe
        itemresponse = requests.get(href)

        itemsoup = BeautifulSoup(itemresponse.content, 'html.parser')
        itemname = itemsoup.find('span', class_='base')
        itemdescription = itemsoup.find('div', class_='value')
        itemattributes = itemsoup.find_all('tr')
        #above section designates and finds the shoe details and attributes

        if itemname:
            name = str(itemname.text.strip()).replace("’", "'")
            print(name)
            attributedict['Name'] = name

        if itemdescription:
            description = str(itemdescription.text.strip())
            if description != '':
                print(description)
                attributedict['Description'] = description
            else:
                attributedict['Description'] = None
        

        for element in itemattributes:
            attribute = element.find('td', class_='col data')
            attributename = element.find('td').get('data-th')
            if attribute:#check if attribute exists
                attributeinfo = str(attribute.text.strip()).replace("～", "-").replace("、", ",").replace("™", "TM")
                print(f'{attributename}: {attributeinfo}')
                attributedict[attributename] = attributeinfo
            else:
                attribute = None

        listofattributes.append(attributedict)
        print()
        #above prints the attributes neatly so that it is read easily instead of just lines

    nextpage += 1


if choice == 'shoes':
    with open('yonexshoes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        field = ['Name', 'Description', 'Color(s)', 'Surface', 'Upper', 'Midsole', 'Outsole', 'Size', 'Material', 'Item Code']
        writer.writerow(field)
        for dict in listofattributes:
            writer.writerow(dict.values())
elif choice == 'racquets':
    with open('yonexracquets.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        field = ['Name', 'Flex', 'Frame', 'Shaft', 'Joint', 'Length', 'Weight/Grip', 'Stringing advice', 'Color(s)', 'Made In', 'Item Code']
        writer.writerow(field)
        for dict in listofattributes:
            writer.writerow(dict.values())
elif choice == 'apparel':
    with open('yonexapparel.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        field = ['Name', 'Color(s)', 'Material', 'Item Code']
        writer.writerow(field)
        for dict in listofattributes:
            writer.writerow(dict.values())
