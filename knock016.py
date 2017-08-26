#coding:utf-8

import codecs
import sys

args = sys.argv

print (args[1])

split_num = int(args[1])

f=codecs.open("hightemp.txt","r","utf-8")
hi_list = f.readlines()
line_list=[]
write_list=[]

# file_num=0
# for (line,i) in zip(hi_list,range(1,len(hi_list))):
#     if i%split_num==0:
#         # print (line_list)
#         write_list.append(line_list)
#         print("---------------------------------------------")
#         print(write_list)
#         line_list.clear()
#         print(line_list)
#     line_list.append(line)
# print("---------------------------------------------")
# print(write_list)
#
# for (li,i) in zip(write_list,range(0,len(write_list))):
#     f_split = codecs.open("split_temp"+str(i)+".txt","w","utf-8")
#     for s in li:
#         f_split.write(s)
#         print(write_list[i])

file_num=0
for (line,i) in zip(hi_list,range(1,len(hi_list))):
    if i%split_num==0:
        file_num = file_num+1
    f_split = codecs.open("split_temp"+str(file_num)+".txt","a","utf-8")
    f_split.write(line)


#"a"でファイル書き込みすると追記になってしまうので、何度も実行するとその度に追記されてしまう
#0番目とhi_list番目のファイルの行数が一つ足りない
#一旦リストに格納→一度に書き込み　を考えたが、Pythonのリストの仕様が分からず断念
#再トライしたい


#pythonのリスト使用について　参考　http://qiita.com/utgwkk/items/5ad2527f19150ae33322
