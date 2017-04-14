#!/usr/bin/python
# -*- coding:utf-8 -*-

def isprime(i):
	j=2
	while(j<i):
		if (i%j!=0):
			j+=1
		else:
			return False
	return True

result = []

i = 2
j = 0
while(True):
	if isprime(i):
		result.append(i)
		j+=1
		if (j==10001):
			print result[-1]
			break
	i+=1

