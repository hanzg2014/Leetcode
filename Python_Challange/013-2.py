#coding: utf8
#!/usr/bin/python

import xmlrpclib
url = 'http://www.pythonchallenge.com/pc/phonebook.php'
phonebook = xmlrpclib.Server(url)
print phonebook.system.listMethods()
print "\n"
print phonebook.phone("Bert")
