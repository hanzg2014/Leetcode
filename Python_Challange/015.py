#coding: utf8
#!/usr/bin/python

import datetime

def leap(year):
    if (year % 400 == 0):
        return True
    elif(year % 4 == 0 and year % 100 != 0):
        return True
    elif(year %100 ==0 and year %400 != 0):
        return True
    else:
        return False

years = [y for y in range(1006,1997) if str(y)[-1] == "6" and leap(y)]
print years

years2=[]

for y in years:
	d = datetime.date(y,1,27)
	if d.weekday()==1:
		years2.append(y)
		
print years2

#####################################################
# http://www.pythonchallenge.com/pc/def/mozart.html #
#####################################################
