#!/usr/bin/python
# -*- coding:utf-8 -*-

def sqr1(i):
	j=0
	Sum = 0
	while(j<=i):
		Sum=Sum+j*j
		j+=1
	return Sum

def sqr2(i):
	j=0
	Sum = 0
	while(j<=i):
		Sum=Sum+j
		j+=1
	return Sum*Sum

print sqr2(100) - sqr1(100)