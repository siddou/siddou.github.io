---
classes: wide
title:  "aws certified Solutions Architect notes 2"
tags:
  - aws
  - certification
---
{% include toc %}

## Design Resilient Architectures

- **Amazon FSx for Windows** -  provides fully managed, highly reliable, and scalable file storage that is accessible over the industry-standard Service Message Block (SMB) protocol. It is built on Windows Server, delivering a wide range of administrative features such as user quotas, end-user file restore, and Microsoft Active Directory (AD) integration. Amazon FSx is accessible from Windows, Linux, and MacOS compute instances and devices. Thousands of compute instances and devices can access a file system concurrently.


### RDS

- **RDS** Amazon Relational Database Service
  - Amazon Aurora
  - PostgreSQL
  - MySQL
  - MariaDB
  - Oracle Database
  - SQL Server

#### Aurora

- **Amazon Aurora Global Database** - is designed for globally distributed applications, allowing a single Amazon Aurora database to span multiple AWS regions. It replicates your data with no impact on database performance, enables fast local reads with low latency in each region, and provides disaster recovery from region-wide outages.

- use **custom endpoint** to map each connection to the appropriate instance or group of instances based on your use case.

### S3

- **protect the S3 objects**
  - Enable Multi-Factor Authentication Delete
  - Enable Versioning

## Design High-Performing Architectures

### CloudWatch

- **Default Metrics**
  - CPU Utilization
  - Network Utilization
  - Disk Reads
- **custom metrics**
  - Memory utilization
  - Disk swap utilization
  - Disk space utilization
  - Page file utilization
  - Log collection

## Design Secure Applications and Architectures

### CloudTrail

- **AWS CloudTrail** is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account. With CloudTrail, you can log, continuously monitor, and retain account activity related to actions across your AWS infrastructure. By default, CloudTrail is enabled on your AWS account when you create it. When activity occurs in your AWS account, that activity is recorded in a CloudTrail event. You can easily view recent events in the CloudTrail console by going to Event history.

## Design Cost-Optimized Architectures

### Fargate

- **AWS Fargate** - Serverless compute for containers
- Set ECS task with **CloudWatch Event rule**.

### ECS

- **ECS** Amazon Elastic Container Service - fully managed container orchestration service