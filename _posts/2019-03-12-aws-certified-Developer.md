---
title:  "aws certified Developper"
tags:
  - aws
  - certification
---
{% include toc %}

## [Exam guide](https://d1.awsstatic.com/training-and-certification/docs-dev-associate/AWS_Certified_Developer_Associate_Updated_June_2018_Exam_Guide_v1.3.pdf){:target="_blank"}


### Domain 1: Deployment
#### 1.1 Deploy written code in AWS using existing CI/CD pipelines, processes, and patterns.
#### 1.2 Deploy applications using Elastic Beanstalk.
#### 1.3 Prepare the application deployment package to be deployed to AWS.
#### 1.4 Deploy serverless applications.
### Domain 2: Security
#### 2.1 Make authenticated calls to AWS services.
#### 2.2 Implement encryption using AWS services.
#### 2.3 Implement application authentication and authorization.
### Domain 3: Development with AWS Services
#### 3.1 Write code for serverless applications.
#### 3.2 Translate functional requirements into application design.
#### 3.3 Implement application design into application code.
#### 3.4 Write code that interacts with AWS services by using APIs, SDKs, and AWS CLI.
### Domain 4: Refactoring
#### 4.1 Optimize application to best use AWS services and features.
#### 4.2 Migrate existing application code to run on AWS.
### Domain 5: Monitoring and Troubleshooting
#### 5.1 Write code that can be monitored.
#### 5.2 Perform root cause analysis on faults found in testing or production.

### acloud.guru training
#### CHAPTER 1 Introduction

| Domain | % of Examination |
| Domain 1:Deployment | 22% |
| Domain 2: Security | 26% |
| Domain 3: Development with AWS Services | 30% |
| Domain 4: Refactoring | 10% |
| Domain 5: Monitoring and Troubleshooting | 12% |
| Total | 100% |

- 130 Minutes in Length
- 65 questions
- Results immediately
- Passmark is 720. Top Score 1000.
- $150 USD

12/02/2019
Hi - yes it is up to date for the latest exam. The exam was released in June 2018 and has not been refreshed since then,


