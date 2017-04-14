#coding: utf8
#!/usr/bin/python
from xml.dom import minidom
import urllib2
import urllib2, pickle
 
url = 'http://www.pythonchallenge.com/pc/def/banner.p'
data = pickle.loads(urllib2.urlopen(url).read())
#for line in data:
#    print ''.join(elmt[0] * elmt[1] for elmt in line)
print data
for datum in data:
#	i = 0
#	while (i<datum[0][1]):
	output = ""
	for datumm in datum:
		output=output+(datumm[0]*datumm[1])
	print output

######################################################
# http://www.pythonchallenge.com/pc/def/channel.html #
######################################################