# coding: utf-8

import json
import codecs
import re

def findTitleFromJson(title):
    f=codecs.open("jawiki-country.json","r","utf-8")
    for line in f:
        article=json.loads(line)
        if article["title"]==title:
            return article["text"]

    return ""


tmp_dic = {}


lines = findTitleFromJson("イギリス").split("\n")

for line in lines :
    tmp_line = re.search("\|(.*) = (.*)",line)
    if tmp_line != None :
        tmp_dic[tmp_line.group(1)] = tmp_line.group(2)

for key,val in tmp_dic.items():
    print (key+"\t"+val)
