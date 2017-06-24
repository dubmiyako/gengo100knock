# coding:  UTF-8

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

# 文字を連結するのに苦労した
