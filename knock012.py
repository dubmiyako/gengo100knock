#coding:utf-8

import codecs

f=codecs.open("hightemp.txt","r","utf-8")
str=[]

for line in f:
    # print line
    str.append(line)

f1=codecs.open("col1.txt","w","utf-8")
f2=codecs.open("col2.txt","w","utf-8")

for s in str:
    str_list=s.split("\t")
    # print (str_list[1])
    f1.write(str_list[1]+"\n")
    f2.write(str_list[2]+"\n")
f1.close()
f2.close()