[Tips](https://acloud.guru/forums/aws-cda-2018/discussion/-LVjFQsZd5s5_HLdVQrx/passed_developer_associate)

[Tips](https://acloud.guru/forums/aws-cda-2018/discussion/-LUk6O3fg_B3MvFP0feD/aws_certified_developer_-_asso)

[Tips](https://acloud.guru/forums/aws-cda-2018/discussion/-L_dBng3i_Y5NFJ7zPsY/cleared_out_aws_developer_asso)

[Tips](https://acloud.guru/forums/aws-certified-developer-associate/discussion/-KUdI5f2LNbi4wvK7v4I/how_to_pass_aws_certified_deve)

[Tips](https://acloud.guru/forums/aws-cda-2018/discussion/-LWDVxz601aEDRXyZS_P/passed_the_cda_exam_on_friday)

[Tips](https://acloud.guru/forums/aws-cda-2018/discussion/-LZRDTlcsGXtCh6EYIwY/passed:_cda_feb_2019)

#### CHAPTER 2 Beginners Guide to IAM
[AWS Security Best Practices](https://d1.awsstatic.com/whitepapers/Security/AWS_Security_Best_Practices.pdf){:target="_blank"}


##### IAM 101 Summary
IAM consists of the following:
- Users
- Groups (A way to group our users and apply polices to the collectively)
- Roles
- Policy Documents
- **IAM is universal**. It does not apply to regions at this time
- The "root account" is simply the account created when first setup your AWS account. It has complete Admin access.
- New Users have **NO permissions** when first created.
- New Users are assigned **Access Key ID & Secret Access Keys** when first created.
- These are not the same as a password, and you cannot use the Access key ID & Secret Access Key to login in to the AWS Management Console.
- You can use this to access AWS via the APIs and Command Line, however.
- You only get to view Access key ID & Secret Access Key once. If you lose them, you have to regenerate them. Do, save them in a secure location.
- Always setup Multifactor Authentication (MFA) on your root account.
- You can create and customise your own password rotation policies.

#### CHAPTER 3 Beginners Guide to EC2
##### EC2 Exam Tips
- On **Demand** - allows you to pay a fixed rate by the hour (or by the second) with no commitment.
- **Reserved** - provides you with a capacity reservation, and offer a significant discount on the hourly charge for an instance. 1 Year or 3 Year Terms.
- **Spot** - enables you to bid whatever price you want for instance capacity, providing for even greater savings if your applications have flexible start and end times.
- **Dedicated Hosts** - Physical EC2 server dedicated for your use. Dedicated hosts can help you reduce costs by allowing you use your existing server-bound software licences.
- If a Spot instances is terminated by Amazon EC2, you will not be charged for a partial hour of usage. However, if you terminate the instance yourself, you will be charged for the complete hour in which the instance ran.
- Different EC2 instances type: **FIGHT DR MC PX!**

SSD
- **General Purpose SSD** - balances price and performance for a wide variety of workloads.
- **Provisioned IOPS SSD** - Highest-performance SSD volume for mission-critical low-latency or high-throughput workloads

Magnetic
- **Throughput Optimized HDD** - Low cost HDD volume designed for frequently accessed, htoughtput-intensive worloads.
- **Cold HDD** - Lowest cost HDD volume designed for less frequently accessed worloads
- **Magnetic** - Previous Generation. Can be a boot volume.

##### ELB Exam Tips
- 3 Types of Load Balancer;
  - Application Load Balancers
  - Network Load Balancers
  - CLassic Load Balancers
- 504 Error means the gateway has timed out. This means that the application not responding within the idle timeout period.
  - Trouble shoot the application. Is it the Web Server or Database Server?
- If you need the IPV4 address of your end user, look for the X-Forwarded-For header.

##### Route53 Exam Tips
- Route 53 is Amazon's DNS service
- Allows you to map your domain names to
  - EC2 Instances
  - Load Balancers
  - S3 Buckets

##### CLI Exam Tips
- **Least Privilege** - Always give your users the minimum amount of access required.
- **Create Groups** - Assign your users to groups. Your users will automatically inherit the permissions of the group. The groups permissions are assigned using policy documents.
- **Secret Access Key** - You will see this only once. If you do not save it, you can delete the Key Pair (Access Key ID and Secret Access Key) and regenerate it. You will need to run **aws configure** again.
- **Do not use just one access key** - Do not create just one access key and share that with all your developpers. If someone leaves the company on bad terms, then you will need to delete the key and create a new one and every developer would the need to update their keys. Instead create one key pair per developer.
- **You can use the CLI on your PC** - You can install the CLI on Mac, Linux or Windows PC.

##### Exam Tips
- Roles allow you to not use Access Key ID's and Secret Access Keys
- Roles are preferred from a security perspective
- Roles are controller by policies
- You can change a policy on a role and it will take immediate affect
- You can attach and detach roles to running EC2 instances without having to stop or terminate these instances
- You can encrypt the root device volume (the volume the OS is installed on) using Operating System level encryption
- You can encrypt the root device volume by first take a snapshot of that volume, and thencreating a copy of that snap with encryption. You can then make an AMI of this snap and deploy the encrypted root device volume.
- You can encrypt additional attached volumes using the console, CLI or API

##### AWS Databases Types - Summary
- RDS - OLTP
  - SQL
  - MySQL
  - PostgreSQL
  - Oracle
  - Aurora
  - MariaDB
- DynamoDB - No SQL
- RedShift - OLAP
- Elasticache - In Memory Caching:
  - Memcached
  - Redis
- Multi-AZ - for Disaster Recovery only. It is not primarily used for improving performance. For performance improvement, you need Read Replicas.
- Read Replica Databases
  - Used for scaling, not DR!
  - Must have automatique backups turned on in order to deploy a read replica.
  - You can have up to 5 read replica copies of any database.
  - You can have read replicas of read replicas (but watch out for latency.)
  - Each read replica will have its own DNS endpoint.
  - You **can** have read replicas that have Multi-AZ
  - You **can** create read replicas of Multi-AZ source databases.
  - Read replicas can be promoted to be their own databases. This breaks the replication.
  - You can have a read replica in a second region (for MySQL and MariaDB.)

##### Elasticache Exam Tips
- Typically, you will be given a scenarion where a particular database is under a lot of stress/load. You may be asked which service you should use to alleviate this.
- Elasticache is a good choice if your database is particulary read-heavy and not prone to frequent changing.
- Redshift is a good answer if the reason your database is feeling stress is because management keep running OLAP transactions on it etc.
- Use Memcached if
  - Object caching is your primary goal
  - You want to keep things as simple as possible
  - You want to scale your cache horizontally (scale out)
- Use Redis if
  - You have advanced data types, such as lists, hashes, and sets.
  - You are doing data sorting and ranking (such as leader boards)
  - Data Persistence
  - Multi AZ
  - Pub/Sub capabilities are needed

#### CHAPTER 4 S3
https://aws.amazon.com/s3/faqs/

##### S3 101 - Summary
- Remember that S3 is Object-based: i.e. allows you to upload files.
- Files can be from 0 Bytes to 5 TB.
- There is unlimited storage.
- Files are stored in Buckets.
- S3 is a universal namespace. That is, names must be unique globally.
- https://s3-eu-west-1.amazonaws.com/acloudguru
- Read after Write consistency for PUTS of new objects
- Eventual Consistency for overwrite PUTS and DELETES (can take some time to propagate)
- S3 Storage Classes/Tiers:
  - S3 (durable, immediately available, frequently accessed)
  - S3 - IA (durable, immediately available, infrequently accessed)
  - S3 - One Zone IA: Same as IA. However, data is stored in a single Available Zone only
  - S3 - Reduced Redundancy Storage (data that is easily reproducible, such as thumbnails, etc.)
  - Glacier - Archived data, where you can wait 3 - 5 hours before accessing
- Remember the core fundamentals of an S3 object:
  - Key (name)
  - Value (data)
  - Version ID
  - Metadata
  - Subresources (used to manage bucket-specific configuration)
    - Bucket Policies, ACLs
    - CORS
    - Transfer Acceleration
- Object-based storage only (for files.)
- **Not suitable to install an operating system on.**
- Successful uploads will generate a HTTP 200 status code.
##### S3 Security - Summary
- By default, all newly created buckets are PRIVATE.
- You can set up access control to your buckets using:
  - Bucket Policies - Applied at a bucket level
  - Access Control Lists - Applied at an object level.
- S3 buckets can be configured to create access logs, which log all requests made to the S3 bucket. These logs can be written to another bucket.
##### S3 Encryption - Summary
- Encryption In-Transit
  - SSL/TLS
- Encryption At Rest
  - Server Side Encryption
    - SSE-S3
    - SSE-KMS
    - SSE-C
  - Client Side Encryption
- Remember that we can use a Bucket Policy to prevent unencrypted files from being uploaded by using creating a policy which only allows requests
wich include **x-amz-server-side-encryption** parameter in the request header.

##### S3 CORS - Summary
- Cross Origin Resource Sharing (CORS)
  - Used to enable cross origin access for your AWS resources
  - e.g. S3 hosted website accessing javascript or image files located in another S3 bucket
  - By default resources in one bucket cannot access resources located in another
  - To allow this we need to configure CORS on the bucket being accesses and enable access for the origin (bucket) attempting to access
  - Always use the s3 website URL, not the regular bucket URL:
  - **http://acloudguru.s3-website-eu-west-1.amazonaws.com**
  - https://s3-eu-west-1.amazonaws.com/acloudguru

##### S3 CloudFront - Summary
- **Edge Location** - This is the location where content will be cached. This is separate to an AWS Region/AZ
- **Origin** - This is the origin of all the files that the CDN will distribute. Origins can be an S3 Bucket, an EC2 Instance, an Elastic Load Balancer, or Router53.
- **Distribution** - This is the name given the CDN, which consits of a collection of Edge Locations.
  - **Web Distribution** - Typically used for Websites.
  - **RTMP** - Used for Media Streaming.
- Edge locations are not just READ only - you can WRITE to them too. (i.e. put an object on to them.)
- Objects are cached for the life of the TTL (Time To Live.)
- You can clear cached objects, but you will be charged. (invalidation)

##### S3 Performance Optimization - Summary
- remember the 2 main approaches to Performance Optimization for S3
  - GET-Intensive Workloads - Use CloudFront
  - Mixed-Workloads - Avoid sequential key names for your S3 objects.
Instead, add a random prefix like a hex hash to the key name to
prevent multiple objects from being stored on the same partition


####  CHAPTER 5 Introduction to Serverless Computing
Serverless Summary
#### CHAPTER 6 DynamoDB
DynamoDB Summary
#### CHAPTER 7 KMS and Encryption on AWS
KMS Exam Tips
#### CHAPTER 8 Other AWS Services
Other AWS Services Summary
#### CHAPTER 9 Developer Theory
Developer Theory Summary
#### CHAPTER 10 Advanced IAM
Advanced IAM Summary
#### CHAPTER 11 Monitoring

#### CHAPTER 12 Summary
Summary and next steps
