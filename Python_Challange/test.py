#!/usr/bin/python
# -*- coding:utf-8 -*-
from string import maketrans   # 必须调用 maketrans 函数。

from string import maketrans

intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "cdefghijklmnopqrstuvwxyzab"
transtab = maketrans(intab, outtab)

str = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. 
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. 
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. 
lmu ynnjw ml rfc spj. """

print str.translate(transtab)


def caesar_decipher(str1,key):
    str2 = ""
    for ch in str1:
        if ("a"<=ch and ch <="z" or "A"<=ch and ch<="Z"):
            str2 = str2 + chr((ord(ch)+key-97)%26 + 97)
        else:
            str2 = str2 + ch
    print str2

str1 = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. 
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. 
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. 
lmu ynnjw ml rfc spj. """

str2 = "map"

caesar_decipher(str1, 2)
caesar_decipher(str2, 2)

