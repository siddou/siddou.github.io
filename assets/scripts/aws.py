#!/usr/bin/python3
import boto3
from botocore.exceptions import ClientError
#import sys

#better print
#import json
#print ('""', json.dumps(response, indent=2, sort_keys=True))

#get-caller-identity
client = boto3.client('sts')
response = client.get_caller_identity()
#print(response['Account'])

# Retrieves all regions/endpoints that work with EC2
ec2 = boto3.client('ec2')
response = ec2.describe_regions()
#print(response['Regions'])

# Retrieves availability zones only for region of the ec2 object
response = ec2.describe_availability_zones()
#print(response['AvailabilityZones'])

# describe_security_group
SECURITY_GROUP_ID = "sg-03cd59f6b8de46004"
try:
    response = ec2.describe_security_groups(GroupIds=[SECURITY_GROUP_ID])
    #print(response)
except ClientError as e:
    print(e)

# create_security_group
SECURITY_GROUP_NAME = "EC2WebSecurityGroup"
DESCRIPTION = "Security Group for Web EC2 instances to allow port 22,80,443"

try:
    response = ec2.create_security_group(GroupName=SECURITY_GROUP_NAME,
                                         Description=DESCRIPTION)
    security_group_id = response['GroupId']
    print('Security Group Created %s.' % (security_group_id))

    data = ec2.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {'IpProtocol': 'tcp',
             'FromPort': 80,
             'ToPort': 80,
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
            {'IpProtocol': 'tcp',
             'FromPort': 443,
             'ToPort': 443,
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
            {'IpProtocol': 'tcp',
             'FromPort': 22,
             'ToPort': 22,
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
        ])
    #print('Ingress Successfully Set %s' % data)
except ClientError as e:
    print(e)

# delete_security_group
try:
    response = ec2.delete_security_group(GroupId=SECURITY_GROUP_ID)
    #print('Security Group Deleted')
except ClientError as e:
    print(e)

# Find the current Ubuntu Server 16.04 LTS AMI
try:
    response = ec2.describe_images(Owners=['099720109477'],
                                   Filters=[{
                                                'Name': 'name',
                                                'Values': ['ubuntu/images/hvm-ssd/ubuntu-xenial-16.04-amd64-server-????????']
                                   },
                                   {
                                                'Name' : 'state',
                                                'Values': ['available']
                                    }])
    sorted_obj = response
    sorted_obj["Images"] = sorted(response["Images"], key=lambda x : x["CreationDate"], reverse=True)
    #print (sorted_obj["Images"][0]["ImageId"])
except ClientError as e:
    print(e)

# instances
response = ec2.describe_instances()
#print(response)

# run-instances
ec2 = boto3.resource('ec2')

AMIIMAGEID = "ami-0370f4064dbc392b9"
KEYNAME = "test1"

try:
    instances = ec2.create_instances(
        ImageId=AMIIMAGEID,
        KeyName=KEYNAME,
        SecurityGroups=["EC2WebSecurityGroup",],
        InstanceType="t2.micro",
        Placement={'AvailabilityZone': 'eu-west-3c',}, 
        MaxCount=1,
        MinCount=1,
        Monitoring={
            'Enabled': True
        },
        TagSpecifications=[{
                            'ResourceType': 'instance',
                            'Tags': [
                                {'Key': 'webserver',
                                 'Value': 'production'}
                                    ]
                            },
                            {
                            'ResourceType': 'volume',
                            'Tags': [
                                {'Key': 'cost-center',
                            'Value': 'cc123'}
                                    ]
                            },
                          ]
        )
    for instance in instances:
        print("Instance '" + instance.id + "' created")
except ClientError as e:
    print(e)

# Stop, Terminate instances
ids = [instance.id, ]

# Wait for the instance to be in a running state or else stop_instance and create_snapshot wont work
try:
    instance = ec2.Instance(instance.id)
    instance.wait_until_running()
except ClientError as e:
    print(e)


# try:
#     #ec2.instances.filter(InstanceIds=ids).stop()
#     #ec2.instances.filter(InstanceIds=ids).terminate()
#     #print("Instance '" + instance.id + "' terminated")
# except ClientError as e:
#     print(e)


# Create tags
try:
    tag = ec2.create_tags(Resources=[instance.id], Tags=[{'Key':'Stack', 'Value':'production'}])
    #print (tag)
except ClientError as e:
    print(e)


session = boto3.Session(profile_name='default')
ec2 = session.client('ec2')

try:
    response = ec2.describe_instances(
            Filters=[
            {
                'Name': 'tag-key',
                'Values': ['Stack']
            },
        ],
    )
    #print (response)
except ClientError as e:
    print(e)


# EBS volume snapshot
## get volume id
client = boto3.client('ec2')

try:
    response = client.describe_volumes(
        Filters=[
            {
                'Name': 'attachment.instance-id',
                'Values': [
                    instance.id,
                ]
            },
            {
                'Name': 'attachment.device',
                'Values': [
                    '/dev/sda1',
                ]
            },
        ],
    )
    VOLUMEID = response["Volumes"][0]['VolumeId']
    #print (VOLUMEID)
except ClientError as e:
    print(e)


#aws ec2 create-snapshot
try:
    response = client.create_snapshot(
        Description='This is my root volume snapshot',
        VolumeId=VOLUMEID,
        TagSpecifications=[
            {
                'ResourceType': 'snapshot',
                'Tags': [
                    {
                        'Key': 'purpose',
                        'Value': 'prod'
                    },
                    {
                        'Key': 'costcenter',
                        'Value': 'cc123'
                    },
                ]
            },
        ],
    )
except ClientError as e:
    print(e)

# get latest snapshot id
try:
    response = client.describe_snapshots(
        Filters=[
            {
                'Name': 'volume-id',
                'Values': [
                    VOLUMEID,
                ]
            },
        ],

    )
    sorted_obj = response
    sorted_obj["Snapshots"] = sorted(response["Snapshots"], key=lambda k: k["StartTime"], reverse=True)
    SNAPSHOTID = sorted_obj["Snapshots"][0]["SnapshotId"]
    print ("Snapshot '" + SNAPSHOTID + "' created")
except ClientError as e:
    print(e)

# delete snapshot

ec2 = boto3.resource('ec2')
snapshot = ec2.Snapshot(SNAPSHOTID)
try:
    response = snapshot.delete(
    )
    print ("Snapshot " + SNAPSHOTID + " deleted")
except ClientError as e:
    print(e)

# Amazon EBS-backed AMI
AMINAME= 'An AMI for my server'


ec2 = boto3.client('ec2')
client = boto3.client('ec2')

try:
    response = client.create_image(
            InstanceId=instance.id,
            Name=AMINAME,
            NoReboot=True)
    print ("image created")
except ClientError as e:
    print(e)


try:
    response = ec2.describe_images(Owners=['self'],
                                   Filters=[{
                                                'Name': 'name',
                                                'Values': [AMINAME]
                                   }])
    sorted_obj = response
    sorted_obj["Images"] = sorted(response["Images"], key=lambda x : x["CreationDate"], reverse=True)
    AMIIMAGEID= sorted_obj["Images"][0]["ImageId"]
    print (AMIIMAGEID)
except ClientError as e:
    print(e)


ec2 = boto3.resource('ec2')

# run instance from ami
try:
    instances = ec2.create_instances(
        ImageId=AMIIMAGEID,
        KeyName=KEYNAME,
        SecurityGroups=["EC2WebSecurityGroup",],
        InstanceType="t2.micro",
        Placement={'AvailabilityZone': 'eu-west-3c',}, 
        MaxCount=1,
        MinCount=1,
        Monitoring={
            'Enabled': True
        },
        TagSpecifications=[{
                            'ResourceType': 'volume',
                            'Tags': [
                                {'Key': 'cost-center',
                            'Value': 'cc123'}
                                    ]
                            },
                          ]
        )
    for instance in instances:
        print("Instance '" + instance.id + "' created")
except ClientError as e:
    print(e)

# deregister-image
ec2 = boto3.client('ec2')
client = boto3.client('ec2')

try:
    response = client.deregister_image(
        ImageId=AMIIMAGEID,
    )
    print ("AMI " + AMIIMAGEID + " deregistered")
except ClientError as e:
    print(e)