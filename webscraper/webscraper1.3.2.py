import requests
from bs4 import BeautifulSoup

badminton = [
    {'item': 'shoes', 'url': 'https://www.yonex.com/badminton/footwear?p=1'},
    {'item': 'racquets', 'url': 'https://www.yonex.com/badminton/racquets?p=1'},
    {'item': 'apparel', 'url': 'https://www.yonex.com/badminton/apparel?p=1'}
]
#the "?p=1" part of the urls arent actually needed it was just easier to change the page like that
#it defaults to the first page if there isnt a "?p=1"
nextpage = 1 

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
        name = item.find('a', class_="product-item-link")

        href = item.find('a').get('href')#href(hypertext reference): the page of the specific shoe
        itemresponse = requests.get(href)

        itemsoup = BeautifulSoup(itemresponse.content, 'html.parser')
        itemdescription = itemsoup.find('div', class_='value')
        itemattributes = itemsoup.find_all('tr')
        #above section designates and finds the shoe details and attributes

        print(name.text.strip())
        if itemdescription:
            print(itemdescription.text.strip())

        for element in itemattributes:
            attribute = element.find('td', class_='col data')
            attributename = element.find('td').get('data-th')
            if attribute is not None:#check if attribute exists
                print(f'{attributename}: {attribute.text.strip()}')
            else:
                pass
        print()
        #above prints the attributes neatly so that it is read easily instead of just lines

    nextpage += 1