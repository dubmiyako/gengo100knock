# coding:  UTF-8

# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．


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
#whileで回さなくても書ける方法がある気がする
