# config:UTF-8

# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
# それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文
# (例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .")
# を与え，その実行結果を確認せよ．

import random

in_str="I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

first=""
last=""
mid=""
split_str=in_str.split(" ")
sf_str=""
char_list=[]

print in_str
for word in split_str:
    if len(word)>4:
        first=word[0]
        last=word[-1:]
        mid=word[1:len(word)-1]
        # print mid
        mid_list=list(mid)
        # print mid_list
        mid= "".join(random.sample(mid_list,len(mid_list)))

        # print first
        # print last
        char_list.append(first+mid+last)
    else:
        char_list.append(word)
print " ".join(char_list)


#ramdom.suffle(リスト)でリストの要素をシャッフルできるが、
#文字リストではNoneが帰ってくる
#random.sample(リスト,任意の長さ)/ランダムに要素をピックアップし任意の長さのリストに格納する
#でランダム文字列のリストを作成できる
