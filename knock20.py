# coding: utf-8

import json
import codecs


f=codecs.open("jawiki-country.json","r","utf-8")


for line in f:
    article=json.loads(line)
    if article["title"]==u"イギリス":
        print (article["text"])
