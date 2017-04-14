#coding: utf8
#!/usr/bin/python
import os
import re
from PIL import Image

i = Image.open("./oxygen.png")
print i.size[0], i.size[1]
x = 0
#while (x<i.size[0]):
#	print i.getpixel((x,50))
#	x+=7

row = [i.getpixel((x,50)) for x in range (0, i.size[0], 7)]
#print row
ords = [r for r, g, b, a in row if r == g == b]
#print ords
print "".join(map(chr, map(int, map(int,re.findall("[0-9]+",("".join(map(chr, ords))))))))

#print re.findall("\d+", "".join(map(chr, ords)))