# coding: utf-8

import json
import codecs

def findTitleFromJson(title):
    f=codecs.open("jawiki-country.json","r","utf-8")
    for line in f:
        article=json.loads(line)
        if article["title"]==title:
            return article["text"]

    return ""



lines = findTitleFromJson("イギリス").split("\n")

for line in lines :
    if "Category" in line :
        print (line)
