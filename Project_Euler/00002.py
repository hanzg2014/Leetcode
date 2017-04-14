#!/usr/bin/python
# -*- coding:utf-8 -*-


fib = []
fib.append(1)
fib.append(2)
i = 0
Sum = 0
while (fib[i] < 4000000):
	fib.append(fib[i]+fib[i+1])
	if (i % 3 == 1):
		Sum = Sum + fib[i]
	i+=1

print fib
print Sum