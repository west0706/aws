#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boto3
import paramiko, time, datetime
import sys


#etl server info
etl_host = 'HOST_IP'
etl_userid = 'USER'
etl_userpw = 'PWD'

#dw rds info
TARGET_RDS = 'TARGET_RDS_NAME'

#time setting
yesterday = datetime.datetime.now() + datetime.timedelta(days=-1)
yesterday = yesterday.strftime('%Y-%m-%d')
RESTORE_TIME = yesterday + 'T18:00:00Z' # Today AM 03:00(UTC+9)


# Connect to ETL Server and Write log
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(etl_host, username=etl_userid, password=etl_userpw)

ftp = ssh.open_sftp()
file=ftp.file('PATH_TO_WRITE_LOG/etl.log', "a", -1)

file.write('\n' + 'RDS Restoring Ready...' + '\n')
file.write('> Start time: ' + time.strftime("%c")+'\n')
file.write('Restore point in time: ' + RESTORE_TIME  + ' UTC' + '\n')


# SNS to Slack
sns = boto3.client('sns', region_name='ap-northeast-2')


# Assume Role
sts_client = boto3.client('sts')

assumedRoleObject = sts_client.assume_role(
    RoleArn="ANOTHER_ACCOUNT_ROLE",
    RoleSessionName="ANOTHER_ACCOUNT_ROLE_SESSION_NAME",
    DurationSeconds=7200
)

credentials = assumedRoleObject['Credentials']

# RDS Restore
rds = boto3.client(
                'rds',
                region_name='ap-northeast-2',
                use_ssl=True,
                aws_access_key_id = credentials['AccessKeyId'],
                aws_secret_access_key = credentials['SecretAccessKey'],
                aws_session_token = credentials['SessionToken']
                )

try:
    file.write('RDS Restoring Started...' + time.strftime("%c") + '\n')

    try:
        response = sns.publish(
                TopicArn="SNS_TOPIC_ARN",
                #Subject='',
                Message='RDS NGCP-DW is creating... :coffee:'
                )
    except Exception, e:
        print str(e)


    result = rds.restore_db_instance_to_point_in_time(

    SourceDBInstanceIdentifier='SOURCE_RDS_INDENTIFIER',
    TargetDBInstanceIdentifier=TARGET_RDS,
    RestoreTime=RESTORE_TIME,
    UseLatestRestorableTime=False,
    DBInstanceClass='INSTANCE_TYPE',
    Port=,
    AvailabilityZone='ap-northeast-2a',
    DBSubnetGroupName='SUBNET_GROUP_NAME',
    MultiAZ=False,
    PubliclyAccessible=False,
    AutoMinorVersionUpgrade=False,
    LicenseModel='bring-your-own-license',
    DBName='',
    Engine='',
    # Iops=3000,
    OptionGroupName='OPTION_GROUP_NAME',
    CopyTagsToSnapshot=True,
    Tags=[
        {
            'Key': '...',
            'Value': '...'
        },
    ],
    StorageType='gp2',
    # TdeCredentialArn='string',
    # TdeCredentialPassword='string',
    # Domain='string',
    # DomainIAMRoleName='string'
    )


    #Waiter run    
    print('API call.. sleep 20sec..')
    time.sleep(20)

    status = rds.describe_db_instances(DBInstanceIdentifier=TARGET_RDS)['DBInstances'][0]['DBInstanceStatus']

    while status != 'available':
        print('still waiting..')
        print(status)
        time.sleep(10)
        print(time.strftime("%c"))
        status = rds.describe_db_instances(DBInstanceIdentifier=TARGET_RDS)['DBInstances'][0]['DBInstanceStatus']


    file.write('RDS Restoring Completed...' + time.strftime("%c") + '\n')

    file.write('> RDS Restoring Ended.' + '\n\n')
    file=ftp.file('PATH_TO_WRITE_LOG/success.log', "a", -1)

    try:
        response = sns.publish(
                TopicArn="SNS_TOPIC_ARN",
                Message='RDS Restoring Completed.'
                )
    except Exception, e:
        print str(e)

except Exception, e:
    file.write(str(e) +'\n')
    print str(e)
    try:
        response = sns.publish(
                TopicArn="SNS_TOPIC_ARN",
                Message=str(e)
                )
    except Exception, e:
        print str(e)


file.flush()
ftp.close()
ssh.close()

