# coding:UTF-8

# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
# ・英小文字ならば(219 - 文字コード)の文字に置換
# ・その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．

import sys

args= sys.argv

input_str=args[1]
out_str=""


for c in input_str:
    if c.islower():
        c=219-ord(c)
        out_str=out_str+chr(c)
    else:
        out_str=out_str+c
print out_str

#ord()で文字→ASCIIコード
#chr()でASCIIコード→文字に変換
