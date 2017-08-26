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



lines = findTitleFromJson("イギリス").split("\n")

for line in lines :
    if "Category" in line :
        category_line = re.search("^\[\[Category:(.+?)(|\|.*)\]\]$",line)
        if category_line != None :
            print (category_line.group(1))
