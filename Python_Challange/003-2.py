#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import re
line = ""

myfile = open("./003-bodyguard.txt")
line1 = myfile.readline()
while line1:
	line = line + line1[:-1]
	line1 = myfile.readline()
myfile.close()
print line

searchObj = re.finditer("[a-z][A-Z][A-Z][A-Z]([a-z])[A-Z][A-Z][A-Z][a-zs]",line)
for search in searchObj:
	print search.group(1)
