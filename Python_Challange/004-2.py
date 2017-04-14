#!/usr/bin/python
# -*- coding:utf-8 -*-

import urllib
import urllib2
import re

number = "37278"
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
while(1):
	print number
	response = urllib2.urlopen(url + number)
	html = ""+ response.read()
	searchObj = re.search("[0-9]+",html)
	number = searchObj.group()



