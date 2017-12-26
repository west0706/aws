#!/usr/bin/python
# -*- coding: utf-8 -*-

import boto3

sqs = boto3.client('sqs')

queue_url = 'https://sqs.ap-northeast-2.amazonaws.com/980923263298/Basic-prd-queue-test'

#Send message to SQS queue
response = sqs.send_message(
		QueueUrl=queue_url,
		DelaySeconds=10,
		MessageAttributes={
			'Title':{
				'DataType':'String',
				'StringValue':'The Whistler'
			}
		},

		MessageBody=(
					'This is a sqs message test!!!'
					)
		)

print response


