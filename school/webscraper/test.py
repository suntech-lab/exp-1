import requests
from bs4 import BeautifulSoup
import csv

# Define the badminton category URLs
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

# Define fieldnames for CSV output
FIELDNAMES = {
    'shoes': ['Name', 'Description', 'Color(s)', 'Surface', 'Upper', 'Midsole', 'Outsole', 'Size', 'Material', 'Item Code'],
    'racquets': ['Name', 'Flex', 'Frame', 'Shaft', 'Joint', 'Length', 'Weight/Grip', 'Stringing advice', 'Color(s)', 'Made In', 'Item Code'],
    'apparel': ['Name', 'Color(s)', 'Material', 'Item Code'],
    'strings': ['Name', 'Description', 'Color(s)', 'Gauge', 'Length', 'Core', 'Outer', 'Coating', 'Made In', 'Item Code'],
    'bags': ['Name', 'Description', 'Color(s)', 'Size (LxWxH)', 'Item Code'],
    'grips': ['Name', 'Description', 'Width', 'Length', 'Thickness', 'Material(s)', 'Quantity', 'Item Code'],
    'towels': ['Name', 'Description', 'Color(s)', 'Material(s)', 'Made In', 'Item Code'],
    'bands': ['Name', 'Color(s)', 'Material(s)', 'Item Code']
}

def get_product_links(category_url):
    """Retrieve product links from a category URL."""
    response = requests.get(category_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    product_links = [item.a['href'] for item in soup.find_all('li', class_='item product product-item')]
    next_page = soup.find('li', class_='item pages-item-next')
    if next_page:
        product_links.extend(get_product_links(next_page.a['href']))
    return product_links

def extract_product_details(product_url, category, writer):
    """Extract and write product details to CSV."""
    response = requests.get(product_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    attributes = {}
    attributes['Name'] = soup.find('span', class_='base').text.strip()
    attributes['Description'] = soup.find('div', class_='value').text.strip()

    for row in soup.find_all('tr'):
        key = row.find('td', class_='label').text.strip()
        value = row.find('td', class_='data').text.strip()
        attributes[key] = value
    
    writer.writerow({field: attributes.get(field, '') for field in FIELDNAMES[category]})

def main():
    # User selects a category
    print("Choose a Yonex badminton category:")
    for opt in badminton:
        print(f"Type '{opt['item']}' for Yonex {opt['item']}")
    choice = input('Enter your choice: ').lower()

    if choice not in FIELDNAMES:
        print("Invalid choice.")
        return

    category_url = next(opt['url'] for opt in badminton if opt['item'] == choice)
    product_links = get_product_links(category_url)

    filename = f'yonex_{choice}.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES[choice])
        writer.writeheader()

        for link in product_links:
            extract_product_details(link, choice, writer)

    print(f"Data extraction completed. Saved to {filename}")

if __name__ == "__main__":
    main()
