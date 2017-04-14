#coding:utf8
#!/usr/bin/python

def fizzbuzz(a,b):
    for n in range(a,b+1):
        print  "fizz"[n%3*4:]+"buzz"[n%5*4:] or n

fizzbuzz(1,100)
#for x in range(101):print"fizz"[x%3*4::]+"buzz"[x%5*4::]or x