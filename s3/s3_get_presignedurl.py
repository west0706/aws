#!/usr/bin/python
# -*- coding: utf-8 -*-
import boto3

# emdp-qd-s3-admin
s3 = boto3.client(
	's3',
	aws_access_key_id='',
	aws_secret_access_key=''
	)


pre = s3.generate_presigned_url(
	'get_object', 
	Params={'Bucket':'mdp-qd-s3-seoul', 
			'Key':'KR/IM_COF/1.XLS'
			},
	ExpiresIn=3600,	#Second
	HttpMethod='GET')

print pre


