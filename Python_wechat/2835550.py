#coding: utf8
#!/usr/bin/python
s = 'Hello'
print s
print s[3]

print [i.upper() for i in "hello"]

str = "this is string example....wow!!!";
str = str.encode('utf-8','strict');

print "Encoded String: " + str;
print "Decoded String: " + str.decode('utf-8','strict')
#?encode用法？

s = "coffee"
print(s.find('f'))    # 从左至右搜索，返回第一个下标
print(s.rfind('f'))   # 从右至左搜索，返回第一个下表

print(s.find('a'))    # 若不存在则返回 -1
#print(s.index('a'))   # 若不存在则抛出 ValueError，其余与 find 相同

str = "0000000!!!this is string example....wow!!!0000000";
print str.strip( 'this' );

print(" hello world    ".strip(' '))
print("helloworld".strip("hed"))
print("["+"          i         ".lstrip() +"]")
print("["+"          i         ".rstrip() +"]")


print('''{}n{}n{}n{}n{}'''.format(
    "hello, WORLD".upper(),
    "hello, WORLD".lower(),
    "hello, WORLD".swapcase(),
    "hello, WORLD".capitalize(),
    "hello, WORLD".title()))

print("""
{}|{}
{}|{}
{}|{}
{}|{}
{}|{}
{}|{}
""".format(
    "Python".startswith("P"),"Python".startswith("y"),
    "Python".endswith("n"),"Python".endswith("o"),
    "i23o6".isalnum(),"1 2 3 0 6".isalnum(),
    "isalpha".isalpha(),"isa1pha".isalpha(),
    "python".islower(),"Python".islower(),
    "PYTHON".isupper(),"Python".isupper(),
))

print "101".zfill(8)

