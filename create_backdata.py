# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 22:07:05 2018

@author: Kawin-PC
"""

import pandas as pd

#first section create city data

index_country=list(range(18))
name_country=['Ratchatevi','Siam_Su','Chitlom','Plenjit','Nana','Asok','Prompong',
              'Field','Siam_Si','Saladang','Nontri','Samyan','Silom','Lumpini','Klongtoel',
              'Sirikit','Sukumwit','Petchburi']
print(len(index_country),len(name_country))
d={'index':index_country,'country_name':name_country}
data=pd.DataFrame(data=d)
data.to_csv("country_mini.csv",index=False)

train_name=['BTS สายสีเขียว','BTS สายสีส้ำเงิน','mrt','int1','int2','int3']
train_type=['bts','bts','mrt','int','int','int']
train_location=[[0,1,2,3,4,5,6],[7,8,9,10],[11,12,13,14,15,16,17],[1,8],[5,16],[9,12]]
d={'train_name':train_name,'train_type':train_type,'train_location':train_location}
data=pd.DataFrame(data=d)
data.to_csv("trainLine_mini.csv",index=False)

price={}
i='BTS Silom Line'
price[i]=[]
price[i].append(16)
price[i].append(16)
price[i].append(26)
price[i].append(30)
price[i].append(33)
price[i].append(37)
price[i].append(40)
for j in range(7,17):
    price[i].append(44)
for j in range(17,24):
    price[i].append(59)
i='BTS Sukhumvit Line'
price[i]=price['BTS Silom Line']
price[i][2]=23

i='MRT'
#price[i]=[]
price[i]=[16,16,19,21,23,25,28,30,32,35,37,39]

i='ARL'
w=[16,16,26,30,33,37,40]
for j in range(7,17):
    w.append(44)
for j in range(17,24):
    w.append(59)
    
x=[16,16,23,30,33,37,40]
for j in range(7,17):
    x.append(44)
for j in range(17,24):
    x.append(59)
    
y=[16,16,19,21,23,25,28,30,32,35,37,39]
for i in range(len(y),len(w)):
    y.append("")
z=[15,15,20,25,30,35,40,45]
for i in range(len(z),len(w)):
    z.append("")
#price[i]=[]
price={'BTS Silom Line':w,'BTS Sukhumvit Line':x,'MRT':y,'ARL':z}
print(price)
d=pd.DataFrame(data=price)
d.to_csv("trainPrice.csv",index=False)