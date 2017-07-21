# coding:  UTF-8

# "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
# という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
# それ以外の単語は先頭に2文字を取り出し，
# 取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

input ='Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
use_first_char=[1,5,6,7,8,9,15,16,19]
genso={}
print input

# input=input.replace(',','').replace('.','');
split_str=input.split(' ')
for (i,s) in enumerate(split_str,1):
    if i in use_first_char:
        genso[s[0]]=i
    else:
        genso[s[0:2]]=i

print genso

#辞書オブジェクトの使い方を覚えた
#enumerate()を用いると、オブジェクトと数値を同時にループできる
