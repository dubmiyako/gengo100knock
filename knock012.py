#coding:utf-8

# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

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

# open()にて"w"を指定することでファイル書き込み(上書き)
