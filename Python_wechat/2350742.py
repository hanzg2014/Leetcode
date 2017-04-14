#coding:utf8
#!/usr/bin/python

from time import time 

#dict, list
t = time() 
list = ['a','b','is','python','jason','hello','hill','with','phone','test', 'dfdf','apple','pddf','ind','basic','none','baecr','var','bana','dd','wrd'] 
#list = dict.fromkeys(list,True) 
print list
filter = [] 
for i in range (1000000): 
    for find in ['is','hat','new','list','old','.']: 
        if find not in list: 
             filter.append(find) 
print "total run time:"
print time()-t

#list, set
t = time() 
lista=[1,2,3,4,5,6,7,8,9,13,34,53,42,44] 
listb=[2,4,6,9,23] 
intersection=[] 
print list()

for i in range (1000000): 
    for a in lista: 
        for b in listb: 
            if a == b: 
                intersection.append(a) 

print "total run time:"
print "list time:", time()-t

t = time() 
listb=[2,4,6,9,23] 
intersection=[] 

b = list(set(lista)&set(listb))
print b
#for i in range (1000000): 
#    list(set(lista)&set(listb)) 

print "total run time:"

print "set time:", time()-t



