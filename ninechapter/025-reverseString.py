#coding:utf8
#!/usr/bin/python

s = "I can feel the love tonight"

def reverseString(s):
    s2 = s.split(" ")
    l = len(s2)
    for n in range(l/2):
        s2[n],s2[l-1-n] = s2[l-1-n],s2[n]       
    print s2

reverseString(s)
