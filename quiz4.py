import csv
import requests
import csv
from bs4 import BeautifulSoup
from time import sleep
from random import randint

f = open('Medication.csv', 'w', newline='\n')
f_obj = csv.writer(f)
f_obj.writerow(['name', 'value'])
h = {'Accept-Language': 'en-US'}
ind = 1
while ind < 6:
    url = f'https://ge.iherb.com/c/california-gold-nutrition?p={ind}'
    r = requests.get(url, headers=h)
    soup_all = BeautifulSoup(r.text, 'html.parser')
    soup = soup_all.find('div', class_='products')
    all_movies = soup.find_all('div', class_='product-cell-container')
    for each in all_movies:
        n = each.find('div', class_='absolute-link-wrapper')
        title_div = n.find('div', class_='product-title')
        title = title_div.find('bdi').text
        # img_span = n.find('span', class_='product-image')
        # img = img_span.find('img')
        # image = img.attrs['src']
        price_div = each.find('div', class_='product-price')
        span = price_div.find('span', class_='price')
        price = span.find('bdi').text
        print(price)
        f_obj.writerow([title, price])
    ind += 1
    sleep(randint(12, 15))

# url = f'https://ge.iherb.com/c/california-gold-nutrition?p=1'
# r = requests.get(url, headers=h)
# soup_all = BeautifulSoup(r.text, 'html.parser')
# soup = soup_all.find('div', class_='products')
# all_movies = soup.find_all('div', class_='product-cell-container')
# for each in all_movies:
#     n = each.find('div', class_='absolute-link-wrapper')
#     title_div = n.find('div', class_='product-title')
#     title = title_div.find('bdi').text
#     # img_span = n.find('span', class_='product-image')
#     # img = img_span.find('img')
#     # image = img.attrs['src']
#     price_div = each.find('div', class_='product-price')
#     span = price_div.find('span', class_='price')
#     price = span.find('bdi').text
#     print(price)
#
#     # f_obj.writerow([title, price])




























