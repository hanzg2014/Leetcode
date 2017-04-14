#coding:utf8
#!/usr/bin/python

a = set('boya')
a.add('python')
a.update("python")
a.remove('python')
print a

lista=[1,2,3,4,5,6,7,8,9,13,34,53,42,44] 
listb=[2,4,6,9,23] 
tuple = (2,3,4,5)

print list(a)

print set(listb)-set(lista)
print list(set(lista)&set(listb))
print set(lista)|set(listb)
print "#################################"
class myclass:
    def __init__(self, key, value):
            self.dict={}
            self.dict[key]=value
    def __setitem__(self,key,value):
            self.dict[key]=value
    def __getitem__(self,key):
            return self.dict[key]

myclass1 = myclass("key1", "value1")
print myclass1["key1"]
myclass1["key0"]= "value0"
print myclass1["key0"]
print "#################################"
class DictDemo:  
    def __init__(self,key,value):  
        self.dict = {}  
        self.dict[key] = value  
    def __getitem__(self,key):  
        return self.dict[key]  
    def __setitem__(self,key,value):  
        self.dict[key] = value  
    def __len__(self):  
        return len(self.dict)  
dictDemo = DictDemo('key0','value0')   
dictDemo['key1'] = 'value1'  
print(len(dictDemo)) #2  
print dictDemo.__getitem__("key0")


