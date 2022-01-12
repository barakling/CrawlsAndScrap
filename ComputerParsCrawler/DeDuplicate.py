#removing duplicates

from collections import OrderedDict

t = [1, 2, 3, 1, 2, 5, 6, 7, 8]

#dup
print(t)
#clean1
print(list(set(t)))
 
 #list minus list
s = [1, 2, 3]
print(list(set(t) - set(s)))

#clean2
print(list(OrderedDict.fromkeys(t)))
#clean3
print(list(dict.fromkeys(t)))
#clean4
res = []
for i in t:
    if i not in res:
        res.append(i)
print ("clean_4 : " + str(res))
#clean5
res2 = []
[res2.append(i) for i in t if i not in res2]
print ("clean_5 : " + str(res2))