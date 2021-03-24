---
classes: wide
title:  "aws certified Solutions Architect notes 2"
tags:
  - aws
  - certification
---
{% include toc %}

### Amazon FSx

#### Amazon FSx for Windows File Server

- provides fully managed, highly reliable, and scalable file storage that is accessible over the industry-standard Service Message Block (SMB) protocol. It is built on Windows Server, delivering a wide range of administrative features such as user quotas, end-user file restore, and Microsoft Active Directory (AD) integration. Amazon FSx is accessible from Windows, Linux, and MacOS compute instances and devices. Thousands of compute instances and devices can access a file system concurrently.

#### Amazon FSx for Lustre

- When you need high-speed, high-capacity distributed storage. This will be for applications that do High Performance Compute (HPC), financial modelling etc. Remember that FSx for Lustre can store data directly in S3.

### AWS Directory Service AD Connector

- **AWS Directory Service Simple AD** - this just provides a subset of the features offered by AWS Managed Microsoft AD, including the ability to manage user accounts and group memberships, create and apply group policies, securely connect to Amazon EC2 instances, and provide Kerberos-based single sign-on (SSO).

### DynamoDB

- Accelerator (**DAX**) - in-memory cache that delivers up to a 10x performance improvement, predictable load.
- **DynamoDB Streams** use cases:
  - An application in one AWS region modifies the data in a DynamoDB table. A second application in another AWS region reads these data modifications and writes the data to another table, creating a replica that stays in sync with the original table.
  - A popular mobile app modifies data in a DynamoDB table, at the rate of thousands of updates per second. Another application captures and stores data about these updates, providing near real time usage metrics for the mobile app.
  - A global multi-player game has a multi-master topology, storing data in multiple AWS regions. Each master stays in sync by consuming and replaying the changes that occur in the remote regions.
  - An application automatically sends notifications to the mobile devices of all friends in a group as soon as one friend uploads a new picture.
  - A new customer adds data to a DynamoDB table. This event invokes another application that sends a welcome email to the new customer.
- Use **partition keys** with high-cardinality attributes. The more distinct partition key values your workload accesses, the more those requests will be spread across the partitioned space

### RDS

- **RDS** Amazon Relational Database Service
  - Amazon Aurora
  - PostgreSQL
  - MySQL
  - MariaDB
  - Oracle Database
  - SQL Server
- Multi-AZ deployments
- use IAM DB Authentication
- **IAM database authentication** - authenticate to your DB instance
- RDS event notification can only send data to an Amazon SNS topic, and not directly to a Lambda function
- **Enhanced Monitoring** - provides metrics in real time for the operating system (OS) that your DB instance runs on, stored for 30 days in the CloudWatch Logs.

#### Aurora

- **Amazon Aurora Global Database** - is designed for globally distributed applications, allowing a single Amazon Aurora database to span multiple AWS regions. It replicates your data with no impact on database performance, enables fast local reads with low latency in each region, and provides disaster recovery from region-wide outages.
- use **custom endpoint** to map each connection to the appropriate instance or group of instances based on your use case.
- **Amazon Aurora Serverless cluster** - on-demand, auto-scaling configuration for Amazon Aurora. Meet the needs of the application’s peak load and scales back down when the surge of activity is over.

### S3

- **S3 Standard**
  - 99.99% availability
  - 99.999999999% durability
  - stored redundantly across multiple device in multiple facilities, and is designed to sustain the loss of 2 facilities concurrently.
- **S3 - IA**
  - (Infrequently Accessed):
    - For data that is accessed less frequently, but requires rapid access when needed. Lower fee than S3, but you are charged a retrieval fee
- **S3 One Zone - IA**
  - For where you want a lower-cost option for infrequently accessed data, but do not require the multiple Availability Zone data resilience.
- **S3 - Intelligent Tiering**
  - Designed to optimize costs by automatically moving data to the most cost-effective access tier, whitout performance impact or operational overhead
- **S3 Glacier**
  - Secure, durable, and low-cost storage class for data archiving. Retrieval times configurable from minutes to hours.
- **S3 Glacier Deep Archive**
  - Amazon S3's lowest-cost storage class where a retrieval time of 12 hours is acceptable.

- **protect the S3 objects**
  - Enable Multi-Factor Authentication Delete
  - Enable Versioning
- you can only add 1 SQS or SNS at a time for Amazon S3 events notification

#### Athena

- interactive query service
- allows to query data located in S3 using SQL
- Serverless
- used to analyse log stored in S3

#### Macie

- uses AI to analyse data in S3 and helps identify PII
- Used to analyse CloudTrail logs for suspicion API activity
- Includes Dashboards, Reporting and Alerting
- Great for PCI-DSS compliance and prevent ID theft

### CloudWatch

- **Default Metrics**
  - CPU Utilization
  - Network Utilization
  - Disk Reads/Writes
  - Disk performance
- **custom metrics**
  - Memory utilization
  - Disk swap utilization
  - Disk space utilization
  - Page file utilization
  - Log collection
- multi-platform **CloudWatch agent** which can be installed on both Linux and Windows-based instances.

