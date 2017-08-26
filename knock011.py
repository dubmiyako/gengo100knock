#coding:utf-8

# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

import codecs

f=codecs.open("hightemp.txt","r","utf-8")
str=[]

for line in f:
    # print line
    str.append(line.replace("\t"," "))

for s in str:
    print (s)


# タブ文字が\tであることを忘れていたので時間がかかった
