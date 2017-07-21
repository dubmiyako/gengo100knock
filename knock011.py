#coding:utf-8

import codecs

f=codecs.open("hightemp.txt","r","utf-8")
str=[]

for line in f:
    # print line
    str.append(line.replace("\t"," "))

for s in str:
    print (s)
