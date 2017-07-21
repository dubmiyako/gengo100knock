# coding:  UTF-8

# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

input ="I am an NLPer"
split_str=[]
char_bigram=[]
split_str=input.split(' ')

str_sp_removed=input.replace(" ","")

for s in split_str:
     char_bigram.append(s)
print "##word bi-gram##"
i=0
while i<len(char_bigram)-1:
    print (char_bigram[i]+" "+char_bigram[i+1])
    i=i+1

str_sp_removed=input.replace(" ","")
print "##char bi-gram##"
i=0
while i<len(str_sp_removed):
    print str_sp_removed[i:i+2]
    i=i+1


#whileを2回回してるのが冗長な気がする
#単語と文字のbi-gramを1回で出力できないか？
