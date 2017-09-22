#!/usr/bin/python
# -*- coding: utf-8 -*-
import boto3

# emdp-qd-s3-admin
s3 = boto3.client(
	's3',
	aws_access_key_id='AKIAJV5BOKVSIXYG42NQ',
	aws_secret_access_key='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'
	)


pre = s3.generate_presigned_url(
	'get_object', 
	Params={'Bucket':'mdp-qd-s3-seoul', 
			'Key':'KR/IM_COF/1.XLS'
			},
	ExpiresIn=3600,	#Second
	HttpMethod='GET')

print pre


