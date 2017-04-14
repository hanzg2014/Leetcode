#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
line = ""

myfile = open("./002-source.txt")
line1 = myfile.readline()
while line1:
	line = line + line1[:-1]
	line1 = myfile.readline()
myfile.close()
print line

dict = {'key':'times'}
for ch in line:
	if dict.has_key(ch):
		dict[ch]+=1
	else:
		dict[ch]=1

print "%s" % dict.items()

