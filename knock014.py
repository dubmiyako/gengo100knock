#coding:utf-8

import codecs
import sys

args = sys.argv

print (args[1])

f=codecs.open("hightemp.txt","r","utf-8")
str=[]

for (line,i) in zip(f,range(0,int(args[1]))):
    # print line
    str.append(line.replace("\t"," "))

for s in str:
    print (s)

#int()でstrをintに変換
