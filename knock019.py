#coding:utf-8

import codecs
from collections import Counter

f=codecs.open("hightemp.txt","r","utf-8")
str=[]
first_column=[]
counter=[]


for line in f:
    # print line
    str.append(line)

for s in str:
    # print (s[ ])
    first_column.append(s.split("\t")[0])
    # print(first_column)
#     print(counter)



cnt=Counter(first_column)

for word in cnt.most_common():
    print (word)
