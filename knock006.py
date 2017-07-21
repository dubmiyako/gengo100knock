# coding:  UTF-8

# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
# それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

def makeBiGram(s,l=[]):
    print "##char bi-gram##"
    i=0
    while i<len(s):
        l.append(s[i:i+2])
        i=i+1


str_x="paraparaparadise"
str_y="paragraph"
list_x=[]
list_y=[]


makeBiGram(str_x,list_x)
makeBiGram(str_y,list_y)
sets_x=set(list_x)
sets_y=set(list_y)
print "X: "
print sets_x
print "Y: "
print sets_y

print "UNION: "
print sets_x.union(sets_y)
print "DIFFERENCE X-Y: "
print sets_x.difference(sets_y)
print "DIFFERENCE Y-X: "
print sets_y.difference(sets_x)
print "INTERSECTION: "
print sets_x.intersection(sets_y)

print u"要素「se」が集合に存在するか？"
print "X: "
print "se" in sets_x
print "Y: "
print "se" in sets_y

# set()で集合(重複のない要素を持つリスト)を作ることができる
