import requests
from bs4 import BeautifulSoup as bss4
import csv


url = requests.get('https://deals.souq.com/eg-en/smart-tvs/c/15236')

soup = bss4(url.text, 'lxml')

products = soup.findAll('div', {'class':'column-block'})

with open('products.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['product name', 'price'])

    for product in products:
        title = product.find('h6', 'title').text
        price = product.find('h5', 'price').text

        writer.writerow([title, price])

print('Done')