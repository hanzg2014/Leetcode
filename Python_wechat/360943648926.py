#coding:utf8
#!/usr/bin/python
#http://chuansong.me/n/360943648926

import time
import urllib2
 
def get_responses():
    urls = [
        'http://www.google.com',
        'http://www.ebay.com',
        'http://www.alibaba.com',
    ]
    start = time.time()
    for url in urls:
        print url
        resp = urllib2.urlopen(url)
        print resp.getcode()
    print "Elapsed time: %s" % (time.time()-start)
 
get_responses()


