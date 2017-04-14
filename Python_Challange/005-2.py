#coding: utf8
#!/usr/bin/python
from xml.dom import minidom
import urllib2
import urllib2, pickle
 
myfile = open("./005-banner.p")
data = pickle.loads(myfile.read())

#for line in data:
#    print ''.join(elmt[0] * elmt[1] for elmt in line)
print data

for datum in data:
	output = ""
	for datumm in datum:
		output = output+datumm[0]*datumm[1]
	print output
######################################################
# http://www.pythonchallenge.com/pc/def/channel.html #
######################################################

