import requests
from bs4 import BeautifulSoup

url = 'https://www.yonex.com/badminton/footwear?p=1'
#the "?p=1" part of the url isnt actually needed it was just easier to change the page like that
#it defaults to the first page if there isnt a "?p=1"
nextpage = 1 

while nextpage < 4:
    url = url[:-1] + str(nextpage)#changes the page of the site (new implementation)

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find('ol', class_="products list items product-items")
    shoes = results.find_all('li', class_="item product product-item")
    #above section of assignments are for the for loop below
    #results variable finds the section where there are the shoes

    for shoe in shoes:
        name = shoe.find('a', class_="product-item-link")

        href = shoe.find('a').get('href')#href(hypertext reference): the page of the specific shoe
        shoeresponse = requests.get(href)

        shoesoup = BeautifulSoup(shoeresponse.content, 'html.parser')
        shoedescription = shoesoup.find('div', class_='value')
        shoeattributes = shoesoup.find_all('tr')
        #above section designates and finds the shoe details and attributes

        print(name.text.strip())
        if shoedescription:
            print(shoedescription.text.strip())

        for element in shoeattributes:
            attribute = element.find('td', class_='col data')
            attributename = element.find('td').get('data-th')
            print(f'{attributename}: {attribute.text.strip()}')
        #above prints the attributes neatly so that it is read easily instead of just lines

        print()

    nextpage += 1