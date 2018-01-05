#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import sys
import stomp

class MyListener(stomp.ConnectionListener):

	def on_error(self, headers, message):
		print('received an error "%s"' % message)

	def on_message(self, headers, message):
		print('received a message "%s"' % message)

	def on_disconnected(self):
		print 'lost connection'


conn = stomp.Connection([('b-9ed7ac09-27d9-47f9-8bf7-bcd052d7ee2a-1.mq.us-east-1.amazonaws.com',61614)])
print('set up Connection')
print conn

conn.set_listener('', MyListener())
print('set up Listener')

conn.start()
print('started connection')

conn.connect('admin', 'wnsduq123456')
#conn.connect(wait=True)

print('connected!')

"""
try:
	conn.subscribe(destination='/active01', id=1, ack='auto')
	print 1111
except Exception, e:
	print e
"""

res = conn.send(destination='/stomp', body='This is message',id=1)
print res
conn.disconnect()

