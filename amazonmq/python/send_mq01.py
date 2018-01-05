#!/usr/bin/python

import stomp

class MyListener(object):
	def on_connecting(self, host_and_port):
		print 'connecting : %s:%s'%host_and_port

	def on_disconnected(self):
		print 'lost connection'

	def on_message(self, headers, body):
		self.__print_async('MESSAGE', headers, body)

	def on_error(self, headers, body):
		self.__print_async('ERROR', headers, body)

	def on_receipt(self, headers, body):
		self.__print_async('RECEIPT', headers, body)

	def on_connected(self, headers, body):
		print 'connected successfully'

	def __print_async(self, frame_type, headers, body):
		print '\r \r',
		print frame_type

	'''
	for header_key in headers.keys():
		print '%s: %s' % (header_key, headers[header_key])
	'''


#Inside Connection() is your server IP and STOMP port
conn = stomp.Connection([('b-04b4eb30-c958-4da7-9e58-78e581a1eae1-1.mq.us-east-1.amazonaws.com',61614)])
conn.set_listener('', MyListener())
conn.start()
#inside connect() is your ActiveMQ username and password
#conn.connect('service', 'tkfkddmldhkd123', wait=False)
conn.connect()
#inside send() there are destination and body.
# Destination is the Queue / Topic name, body is the message you want to send.
conn.send(destination='/active01', body='This is message', id=1)
conn.disconnect()
