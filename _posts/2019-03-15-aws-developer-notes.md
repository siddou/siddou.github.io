---
classes: wide
title:  "aws certified Developper notes"
tags:
  - aws
  - certification
---
{% include toc %}

#EC2
- Storage
  - EBS provides persistent block storage volumes.
  - EBS encryption uses AWS KMS customer master keys
  - Instance Stores will be wiped if the instance is stopped
- bootstrap script via **Userdata**

# S3 (AMazon Simple Storage Service)
- Write access best practice: use IAM role with permissions
- Encryption: use bucket policy
- Put Object is used to Put a single item.
- The multipart upload API enables you to upload large objects in parts.
- support at least 3500 requests per second
- There are two ways to configure server-side encryption for Amazon S3 artifacts:
  - CodePipeline creates an Amazon S3 artifact bucket and default AWS-managed SSE-KMS encryption keys when you create a pipeline using the Create Pipeline wizard. The master key is encrypted along with object data and managed by AWS.
  - You can create and manage your own customer-managed SSE-KMS keys.

# S3 CORS (Cross Online Resource Sharing)

# S3 CloudFront
-  fast content delivery network (CDN)
-  Edge Location - This is the location where content will be cached. This is separate to an AWS Region/AZ

# CodeBuild
Overrride build with buildspecOverride properties set to the new buildspec.yml file

# RDS (Amazon Relational Database Service)
- Set up, operate, and scale a relational database in the cloud
- Support Transparent Data Encryption (TDE)

# Elasticache
- Choose **Memcached** if You need the simplest model possible.
- Choose **Redis** for complex models.
- 2 different caching strategies:
  - Lazy loading (only caches the data when it is requested)
  - Write Through (writes data into the cache whenever there is a change to the database)