### CloudTrail

- monitors API calls in the AWS platform.
- **AWS CloudTrail** is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account. With CloudTrail, you can **log**, continuously monitor, and retain account activity related to actions across your AWS infrastructure. By default, CloudTrail is enabled on your AWS account when you create it. When activity occurs in your AWS account, that activity is recorded in a CloudTrail event. You can easily view recent events in the CloudTrail console by going to Event history.

### RedShift

- Analyze all of your data with the fastest and most widely used cloud data warehouse
- **Amazon Redshift Spectrum** - query data directly from files on Amazon S3

### X-Ray

- Interceptors to add to your code to trace incoming HTTP requests
- Client handlers to instrument AWS SDK clients that your application uses to call other AWS services
- An HTTP client to use to instrument calls to other internal and external HTTP web services
- The X-Ray Integrates with the following AWS services:
  - Elastic Load Balancing
  - AWS Lambda
  - Amazon API Gateway
  - Amazon Elastic Compute Cloud
  - AWS Elastic Beanstalk
- The X-Ray Integrates with the following languages:
  - Java
  - Go
  - Node.js
  - Python
  - Ruby
  - .Net

### ECS

- **ECS** Amazon Elastic Container Service - fully managed container orchestration service
- Use the AWS Systems Manager Parameter Store to keep the **database credentials** and then encrypt them using AWS KMS. Create an IAM Role for your Amazon ECS task execution role (taskRoleArn) and reference it with your task definition

#### Fargate

- **AWS Fargate** - Serverless compute for containers
- Set ECS task with **CloudWatch Event rule**.


### Elastic Beanstalk

- use EC2 instances
- service for deploying and scaling web applications and services developed with Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker on familiar servers such as Apache, Nginx, Passenger, and IIS.
- Choose instance type  when creating a new configuration file in S3 and use the same during environment creation
- blue and green - two separate, but identical environment, use separated instances.
- Custom Platforms: create a platform by providing Elastic Beanstalk with a Packer template

[![]({{ "/assets/images/aws/developer/deployment-methods.png" | absolute_url }}){:class="img-responsive"}]({{ "/assets/images/aws/developer/deployment-methods.png" | absolute_url }})

### SNS (Amazon Simple Notification Service)

- highly available, durable, secure, fully managed pub/sub messaging service that enables you to decouple microservices, distributed systems, and serverless applications.

### SQS (Amazon Simple Queue Service)

