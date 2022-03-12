from bs4 import BeautifulSoup
import requests
import re
import random
import csv

#Python class for declaring movie attribtues.
class ExtractMovies(object):
    def __init__(self, name, price, sale ):
        self.name = name
        self.price = price
        self.sale = sale
        self.department = department
            
def first2(s):
    return s[:4]

url = 'https://www.castro.com/sale/categories/women?p={}'
page_number = 1
while(page_number <= 9): 
    response = requests.get(url.format(page_number))

    soup = BeautifulSoup(response.text, 'html.parser')

    movies = soup.select('div.product_info')

    #name = [a.attrs.get('href') for a in soup.select('div.product-name a')]
    name = soup.select('div.product-name')
    prices = soup.select('div.price')
    sales = soup.select('span.value')
    department = 'SALE Woman'

    _temp_ = []

    #loop to get and assign class instances
    for index in range(0, len(movies)):
        name = [a.attrs.get('title') for a in soup.select('div.product-name a')]
        #name = movies[index].get_text()
        price = prices[index].get_text().replace('    מחיר מדף  0.00 ₪   ', '') 
        price = price.replace('   מחיר רגיל ', ';')
        price = price.replace('  החל מ ', '') 
        price = price.replace('פריט שני ב- 50% הנחה',';פריט שני ב- 50% הנחה')
        sale = sales[index].get_text()
        movie_instances = ExtractMovies(
            name[index], price,sale
            )
        _temp_.append(movie_instances)

    #shuffling array to randomize movies
    #random.shuffle(_temp_)

    filename = 'Castro.csv'
    f = open(filename,'a',encoding='UTF8',newline='')


    music = csv.writer(f,delimiter=';')

    i=1    
    for obj in _temp_:
            {i, obj.name, obj.price , obj.sale, obj.department} 
            i=i+1        
            if(i==500):
                break
        
        # music.writerow(data)
            music.writerow([obj.name, obj.price, obj.sale, obj.department])
#music.writerow(_temp_) #Writing to CSV
    page_number += 1