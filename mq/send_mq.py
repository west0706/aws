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


conn = stomp.Connection(host_and_ports=[('b-04b4eb30-c958-4da7-9e58-78e581a1eae1-1.mq.us-east-1.amazonaws.com',61614)])
print('set up Connection')
print conn

conn.set_listener('', MyListener())
print('set up Listener')

conn.start()
print('started connection')

conn.connect('service', 'tkfkddmldhkd123')
#conn.connect()
print('connected!')

conn.subscribe(destination='/test-stomp', id=1, ack='auto')

conn.send(body=' '.join(sys.argv[1:]), destination='/test-stomp')

time.sleep(2)
#except Exception, e:

conn.disconnect()