# SQS (Amazon Simple Queue Service)
- fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications
- Short Polling - returned immediately even if no messages are in the queue
- Long Polling - polls the queue periodically and only returns a response when a message is in the queue or go the timeout is reached
- Standard Queues (default): best effort ordering, message delivered at least once
- FIFO Queues (First In First Out): ordering strictly preserved, message delivered once, no duplicates (e.g. good for banking transactions which need to happen in strict order

# STS (AWS Security Token Service)
- web service that enables you to request temporary, limited-privilege credentials for AWS Identity and Access Management (IAM) users or for users that you authenticate (federated users).
- To assume a role, an application calls the AWS STS **AssumeRole** API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. This session has the same permissions as the identity-based policies for that role.

# SNS (Amazon Simple Notification Service)
- highly available, durable, secure, fully managed pub/sub messaging service that enables you to decouple microservices, distributed systems, and serverless applications.

# Lambda
- Avoid recursion
- environment variables ensure that the code references the correct endpoints when running in each stage
- a function can be created to install external libraries

# API Gateway
- create and deploy your own REST and WebSocket APIs at any scale
- can manage multiple release stages for each API
- crontrol API behavior by configuring Method request, Method response

# Systems Manager Parameter Store
- Provides secure, hierarchical storage for configuration data management and secrets management.
- Store data such as passwords, database strings, and license codes as parameter values.
- Store values as plain text or encrypted data.
- You can then reference values by using the unique name that you specified when you created the parameter.

# Kinesis
- collect, process, and analyze video and data streams in real time
- three core services:
  - Kinesis Streams:
    - Video Streams - securely stream video from connected devices to AWS for analytics and machine learning
    - Data Steams - Build custom applications process data in real-time
- Kinesis Firehose - capture, transform, load data streams into AWS data stores for near real-time analytics with BI tools
- You can configure Lambda to subscribe to a Kinesis Stream and execute a function on your behalf when a new record is detected, before sending the processed data on to its final destination
- Preprocessing Data with AWS Lambda function

# CloudWatch
- monitoring and management service
- can load all the metrics in your account (both AWS resource metrics and application metrics that you provide) for search, graphing, and alarms

# Elastic Beanstalk
- service for deploying and scaling web applications and services developed with Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker on familiar servers such as Apache, Nginx, Passenger, and IIS.
- Choose instance type  when creating a new configuration file in S3 and use the same during environment creation
- blue and green - two separate, but identical environment, use separated instances.

[![]({{ "/assets/images/aws/developer/deployment-methods.png" | absolute_url }}){:class="img-responsive"}]({{ "/assets/images/aws/developer/deployment-methods.png" | absolute_url }})


# DynamoDB
- Auto scaling - when you have unpredictable workloads
- Cross-region replication - for disaster recovery scenarios
- Steams - stream data to other sources
- Accelerator (DAX) - in-memory cache that delivers up to a 10x performance improvement, predictable load.
- TTL can be enabled for items that can be deleted in a particular timeframe.
- Encryption can only be configured during table creation time
- Not a good choice for storing BLOBs, directly, but it could be a good choice for indexing BLOBs that are stored on S3

- Provisioned Throughput is measured in Capacity Units
- 1 x Write Capacity Unit = 1 x 1KB Write per second.
- 1 x x Read Capacity Unit = 1x 4KB Strongly Consistent Read OR 2 x 4KB Eventually Consistent Reads per second.
- Calculate Write Capacity Requirements (100 x 512 byte items per second):
  - First, calculate how many Capacity Units for each write: Size of each item / 1KB (for Write Capacity Units) 512 bytes / 1KB = 0.5
  - Rounded-up to the nearest whole number, each write will need 1 x Write Capacity Unit per write operation
  - Multiplied by the number of writes per second = 1 x 100 = 100 Write Capacity Units required
- Calculate Read Capacity Requirements (80 x 3KB items per second):
  - First, calculate how many Capacity Units for each read: Size of each item / 4KB (for Read Capacity Units) 3KB / 4KB = 0.75
  - Rounded-up to the nearest whole number, each read will need 1 x Read Capacity Unit operation
  - Multiplied by the number of reads per second = 1 x 80 = 80 Read Capacity Units required for Strongly Consistent, but if Eventual Consistency is acceptable, divide by 2 = 40 read Capacity Units required

300 items every 30 seconds. Each items is of size 6KB, calculate read capacity: 
```
300 items = 30 sec
10 items = 1 sec : 10 items per second
1 read = 4KB
1 Item = 6KB = 2 read
10 items * 2 reads = 20 reads / 2 (consistent read) = 10 reads
```

# DynamoDB Scan vs Query
- Scan (it's more efficient to use query!) - sequential (default), parallel
- A parallel scan can be the right choice if the following conditions are met:
  - The table size is 20 GB or larger.
  - The table's provisioned read throughput is not being fully utilized.
  - Sequential Scan operations are too slow.
- Reduce the impact of a query or scan by setting a smaller **page size** which uses fewer read operations.
- DynamoDB Streams use cases:
  - An application in one AWS region modifies the data in a DynamoDB table. A second application in another AWS region reads these data modifications and writes the data to another table, creating a replica that stays in sync with the original table.
  - A popular mobile app modifies data in a DynamoDB table, at the rate of thousands of updates per second. Another application captures and stores data about these updates, providing near real time usage metrics for the mobile app.
  - A global multi-player game has a multi-master topology, storing data in multiple AWS regions. Each master stays in sync by consuming and replaying the changes that occur in the remote regions.
  - An application automatically sends notifications to the mobile devices of all friends in a group as soon as one friend uploads a new picture.
  - A new customer adds data to a DynamoDB table. This event invokes another application that sends a welcome email to the new customer.

# Cloud​Formation
- provides a common language for you to describe and provision all the infrastructure resources in your cloud environment
- package then deploy
- templates?
- Automate Lambda functions deployment

# CodeDeploy
- deployment service that automates software deployments to a variety of compute services such as Amazon EC2, AWS Fargate, AWS Lambda, and your on-premises servers

# X-Ray
- The X-Ray Integrates with the following AWS services:
  - Elastic Load Balancing
  - AWS Lambda
  - Amazon API Gateway
  - Amazon Elastic Compute Cloud

# CodePipeline
-  continuous delivery service that helps you automate your release pipelines for fast and reliable application and infrastructure updates

# Ecs (Amazon Elastic Container Service)
- Highly scalable, high-performance container orchestration service that supports Docker containers and allows you to easily run and scale containerized applications

# Elb (Elastic Load Balancing)
- automatically distributes incoming application traffic across multiple targets, such as Amazon EC2 instances, containers, IP addresses, and Lambda functions
- access logs can be enabled

# Step Functions
- Great way to visualize your serverless application.
- Step Functions automatically triggers and tracks each step.
- Step Functions logs the state of each step so if something goes wrong you can track what went wring and where.
- With IAM roles for Amazon ECS tasks, you can specify an IAM role that can be used by the containers in a task

# IAM
- IAM consists of the following:
  - Users
  - Groups (A way to group our users and apply polices to the collectively)
  - Roles
  - Policy Documents
- **Federation** allows users to authenticate with a web Identity Provider (Google, Facebook, Amazon)
- The user authentication first with the Web ID Provider and receives an authentication token, which is exchanged for temporary AWS credentials allowing them to assume an IAM role.

# IAM Roles
- A role specifies a set of permissions that you can use to access AWS resources. In that sense, it is similar to an IAM user. A principal (person or application) assumes a role to receive temporary permissions to carry out required tasks and interact with AWS resources. The role can be in your own account or any other AWS account
- The permissions of your IAM user and any roles that you assume are not cumulative. Only one set of permissions is active at a time. When you assume a role, you temporarily give up your previous user or role permissions and work with the permissions that are assigned to the role. When you exit the role, your original permissions are automatically restored.

# IAM Policies
- Managed Policy (recommanded policy) - AWS-managed default Policies
- Customer Managed Policy - Managed by you
- Inline Policy - Managed by you and embedded in a single user, group, or role.

# Cognito
- Lets you add user sign-up, sign-in, and access control to your web and mobile apps quickly and easily.
- Scales to millions of users and supports sign-in with social identity providers, such as Facebook, Google, and Amazon, and enterprise identity providers via SAML 2.0.

# KMS (AWS Key Management)
- Managed service that makes it easy for you to create and control the encryption keys used to encrypt your data.
- Integrated with other AWS services including, EBS, S3, Amazon Redshift, Amazon Elastic Transcoder, Amazon WoekMail, Amazon Relational Database Service (Amazon RDS), and others to make it simple to encrypt your data with encryption keys that you manage.
- If you are exceeding the requests per second limit, consider using the data key caching feature of the AWS Encryption SDK. Reusing data keys, rather than requesting a new data key for every encryption operation, might reduce the frequency of your requests to AWS KMS.

# CodeStar
- cloud-based service for creating, managing, and working with software development projects on AWS

# Route 53
- Routing Policy
  - Simple routing policy – Use for a single resource that performs a given function for your domain, for example, a web server that serves content for the example.com website.
  - Failover routing policy – Use when you want to configure active-passive failover.
  - Geolocation routing policy – Use when you want to route traffic based on the location of your users.
  - Geoproximity routing policy – Use when you want to route traffic based on the location of your resources and, optionally, shift traffic from resources in one location to resources in another.
  - Latency routing policy – Use when you have resources in multiple AWS Regions and you want to route traffic to the region that provides the best latency.
  - Multivalue answer routing policy – Use when you want Route 53 to respond to DNS queries with up to eight healthy records selected at random.
  - Weighted routing policy – Use to route traffic to multiple resources in proportions that you specify.

# Cloud​Formation
- a service that helps you model and set up your Amazon Web Services resources so that you can spend less time managing those resources and more time focusing on your applications that run in AWS
- You create a template that describes all the AWS resources that you want (like Amazon EC2 instances or Amazon RDS DB instances), and AWS CloudFormation takes care of provisioning and configuring those resources for you
- can automate lambda deployment

# CodeDeploy
- deployment service that automates application deployments to Amazon EC2 instances, on-premises instances, serverless Lambda functions, or Amazon ECS services.
- **AppSpec file** - CodeDeploy Application Specification Files
- You can deploy a nearly unlimited variety of application content, including:
  - code
  - serverless AWS Lambda functions
  - web and configuration files
  - executables
  - packages
  - scripts
  - multimedia files

# RedShift
- fast, scalable data warehouse that makes it simple and cost-effective to analyze all your data across your data warehouse and data lake
- Normally used for columnar based databases

# OpsWorks
- configuration management service that provides managed instances of Chef and Puppet