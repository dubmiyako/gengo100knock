# coding:  UTF-8


p=u'パトカー'
t=u'タクシー'
char=[]
i=0
while i < len(p+t)/2:
    char.append(p[i])
    char.append(t[i])
    i+=1

str="".join(char)
print(str)

#繰り返し処理をどうするかで悩んだ
#もっと良い方法があるはず
