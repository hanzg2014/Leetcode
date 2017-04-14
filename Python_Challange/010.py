#coding: utf8
#!/usr/bin/python

# program without string operations
def sign(n): 
	return cmp(n, 0)
def say(a):
	r = 0
	p = 0
	while a > 0:
		c = 3 - sign((a % 100) % 11) - sign((a % 1000) % 111)
		r += (10 * c + (a % 10)) * 10**(2*p)
		a /= 10**c
		p += 1
	return r

a = 1
for i in xrange(1, 31):
	print i, a
	a = say(a)

b = str(a)
print len(b)

###################################################
# http://www.pythonchallenge.com/pc/def/5808.html #
###################################################
