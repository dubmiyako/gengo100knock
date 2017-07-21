#coding:utf-8

import codecs
#
# f=codecs.open("hightemp.txt","r","utf-8")
str1=[]
str2=[]


f1=codecs.open("col1.txt","r","utf-8")
f2=codecs.open("col2.txt","r","utf-8")
f_merse=codecs.open("col_merse.txt","a","utf-8")

for (line1,line2) in zip(f1,f2):
    # print line
    # str1.append(line)
    # str2.append(line)
    f_merse.write(line1.replace("\n","")+"\t"+line2)

f_merse.close()

# for (s1,s2) in zip(str1,str2):
#     # print (str_list[1])
#     f_merse.write(str_list[1]+"\t"+str_list2[])
# f1.close()
# f2.close()
