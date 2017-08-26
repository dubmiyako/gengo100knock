#coding:utf-8

# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

import codecs
str1=[]
str2=[]


f1=codecs.open("col1.txt","r","utf-8")
f2=codecs.open("col2.txt","r","utf-8")
f_merse=codecs.open("col_merse.txt","a","utf-8")

for (line1,line2) in zip(f1,f2):
    f_merse.write(line1.replace("\n","")+"\t"+line2)

f_merse.close()

# 元ファイルに改行文字があり、途中で改行されてしまうので
# "\n"をreplaceで消去している
