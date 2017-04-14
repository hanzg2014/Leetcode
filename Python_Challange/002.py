#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
line = ""

f = open("002-source.txt")          # 返回一个文件对象
line1 = f.readline()   
          # 调用文件的 readline()方法
while line1:           # 后面跟 ',' 将忽略换行符
    line = line+line1[:-1]
    line1 = f.readline()
f.close()

dict = {'Name': 'Rare'}

for ch in line:
	if  dict.has_key(ch):
		dict[ch]+=1
	else:
		dict[ch]=1

print dict.items()


#######################################################
# http://www.pythonchallenge.com/pc/def/equality.html #
#######################################################




