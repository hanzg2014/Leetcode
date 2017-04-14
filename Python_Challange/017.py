#coding:utf8
#!/usr/bin/python

from urllib2 import Request, build_opener, HTTPCookieProcessor, HTTPHandler
import urllib
import cookielib
import re
import bz2
import xmlrpclib

cj = cookielib.CookieJar()
opener = build_opener(HTTPCookieProcessor(cj), HTTPHandler)
f = opener.open("http://www.pythonchallenge.com/pc/def/linkedlist.php")
html = f.read()
for cookie in cj:
    print cookie





##########################################################
# http://www.pythonchallenge.com/pc/return/balloons.html #
##########################################################

