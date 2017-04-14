#!/usr/bin/python
# -*- coding:utf-8 -*-

i = 0
Sum = 0

while (i<1000): 
    if (i % 3 == 0 or i % 5 == 0):
        Sum = Sum + i
    i+=1

print Sum


