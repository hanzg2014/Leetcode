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

r=re.compile(r'(\d+)$') 

comment=[] 
nextnothing='90052' 
f=zipfile.ZipFile('./channel.zip') 
while(1): 
	try: 
		comment.append(f.getinfo('%s.txt' % nextnothing).comment) 
		nextnothing=r.search(f.read('%s.txt' % nextnothing)).group() 
	except: 
		print ''.join(comment) 
		break 

#####################################################
# http://www.pythonchallenge.com/pc/def/oxygen.html #
#####################################################
