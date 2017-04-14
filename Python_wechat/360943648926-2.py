#coding:utf8
#!/usr/bin/python
#http://chuansong.me/n/360943648926

import time
import urllib2
import threading 
 
class geturlThread(threading.Thread):
    def __init__(self, url):
        self.url = url
        super(geturlThread,self).__init__()
    def run(self):
        resp = urllib2.urlopen(self.url)
        print self.url, resp.getcode()

def get_responses():
    urls = [
        'http://www.google.com',
        'http://www.ebay.com',
        'http://www.alibaba.com',
    ]
    start = time.time()
    threads = []
    for url in urls:
        t = geturlThread(url)
        threads.append(t)
        t.start()

    for t in threads:
        t.join() 
    #print out the time when all threads end
    print "Elapsed time: %s" % (time.time()-start)
 

get_responses()