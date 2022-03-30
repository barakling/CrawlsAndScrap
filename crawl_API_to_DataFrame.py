
import requests
import json
import pandas as pd



head1 = "me head99"

api_url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(api_url)
p = response.json()
print("\n") 
print("wooooooow",p)

print(p["id"])
print(p["title"])

#print("Print each key-value pair from JSON response")
#for key, value in p.items():
        #print(key, ":", value)

print("\n")       

dataframe_1_df = pd.DataFrame({"head1" : range(8), "head3" : range(8,16), "head4" : "constant text", "Line_Number" : range(8), "Title" : p["title"], "Completed" : p["completed"] })
#print(dataframe_1)
dataframe_1_df.to_pickle("./test1.pkl")

unpickled_df = pd.read_pickle("./test1.pkl")
print(unpickled_df)


