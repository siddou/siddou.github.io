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

# S3
- Write access best practice: use IAM role with permissions
- Put Object is used to Put a single item.
- The multipart upload API enables you to upload large objects in parts.
- support at least 3500 requests per second
- There are two ways to configure server-side encryption for Amazon S3 artifacts:
  - CodePipeline creates an Amazon S3 artifact bucket and default AWS-managed SSE-KMS encryption keys when you create a pipeline using the Create Pipeline wizard. The master key is encrypted along with object data and managed by AWS.
  - You can create and manage your own customer-managed SSE-KMS keys.

# S3 CloudFront
-  fast content delivery network (CDN)
-  Edge Location - This is the location where content will be cached. This is separate to an AWS Region/AZ

# CodeBuild
Overrride build with buildspecOverride properties set to the new buildspec.yml file

# RDS (Amazon Relational Database Service)
- Set up, operate, and scale a relational database in the cloud
- Support Transparent Data Encryption (TDE)

# Elasticache
Managed, Redis or Memcached-compatible in-memory data store.

2 different caching strategies:
- Lazy loading (only caches the data when it is requested)
- Write Through (writes data into the cache whenever there is a change to the database)

# SQS (Amazon Simple Queue Service)
- Short Polling - returned immediately even if no messages are in the queue
- Long Polling - polls the queue periodically and only returns a response when a message is in the queue or go the timeout is reached

# STS (AWS Security Token Service)
- web service that enables you to request temporary, limited-privilege credentials for AWS Identity and Access Management (IAM) users or for users that you authenticate (federated users).
- To assume a role, an application calls the AWS STS **AssumeRole** API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. This session has the same permissions as the identity-based policies for that role.

# SNS (Amazon Simple Notification Service)
- highly available, durable, secure, fully managed pub/sub messaging service that enables you to decouple microservices, distributed systems, and serverless applications.

# IAM Roles
- A role specifies a set of permissions that you can use to access AWS resources. In that sense, it is similar to an IAM user. A principal (person or application) assumes a role to receive temporary permissions to carry out required tasks and interact with AWS resources. The role can be in your own account or any other AWS account
- The permissions of your IAM user and any roles that you assume are not cumulative. Only one set of permissions is active at a time. When you assume a role, you temporarily give up your previous user or role permissions and work with the permissions that are assigned to the role. When you exit the role, your original permissions are automatically restored.

# Cognito
- Lets you add user sign-up, sign-in, and access control to your web and mobile apps quickly and easily.
- Scales to millions of users and supports sign-in with social identity providers, such as Facebook, Google, and Amazon, and enterprise identity providers via SAML 2.0.

# Lambda
- Avoid recursion
- environment variables ensure that the code references the correct endpoints when running in each stage

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

# Cloud​Formation
- provides a common language for you to describe and provision all the infrastructure resources in your cloud environment
- package then deploy
- templates?

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

# Step Functions
- Great way to visualize your serverless application.
- Step Functions automatically triggers and tracks each step.
- Step Functions logs the state of each step so if something goes wrong you can track what went wring and where.
- With IAM roles for Amazon ECS tasks, you can specify an IAM role that can be used by the containers in a task

# IAM consists of the following:
- Users
- Groups (A way to group our users and apply polices to the collectively)
- Roles
- Policy Documents

# KMS (AWS Key Management)
- Managed service that makes it easy for you to create and control the encryption keys used to encrypt your data.
- Integrated with other AWS services including, EBS, S3, Amazon Redshift, Amazon Elastic Transcoder, Amazon WoekMail, Amazon Relational Database Service (Amazon RDS), and others to make it simple to encrypt your data with encryption keys that you manage.

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