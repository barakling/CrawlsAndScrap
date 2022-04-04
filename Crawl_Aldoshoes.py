import certifi
from bs4 import BeautifulSoup
import requests
from lxml import html
import pandas as pd
import pickle as pkl

#Python class for declaring movie attribtues.
class SaleItemsExtract(object):
    def __init__(self,  Makat, Makat_Desc, Makat_Price):
        self.Makat = Makat
        self.Makat_Desc = Makat_Desc
        self.Makat_Price = Makat_Price
        #self.department = department


#to mail

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox911cc8290c0a4a61a39ff78382bff43e.mailgun.org/messages", verify=False,
       
        data={"from": "Mailgun Sandbox <postmaster@sandbox911cc8290c0a4a61a39ff78382bff43e.mailgun.org>",
            "to": "Barak Ling <ling.barak@gmail.com>",
            "subject": "Hello Barak Ling",
            "text": "Congratulations Barak Ling, you just sent an email with Mailgun!  You are truly awesome!"})
#--------------------------------------------------------------------------------------------------------------------            


page = requests.get('https://www.aldoshoes.co.il/cis/cis-women/footwear/sandals/high-heels-sandals/valerria-light-purple-ladies-sandals-dress-fashion-high.html', verify=False)
tree = html.fromstring(page.content) 

Makat = tree.xpath('//*[@id="product_addtocart_form"]/div[2]/div[1]/div[2]/div/div[2]/span/span[2]/text()')
Makat_Desc = tree.xpath('//*[@id="product_addtocart_form"]/div[2]/div[1]/div[2]/div/div[2]/span/span[1]/text()')
Makat_Price = tree.xpath('//*[@id="product-price-703253"]/text()')

Makat_Clean = [item.replace("'", "") for item in Makat]

Makat_Price_Clean = [item.replace(" ", "") for item in Makat_Price]
Makat_Price_Clean = [item.replace("\n", "") for item in Makat_Price_Clean]
Makat_Price_Clean = [item.replace("₪", "") for item in Makat_Price_Clean]

dict2 = {}

dict2["Makat"] = str(Makat_Clean)[1:-1]
dict2["Makat_Desc"] = str(Makat_Desc)[1:-1]
dict2["Makat_Price"] = str(Makat_Price_Clean)[1:-1]

#print(dict2)
#print(type(dict2))

unpickled_dict_to_file = pd.read_pickle("Aldo_Shoes_base.pkl")
#print(type(unpickled_dict_to_file2))

print(dict2==unpickled_dict_to_file)

if unpickled_dict_to_file == dict2:
    print("same")
    send_simple_message()
elif unpickled_dict_to_file != dict2:
    print("changed")
    


#dict_to_file = open('Aldo_Shoes_1.pkl', 'wb')
#dict_to_file2 = open('Aldo_Shoes_base.pkl', 'wb')
#pkl.dump(dict2, dict_to_file)
#dict_to_file.close()

#print(pkl.dumps('Aldo_Shoes_1.pkl') == pkl.dumps('Aldo_Shoes_base.pkl'))

"""unpickled_dict_to_file = pd.read_pickle("Aldo_Shoes_1.pkl")
unpickled_dict_to_file2 = pd.read_pickle("Aldo_Shoes_base.pkl")
print(unpickled_dict_to_file)
print(unpickled_dict_to_file2)"""

