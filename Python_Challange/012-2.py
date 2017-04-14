#coding: utf8
#!/usr/bin/python

import os
from PIL import Image

f=open("evil2.gfx",'rb')
contents = f.read()

print contents

for i in range(5):
	open("image"+str(i)+".dat","wb").write(contents[i::5])
