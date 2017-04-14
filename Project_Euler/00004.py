#!/usr/bin/python
# -*- coding:utf-8 -*-

def reverse(n):
    result = 0
    while n:
        result = result * 10 + n % 10
        n //= 10
    return result

lrg = 0
lrg1 = 0
i = 100

while(i<1000):
	j = 100
	while(j<1000):
		if (reverse(i*j) == i*j):
			lrg = i*j
			if (lrg > lrg1):
				lrg1 = lrg
				print lrg1
		j+=1
	i+=1




