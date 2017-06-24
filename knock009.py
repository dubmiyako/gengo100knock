# config:UTF-8

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
        print mid
        mid_list=list(mid)
        print mid_list
        sf= random.shuffle(mid_list)
        print sf
        # print first
        # print last
        char_list.append(first+mid+last)
    else:
        char_list.append(word)
print " ".join(char_list)
