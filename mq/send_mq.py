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


conn = stomp.Connection([('b-04b4eb30-c958-4da7-9e58-78e581a1eae1-1.mq.us-east-1.amazonaws.com',61614)])
print('set up Connection')
print conn

conn.set_listener('', MyListener())
print('set up Listener')

conn.start()
print('started connection')

# conn.connect('service','tkfkddmldhkd123')
conn.connect()
print('connected!')

"""
try:
	conn.subscribe(destination='/active01', id=1, ack='auto')
	print 1111
except Exception, e:
	print e
"""

res = conn.send(destination='/test-stomp', body='This is message',id=1)
print res
conn.disconnect()

