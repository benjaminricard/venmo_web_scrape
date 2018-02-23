# -*- coding: utf-8 -*-
import requests
import json
from datetime import datetime
import csv
import time
import codecs
from urllib2 import urlopen
import sys
import urllib2
from random import randint
list = [TIME1, TIME2]
start = list[int(sys.argv[1])]
	# Initialize json objects, arrays
URL = "https://venmo.com/api/v5/public?until="+str(start)
req = urllib2.Request(URL, headers={ 'User-Agent': 'Mozilla/5.0' })
data= urllib2.urlopen(req).read().decode("utf-8")
venmo_api = json.loads(data)
venmo_info = []

	#returns next page from paging/next
def get_next_page(json):
    try:	    
	return json['paging']['next']
    except urllib2.HTTPError:
	time.sleep(500)
	f = open('errors'+'.txt','a')
	f.write('\n' + newURL)
	f.close()
#iterate over json objects
for i in range(1,10000000):
    try:
       try:
	    for j in range(0,20):
		lowerlvl = []
		lowerlvl.append(venmo_api['data'][j]['updated_time'])
		lowerlvl.append(venmo_api['data'][j]['actor']['username'])
		lowerlvl.append(venmo_api['data'][j]['transactions'][0]['target']['username'])
		lowerlvl.append(venmo_api['data'][j]['message'])
		lowerlvl.append(venmo_api['data'][j]['type'])
		venmo_info.append(lowerlvl)
       except TypeError:
	    pass
    except(TypeError, KeyError) as e:
	pass
    newURL = get_next_page(venmo_api)
    req = urllib2.Request(newURL, headers={ 'User-Agent': 'Mozilla/5.0' })
    data= urllib2.urlopen(req).read().decode("utf-8")
    venmo_api = json.loads(data)
    if len(venmo_info)>1000:
#append output to csv
	with open("output_"+str(start)+".csv", "a") as fp:
	    for i in venmo_info:
		xx = [x.encode('utf-8') for x in i]
		wr = csv.writer(fp)
		wr.writerow(xx)
	venmo_info=[]
	if int(newURL[-10:]) < int(list[int(sys.argv[1])+1]+1000):
		print "Done!"
		print newURL
		sys.exit()
#append newURL for logging purposes
print newURL
f = open('timestamp_'+str(start)+'.txt','a')
f.write('\n' + newURL)
f.close()
