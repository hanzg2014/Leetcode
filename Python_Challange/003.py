#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import re
#pattern = re.match(line,"[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]")

line = ""

f = open("bodyguard.txt")          # 返回一个文件对象
line1 = f.readline()   
          # 调用文件的 readline()方法
while line1:           # 后面跟 ',' 将忽略换行符
    line1 = f.readline()
    line = line+line1[:-1]
f.close()
print line
searchObj = re.finditer("[a-z][A-Z][A-Z][A-Z]([a-z])[A-Z][A-Z][A-Z][a-z]", line)

for search in searchObj:
	print search.group(1)


#########################################################
# http://www.pythonchallenge.com/pc/def/linkedlist.html #
#########################################################

