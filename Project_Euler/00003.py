#!/usr/bin/python
# -*- coding:utf-8 -*-

result = []
i = 1
while (i<600851475143):
	if (600851475143 % i == 0 and i <= 600851475143/2):
		result.append(i)
	i+=1
print result[-1]
