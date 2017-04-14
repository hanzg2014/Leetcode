#coding: utf8
#!/usr/bin/python
import string
import io
# program without string operations

def say(a):

	b = []
	lg = len(a)
	i = 0
	j = 0
	k = 0 
	idx = a[i]
	while (i<lg):
		idx = a[i]
		while (a[i] == idx):
			k+=1
			i+=1
			if (i == lg):
				break
		b.append(k)
		b.append(idx)
		k = 0

		#b[2*j-1]=idx
		#b[2*(j-1)]=k
	return b


a = [1]
print a[0]
print len(a)
i = 0
while (i<30):
	a=say(a)	
	print "a[i]%d" %(i+1)
	print len(a)
	i+=1
