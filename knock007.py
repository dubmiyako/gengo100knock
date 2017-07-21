# coding:  UTF-8

# 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
# さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．

import sys

args = sys.argv

x=args[1]
y=args[2].decode('cp932')
z=args[3]
print args

print x+u"時の"+y+u"は"+z

#変数に格納された2バイト文字の、文字化けを直す方法が分かり難かった
#winのコンソールの文字コード(CP932)をhoge.decode('文字コード')で
#Unicodeに変換する必要がある

#CP932：Shift-JISをもとに、拡張文字の追加を行ったもの
