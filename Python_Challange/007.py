#coding: utf8
#!/usr/bin/python
import os
import re
import zipfile
from PIL import Image

i = Image.open("./oxygen.png")

x=0
while (x<i.size[0]):
	print i.getpixel((x,45))
	x+=1

row = [i.getpixel((x, 50)) for x in range(0, i.size[0], 7)]
ords = [r for r, g, b, a in row if r == g == b]

print "".join(map(chr, map(int, re.findall("\d+", "".join(map(chr, ords))))))

#########################################################
# http://www.pythonchallenge.com/pc/def/integrity.html #
#########################################################

