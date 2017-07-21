# coding:  UTF-8

# 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．

input = u"パタトクカシーー"
char=[]
i=1
for c in input:
    if i%2==1:
        char.append(c)
        # s+= str[i]
    i+=1
str="".join(char)
print (str)

# 文字を連結する処理に苦労した
# リストの要素は.join(char)で一つの文字列に変換できる
