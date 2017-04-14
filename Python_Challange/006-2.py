#coding: utf8
#!/usr/bin/python
import os
import re
import zipfile 

#filename = "90052"
#while(1):
#	f = open("channel/"+filename + ".txt")          # 返回一个文件对象
#	line = f.readline()   
#	searchObj = re.search("[0-9]+", line)
#	print searchObj.group()
#	filename = searchObj.group()
f=zipfile.ZipFile("./channel.zip")
print f.infolist()
print f.namelist()
#print f.read("readme.txt")
#f.read("90052.txt")
#f.read("%s.txt" % p)
p = "90052"
info = []
try:
	while(1):
			searchObj = re.search("([0-9]+)",f.read(p+".txt"))
			p = searchObj.group()
			info.append(f.getinfo(p+".txt").comment)
except:
	print "".join(info)
#p = "90052"
#print p+".txt"
#searchObj = re.search("([0-9]+)",f.read(p+".txt"))
#p = searchObj.group()
#print p+".txt"
#print f.read("46145.txt")

	#print name
#	print ""+f.getinfo(name).comment


#f.read(p) "Next nothing is 94191"