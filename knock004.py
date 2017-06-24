# coding:  UTF-8


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
