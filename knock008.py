# coding:UTF-8
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
