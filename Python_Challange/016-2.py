#coding: utf8
#!/usr/bin/python

from PIL import Image
import numpy as np  

magnate=[]
im = Image.open("./mozart.gif")
im2 = np.array(list(im.getdata())).reshape((640,480))
w,h = im.size
for j in range(h):
    for i in range(w-5):
        if (im.getpixel((i,j))==195 and im.getpixel((i+4,j))==195):
            magnate.append([i,j])
print magnate
#print im2
#print magnate
im3 = Image.new(im.mode, (640,480),0)

for k in range(h):
    for l in range(640 - int((magnate[k])[0])):
        im3.putpixel((l,k), im.getpixel((l + int((magnate[k])[0]),k)))
    for m in range(640 - int((magnate[k])[0]),640):
        print m,k
        im3.putpixel((m,k), im.getpixel((m - 640 + int((magnate[k])[0]),k)))
        #im3.putpixel((m,k), 0)
            #im.getpixel((m - 479 - int((magnate[k])[0]),k)))
        #im3.putpixel((l,k), im.getpixel((l - 479 + int((magnate[k])[0]),k)))
im3.show()