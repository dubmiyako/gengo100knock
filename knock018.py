#coding:utf-8

import codecs

f=codecs.open("hightemp.txt","r","utf-8")
lines=[]
first_char=[]

for line in f:
    # print line
    lines.append(line.replace("\t"," "))

sorted_lines=sorted(lines, key=lambda x: x.split()[2])

for line in sorted_lines:
    print (line)
