#coding:utf-8

import codecs
import sys

args = sys.argv

print (args[1])

f=codecs.open("hightemp.txt","r","utf-8")

str=[]

for line in f:
    str.append(line)

str.reverse()

for (line,i) in zip(str,range(0,int(args[1]))):
    # print line
    print (line)



#int()でstrをintに変換
