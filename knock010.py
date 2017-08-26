#coding:UTF-8

# 行数をカウントせよ．確認にはwcコマンドを用いよ．

import codecs

f=codecs.open("hightemp.txt","r","utf-8")
strlist=[]

for line in f:
    # print line
    strlist.append(line)

print len(strlist)


# codecs.open()で文字コードを指定してファイルを開く
