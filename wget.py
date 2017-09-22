#!/usr/bin/python
# -*- coding: cp949 -*-

import urllib2
import time


while True:
	response = urllib2.urlopen('http://gmdpapi.eland.co.kr:8001')
	code = response.getcode()
	print code
	#html = response.read()
	#print html
	time.sleep(10)
