#coding: utf8
#!/usr/bin/python

from PIL import Image

# download the image from: http://www.pythonchallenge.com/pc/return/cave.jpg

image = Image.open("cave.jpg")
size = tuple(x for x in image.size)
odd = even = Image.new("RGB", size, (255,0,0,0))

for x in range (image.size[0]):
	for y in range (image.size[1]):
		if ((x+y)%2==1):
			image.putpixel((x,y), 0)
image.save("1.jpg")



###################################################
# http://www.pythonchallenge.com/pc/def/evil.html #
###################################################
