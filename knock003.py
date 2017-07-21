# coding:UTF-8

# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
# という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

input ='Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
split_str=[]
pi=[]
print input

input=input.replace(',','').replace('.','');
split_str=input.split(' ')
for s in split_str:
     pi.append(len(s))

print pi
