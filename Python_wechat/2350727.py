#coding:utf8
#!/usr/bin/python

#Chained Comparison
mynumber = 3
if 4 > mynumber > 2:
    print("Chained comparison operators work! \n" * 3)

mylist = ["show","me","the","money"]
for index, value in enumerate(mylist):
    print index,value

from collections import Counter
from random import randrange
import pprint

mycounter = Counter()

for i in range(100):

    random_number = randrange(10)
    mycounter[random_number] += 1

for i in range(10):
    print(i, mycounter[i])


#reversed_dict()
my_phrase = ["No", "one", "expects", "the", "Spanish", "Inquisition"]
my_dict = {key: value for value, key in enumerate(my_phrase)}
#乱顺序？
print "my_dict:", my_dict
print "\n"
print "my_dict.items():", my_dict.items()
print "\n"
reversed_dict = {value: key for key, value in my_dict.items()}
print "reversed_dict:", reversed_dict
print "\n"


#python2 and python3 
    #from __future__ import print_function
    #from __future__ import division

    #mynumber = 5

    #print "Python 2:"
    #print "The number is %d" % (mynumber)

    #print mynumber / 2,
    #print mynumber // 2

    #print('nPython 3:')
    #print("The number is {}".format(mynumber))

    #print(mynumber / 2, end=' ')
    #print(mynumber // 2)

#C Braces
    #from __future__ import braces
    #File "", line 1
    #from __future__ import braces
    #SyntaxError: not a chance


#get and iteritem
my_dict = {'name': 'Lancelot', 'quest': 'Holy Grail', 'favourite_color': 'blue'}
print(my_dict.get('name', 'African or European?\n'))
print(my_dict.get('what', "default\n"))

for key, value in my_dict.iteritems():
    print(key, value)

#inspection tools
#dir(my_dict)
#help(my_dict)

#PEP-8
my_long_text = ("We are no longer the knights who say Ni! "
                "We are now the knights who say ekki-ekki-"
                "ekki-p'tang-zoom-boing-z'nourrwringmm!")
print(my_long_text2)