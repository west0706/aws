#!/usr/bin/python
# -*- coding: utf-8 -*-

import boto3

sqs = boto3.client('sqs')
queue_url = 'https://sqs.ap-northeast-2.amazonaws.com/980923263298/Basic-prd-queue-test'

# Receive message from SQS queue

response = sqs.receive_message(
			QueueUrl=queue_url,
			AttributeNames=['All']			
		)


message = response['Messages'][0]
receipt_handle = message['ReceiptHandle']

print receipt_handle

# Delete received message from queue
sqs.delete_message(
		QueueUrl=queue_url,
		ReceiptHandle=receipt_handle
		)
print('Received and deleted message: %s' % message)
