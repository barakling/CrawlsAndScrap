import certifi
from bs4 import BeautifulSoup
import requests
from lxml import html
import pandas as pd
import pickle as pkl
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#declaring ZEREM attribtues.
class SaleItemsExtract(object):
    def __init__(self,  Makat, Makat_Desc, Makat_Price, Makat_Category):
        self.Makat = Makat
        self.Makat_Desc = Makat_Desc
        self.Makat_Price = Makat_Price
        self.Makat_Category = Makat_Category
        #self.department = department

#--------------------------------------------------------------------------------------------------------------------            

#Itsi Bitsy
url = 'https://www.aldoshoes.co.il/cis/cis-women/footwear/sandals/high-heels-sandals/valerria-light-purple-ladies-sandals-dress-fashion-high.html'
page = requests.get(url, verify=False)
tree = html.fromstring(page.content) 
#get data to variables
Makat = tree.xpath('//*[@id="product_addtocart_form"]/div[2]/div[1]/div[2]/div/div[2]/span/span[2]/text()')
Makat_Desc = tree.xpath('//*[@id="product_addtocart_form"]/div[2]/div[1]/div[2]/div/div[2]/span/span[1]/text()')
Makat_Price = tree.xpath('//*[@id="product-price-703253"]/text()')
Makat_Category = tree.xpath('//*[@id="product_addtocart_form"]/div[2]/div[1]/div[2]/div/div[1]/div/span[1]/text()')
#Cleaning
Makat_Clean = [item.replace("'", "") for item in Makat]
Makat_Price_Clean = [item.replace(" ", "") for item in Makat_Price]
Makat_Price_Clean = [item.replace("\n", "") for item in Makat_Price_Clean]
Makat_Price_Clean = [item.replace("₪", "") for item in Makat_Price_Clean]
Makat_Category = [item.replace(" ", "") for item in Makat_Category]
Makat_Category = [item.replace("\n", "") for item in Makat_Category]
#variables to Dict
dict2 = {}
dict2["מחלקה"] = str(Makat_Category).replace("'"," ")[1:-1]
dict2["ברקוד"] = str(Makat_Clean).replace("'"," ")[1:-1]
dict2["מותג"] = str(Makat_Desc).replace("'"," ")[1:-1]
dict2["מחיר_חדש"] = str(Makat_Price_Clean).replace("'"," ")[1:-1]
print(dict2)
#Dict to pickle dtp
dtp = open('Aldo_Shoes_1.pkl', 'wb')
pkl.dump(dict2, dtp)
dtp.close()
dtp2 = open('Aldo_Shoes_base.pkl', 'wb')
pkl.dump(dict2, dtp2)
dtp2.close()
dtp_af_pkl = pd.read_pickle("Aldo_Shoes_1.pkl")
dtp_af_pkl2 = pd.read_pickle("Aldo_Shoes_base.pkl")
##print(dtp_af_pkl==dtp_af_pkl2)
#Pickle to Dict
##unpickled_dtp = pd.read_pickle("Aldo_Shoes_base.pkl")


if dtp_af_pkl == dtp_af_pkl2:
    print("same")
    send_simple_message()
elif unpickled_dict_to_file != dict2:
    print("changed")


###### Distribution Class #######

# to mail
#--------------------------

mail_content = f"""
יש לי חדשות טובות בשבילך ♫
{dict2}  
אהבת? :) 

קישור אם בא לך להביט
{url}
"""
#The mail addresses and password
sender_address = 'my.private.selector@gmail.com'
sender_pass = 'Ag134679'
receiver_address = 'ling.barak@gmail.com'
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = f'התקבל מחיר חדש ל{dict2["מחלקה"]}'   #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')

###### END Distribution #######


#print(type(dict2))

#unpickled_dict_to_file = pd.read_pickle("Aldo_Shoes_base.pkl")
#print(type(unpickled_dict_to_file2))

"""print(dict2==unpickled_dict_to_file)

if unpickled_dict_to_file == dict2:
    print("same")
    send_simple_message()
elif unpickled_dict_to_file != dict2:
    print("changed")"""
    


"""unpickled_dict_to_file = pd.read_pickle("Aldo_Shoes_1.pkl")
unpickled_dict_to_file2 = pd.read_pickle("Aldo_Shoes_base.pkl")
print(unpickled_dict_to_file)
print(unpickled_dict_to_file2)"""
