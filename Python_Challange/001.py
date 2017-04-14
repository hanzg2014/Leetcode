#!/usr/bin/python
# -*- coding:utf-8 -*-
import string


str1 = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
str2 = ""
def caesarCipher(s, key):  
	str2 = ""
	for ch in s:
		if ("a"<=ch and ch<="z" or "A"<=ch and ch<="Z"):
			ch1 = chr((ord(ch)-97+key)%26+97)
			str2 = str2 + ch1
		else:
			str2 = str2 + ch
	print str2
caesarCipher(str1,2)

##################################################
# http://www.pythonchallenge.com/pc/def/orc.html #
##################################################



