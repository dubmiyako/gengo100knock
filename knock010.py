#coding:UTF-8

import codecs

f=codecs.open("hightemp.txt","r","utf-8")
strlist=[]

for line in f:
    # print line
    strlist.append(line)

print len(strlist)
