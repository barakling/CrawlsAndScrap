from bs4 import BeautifulSoup
import requests
import pandas as pd
import pickle as pkl

#Python class for declaring movie attribtues.
class SaleItemsExtract(object):
    def __init__(self, name, price, sale ):
        self.name = name
        self.price = price
        self.sale = sale
        self.department = department
            
def first2(s):
    return s[:4]

url = 'http://www.castro.com/sale/categories/women/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

thescrap = soup.select('div.product_info')

name = soup.select('div.product-name')
prices = soup.select('div.price')
sales = soup.select('span.value')
department = "SALE Woman"

_temp_ = []

#loop to get and assign class instances
for index in range(0, len(thescrap)):
    dict1 = {}
    dict1["name"] = [a.attrs.get('title') for a in soup.select('div.product-name a')]
    dict1["price"] = prices[index].get_text() 
    dict1["sale"] = sales[index].get_text()
    dict1["department"] = department
    dict1["Index_Main"] = index
    
    _temp_.append(dict1)
    
    
df_Fresh = pd.DataFrame(_temp_)
unpickled_Last_Fresh = pd.read_pickle("./Fresh_Only.pkl")
df_Fresh.to_pickle("./Fresh_Only.pkl")
#print(df_Fresh.dtypes)
#print(unpickled_Last_Fresh.dtypes)

# For Testing - Remove row 18 for pickle compare
#df2 = df_Fresh[df_Fresh.Index_Main != 18]
#df2.to_pickle("./Fresh_Only.pkl")

# Merge data by NAME column
# Only new names will be send to mail
#m = df_Fresh.merge(unpickled_Last_Fresh, left_on='name', right_on='name', how='outer', suffixes=['', '_'], indicator=True)
#n = m.loc[m['_merge'] == "left_only"]
#print(n)