- distributed message queueing system
- allows you to decouple the components of an application so that they are independent
- Pull-based not push-based
- Standard Queues (default): best effort ordering, message delivered at least once
- FIFO Queues (First In First Out): ordering strictly preserved, message delivered once, no duplicates (e.g. good for banking transactions which need to happen in strict order
- Visibility Timeout
  - Default 30 seconds - increase if your task takes >30 seconds to complete
  - Max 12 hours
- Short Polling - returned immediately even if no messages are in the queue
- Long Polling - polls the queue periodically and only returns a response when a message is in the queue or go the timeout is reached
- messages in the SQS queue will continue to exist until you delete that message
- does not support an extensive list of industry-standard messaging APIs and protocol

### MQ (Amazon MQ)

- It supports industry-standard APIs and protocols so you can switch from any standards-based message broker to Amazon MQ without rewriting the messaging code in your applications.

### SNS vs SQS

| Features            | SNS                        | SQS                   |
| ------------------- | -------------------------- | --------------------- |
| Message persistence | Not persisted              | Persisted             |
| Delivery mechanism  | Push (Passive)             | Poll (Active)         |
| Producer/consumer   | Publish/subscribe (1 to N) | Send/receive (1 to 1) |

### EBS - Amazon Elastic Block Store

#### EBS Volumes

- Persistant block storage
- Termination Protection is **turned off** by default, you must turn it on.
- On an EBS-backed instance, the **default action is for the root EBS volume to be deleted** when the instance is terminated.
- EBS Root Volumes of your DEFAULT AMI's cannot be encrypted. You can also use a third tool (such as bit locker etc) to encrypt the root volume, or this can be done when creating AMI's (lab to follow) in the AWS console or using the API.
- Additional volumes can be encrypted
- Automatically replicated within its AZ
- **5 EBS Types**:
  - General Purpose (SSD) -> Most Workloads
  - Provisioned IOPS (SSD) -> Databases
  - Throughput Optimised Hard Disk Drive -> Big Data & Data Warehouses
  - Cold Hard Disk Drive -> File Servers
  - Magnetic -> infrequently accessed
- Max IOPS > 32,000 use a **Nitro-based** EC2 instance.


##### EBS Snapshots
- Volumes exist on EBS.Think of EBS as a virtual hard disk.
- Snapshots exist on S3. Think of Snapshots as a photograph of the disk.
- Snapshots are point in time copies of Volumes.
- Snapshots are incremental - This means that only the blocks that have changed since your last snapshot are moved to S3.
- To create a snapshot for Amazon EBS volumes that serve as root devices, you should stop the instance before taking the snapshot.
- However you can take a snap while Volumes and Snapshots
- You can change EBS volume sizes on the fly, including changing the size and storage type.
- Volumes will ALWAYS be in the same availability zone as the EC2 instance.
- To move an EC2 volume from one AZ to another, take a snapshot of it, create an AMI from the snapshot and then use the AMI to launch the EC2 instance in a new AZ.
- To move an EC2 volume from one region to another, take a snapshot of it, create an AMI from the snapshot and then copy the AMI from one region to the other. Then use the copied AMI to launch the new EC2 instance in the new region.

### Efs

- Provides a simple, scalable, elastic file system for Linux-based workloads for use with AWS Cloud services and on-premises resources

### EC2

#### Instance Types

- **On Demand**
  - Allows you to pay a fixed rate by the hour (or by the second) with no commitment.
- **Reserved**
  - Provide you with a capacity reservation, and offer a significant discount on the hourly charge for an instance. Contract Terms are 1 Year or 3 Year Terms. Only Convertible Reserved Instances can be exchanged for other Convertible Reserved Instances
- **Spot**
  - Enables you to bid whatever price you want for instance capacity, providing for even greater savings if your applications have flexible start and end times.
  - If Spot instance is terminated by Amazon EC2, you will not be charged for partial hour usage. However, if you terminate the instance yourself, you will be charged for any hour in which the instance ran.
- **Dedicated Hosts**
  - Physical EC2 server dedicated for you use. Dedicated Hosts can help you reduce costs by allowing you to use your existing server-bound software licences.
- EC2 Instance Types - Mnemonic
  - F - For FPGA
  - I - For IOPS
  - G - Graphics
  - H - High DIsk Throughput
  - T - Cheap general purpose (think T2 Micro)
  - D - For Density
  - R - RAM
  - M - Main choice for general purpose apps
  - C - For Compute
  - P - Graphics (think Pics)
  - X - Extreme Memory
  - Z - Extreme Memory AND CPU
  - A - Arm-based workloads
  - U - Bare Metal

#### Auto Scaling

- Scaling options
  - Maintain current instance levels at all times
  - Scale manually
  - Scale based on a schedule
  - Scale based on demand
  - Use predictive scaling
- **target tracking scaling** - select a scaling metric and set a target value
- First EC2 instance be terminated: The instance launched from the oldest launch configuration

##### AWS Auto Scaling Group Scale out, Scale up

| Scaling up                                 | Scaling out        |
| ------------------------------------------ | ------------------ |
| change the instance types to a higher type | add more instances |


### KMS (AWS Key Management)

- Managed service that makes it easy for you to create and control the encryption keys used to encrypt your data.
- Integrated with other AWS services including, EBS, S3, Amazon Redshift, Amazon Elastic Transcoder, Amazon WorkMail, Amazon Relational Database Service (Amazon RDS), and others to make it simple to encrypt your data with encryption keys that you manage.
- If you are exceeding the requests per second limit, consider using the data key caching feature of the AWS Encryption SDK. Reusing data keys, rather than requesting a new data key for every encryption operation, might reduce the frequency of your requests to AWS KMS.
- When you create an **AWS KMS customer master key (CMK)** in a custom key store, AWS KMS generates and stores non-extractable key material for the CMK in an **AWS CloudHSM cluster** that you own and manage.

### AWS Resource Access Manager (RAM)

- to easily and securely share your resources with your AWS accounts.

### AWS Organizations

- Consolidate all of the company’s accounts using AWS Organizations.

### AWS Control Tower

- offers the easiest way to set up and govern a new, secure, multi-account AWS environment.

### ELB

- cannot increase the instances based on demand.


### Elasticache

- In-memory cache sits between your application and database
- 2 different caching strategies: Lazy loading and Write Through
- Lazy Loading only caches the data when it is requested
- Elasticcache Node failures not fatal, just lots of cache misses
- Cache miss penalty: Initial request, query database, writing to cache
- Avoid stale data by implementing a TTL
- Write Through strategy writes data into the cache whenever there is a change to the database
- Data is never stale
- Write penalty: Each write involves a write to the cache
- Elasticache node failure means that data is missing until added or updated in the database
- Wasted resources if most of the data is never used
- ElastiCache for **Redis** - Redis AUTH command can improve data security by requiring the user to enter a password before they are granted permission to execute Redis commands on a password-protected Redis server

### Storage Gateway

Enables hybrid storage between on-premises storage environments and the AWS Cloud.
The Storage Gateway virtual appliance connects directly to your local infrastructure as a file server, as a volume, or as a virtual tape library (VTL)

- **File Gateway** (nfs) - For flat files, stored directly on S3
- **Volume Gateway** (isci)
  - **Stored Volumes** - Entire Dataset is stored on site and is asynchronously backed up to S3.
  - **Cached Volumes** - Entire Dataset is stored on S3 and the most frequently accessed data is cached on site
- **Gateway Virtual Tape Library** - Used for backup and uses popular backup applications like Netbackup, Backup Exec, Veeam etc.


### AWS Systems Manager Parameter Store

- Provides secure, hierarchical storage for configuration data management and secrets management.
