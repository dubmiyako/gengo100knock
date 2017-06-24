# coding:  UTF-8


import sys

args = sys.argv

x=args[1]
y=args[2].decode('cp932')
z=args[3]
print args

print x+u"時の"+y+u"は"+z

#変数に格納された2バイト文字の文字化けを

#直す方法が分かり難かった
#winのコンソールの文字コード(CP932)をhoge.decode('文字コード')で
#Unicodeに変換する必要がある
