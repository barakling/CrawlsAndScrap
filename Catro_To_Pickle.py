from bs4 import BeautifulSoup
import requests
import pandas as pd
import pickle as pkl


url = 'https://www.castro.com/sale/categories/women/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

thescrap = soup.select('div.product_info')

name = soup.select('div.product-name')
prices = soup.select('div.price')
sales = soup.select('span.value')
department = "SALE Woman"

_temp_ = []

for _ in thescrap:
    _temp_.append(_.text)

    df = pd.DataFrame(data=_temp_)

df.to_pickle("./test1.pkl")

unpickled_df = pd.read_pickle("./test1.pkl")
print(unpickled_df)

#with open("./test1.pkl", "rb") as f:
#    object = pkl.load(f)
#df = pd.DataFrame(object)
#df.to_csv(r'./file.csv')
