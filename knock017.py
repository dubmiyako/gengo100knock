#coding:utf-8

import codecs

f=codecs.open("hightemp.txt","r","utf-8")
str=[]
first_char=[]

for line in f:
    # print line
    str.append(line.replace("\t"," "))

for s in str:
    # print (s[1])
    first_char.append(s[1])

char_sets=set(first_char)

print (char_sets)
