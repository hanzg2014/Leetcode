#coding: utf8
#!/usr/bin/python
from xml.dom import minidom
import urllib2
import re

line = "82682"
#while(1):
#	resp = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+line).read()
#	searchObj = re.search("[0-9]+", resp)
#	print searchObj.group()
#	line = searchObj.group()

#	print searchObj.group(1)
#	line = searchObj.group(1)

while(1):
	resp = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+line).read()
	searchObj = re.finditer("([0-9]+)", resp)
	for search in searchObj:
		print search.group(1)
		line = search.group(1)


###################################################
# http://www.pythonchallenge.com/pc/def/peak.html #
###################################################



