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
- key-value store
- Auto Scaling not enabled by default.

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
- When **failing over**, Amazon RDS simply flips the canonical name record (CNAME) for your DB instance to point at the standby, which is in turn promoted to become the new primary.
- increase the disk space **without downtime** - enable storage autoscaling.

#### Aurora

- **Amazon Aurora Global Database** - is designed for globally distributed applications, allowing a single Amazon Aurora database to span multiple AWS regions. It replicates your data with no impact on database performance, enables fast local reads with low latency in each region, and provides disaster recovery from region-wide outages.
- use **custom endpoint** to map each connection to the appropriate instance or group of instances based on your use case.
- **Amazon Aurora Serverless cluster** - on-demand, auto-scaling configuration for Amazon Aurora. Meet the needs of the application’s peak load and scales back down when the surge of activity is over.

##### Aurora Endpoint Type

- Cluster Endpoint – The Cluster Endpoint connect your application to the current primary DB instance for that DB cluster. ...
- Reader Endpoint – The Reader Endpoint load-balances connections across the pool of available Read Replicas. ...
- Instance Endpoints – An Instance Endpoint connects to a specific instance in the cluster.
- Custom endpoint – A custom endpoint for an Aurora cluster represents a set of DB instances that you choose

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
  - Designed to optimize costs by automatically moving data to the most cost-effective access tier, without performance impact or operational overhead
- **S3 Glacier**
  - Secure, durable, and low-cost storage class for **data archiving**. Retrieval times configurable from minutes to hours.
- **S3 Glacier Deep Archive**
  - Amazon S3's lowest-cost storage class where a retrieval time of 12 hours is acceptable.

- **protect the S3 objects**
  - Enable Multi-Factor Authentication Delete
  - Enable Versioning
- you can only add 1 SQS or SNS at a time for Amazon S3 events notification
- Can notify to SQS, SNS & Lambda...


- Configure cross-account permissions in S3 by creating an IAM customer-managed policy that allows an IAM user or role to copy objects from the source bucket in one account to the destination bucket in the other account. Then attach the policy to the IAM user or role that you want to use to copy objects between accounts.

#### S3 Glacier

- ensure that retrieval capacity is available
  - Expedited Retrieval
  - Purchase provisioned retrieval capacity

#### S3 Transfer Acceleration

- enables fast, easy, and secure transfers of files over long distances between your client and your Amazon S3 bucket

#### Routing traffic to a website that is hosted in an Amazon S3 Bucket

- The S3 bucket name must be the same as the domain name
- Need a registered domain name

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
- When you launch an Amazon Redshift cluster, you can choose to encrypt it with a master key from the AWS Key Management Service (AWS KMS)
- To enable cross-Region snapshot copy for an **AWS KMS–encrypted cluster**, you must configure a snapshot copy grant for a master key in the destination AWS Region

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

#### EKS (Amazon Elastic Kubernetes Service)

- **EKS** - provisions and scales the **Kubernetes** control plane, including the API servers and backend persistence layer, across multiple AWS availability zones for high availability and fault tolerance

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
- retention period from 1 minute to 14 days
- cannot set a priority to individual items in the SQS queue

### MQ (Amazon MQ)

- It supports industry-standard APIs and protocols so you can switch from any standards-based message broker to Amazon MQ without rewriting the messaging code in your applications.
- Authentication from applications to the ActiveMQ broker itself is provided using username and password-based authentication.
Amazon MQ supports LDAP authentication and authorization with directory services like Microsoft Active Directory.

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
- EBS volumes support live configuration changes while in production which means that you can modify the volume type, volume size, and IOPS capacity without service interruptions.
An EBS volume is off-instance storage that can persist independently from the life of an instance

![]({{ "/assets/images/aws/architect/Disks.png" | absolute_url }}){:class="img-responsive"}

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

#### Amazon Data Lifecycle Manager (DLM)

- automate the creation, retention, and deletion of snapshots taken to back up your Amazon EBS volumes

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

#### lifecycle instance states

- **pending** – The instance is preparing to enter the running state. An instance enters the pending state when it launches for the first time, or when it is restarted after being in the stopped state.
- **running** – The instance is running and ready for use.
- **stopping** – The instance is preparing to be stopped. Take note that **you will not billed** if it is preparing to stop however, **you will still be billed if it is just preparing to hibernate**.
- **stopped** – The instance is shut down and cannot be used. The instance can be restarted at any time.
- **shutting-down** – The instance is preparing to be terminated.
- **terminated** – The instance has been permanently deleted and cannot be restarted. Take note that Reserved Instances that applied to terminated instances are **still billed until the end of their term according to their payment option**.

#### Auto Scaling

- Scaling options
  - Maintain current instance levels at all times
  - Scale manually
  - Scale based on a schedule
  - Scale based on demand
  - Use predictive scaling
- **target tracking scaling** - select a scaling metric and set a target value
- Cooldown period
  - default value is 300 seconds
  - It ensures that the Auto Scaling group does not launch or terminate additional EC2 instances before the previous scaling activity takes effect.
- default termination policy - First EC2 instance be terminated: The instance launched from the oldest launch configuration
- Instance scale-in protection - To control whether an Auto Scaling group can terminate a particular instance when scaling in.

##### AWS Auto Scaling Group Scale out, Scale up

| Scaling up                                 | Scaling out        |
| ------------------------------------------ | ------------------ |
| change the instance types to a higher type | add more instances |

#### ENI VS ENA VS EFA

- **ENI** - Elastic Network Interface - For basic networking, ex separate management network, separate loggin network.
- **ENA** - Elastic Network Adapter - For speed between 10Gbps and 100Gbps, reliable, high throughput.
- **EFA** - Elastic Fabric Adapter - For High Performance Computing (HPC) and machine learning.

### KMS (AWS Key Management)

- Managed service that makes it easy for you to create and control the encryption keys used to encrypt your data.
- Integrated with other AWS services including, EBS, S3, Amazon Redshift, Amazon Elastic Transcoder, Amazon WorkMail, Amazon Relational Database Service (Amazon RDS), and others to make it simple to encrypt your data with encryption keys that you manage.
- If you are exceeding the requests per second limit, consider using the data key caching feature of the AWS Encryption SDK. Reusing data keys, rather than requesting a new data key for every encryption operation, might reduce the frequency of your requests to AWS KMS.
- When you create an **AWS KMS customer master key (CMK)** in a custom key store, AWS KMS generates and stores non-extractable key material for the CMK in an **AWS CloudHSM cluster** that you own and manage.

### AWS Systems Manager Parameter Store

- provides secure, hierarchical storage for configuration data management and secrets management. You can store data such as passwords, database strings, Amazon Machine Image (AMI) IDs, and license codes as parameter values. You can store values as plain text or encrypted data.
- doesn’t rotate its parameters by default

### AWS Secrets Manager

- Similar to Systems Manager Parameter Store
- Automatic rotate secrets
- Charge per secret stored and per 10,000 API calls
- generate random secrets

### AWS Resource Access Manager (RAM)

- to easily and securely share your resources with your AWS accounts.

### AWS Organizations

- Consolidate all of the company’s accounts using AWS Organizations.

### AWS Control Tower

- offers the easiest way to set up and govern a new, secure, multi-account AWS environment.

### AWS Config

- enables you to assess, audit, and evaluate the configurations of your AWS resources
- By creating an AWS Config rule, you can enforce your ideal configuration in your AWS account.

### ELB

- cannot increase the instances based on demand.


### Elasticache

- In-memory cache sits between your application and database
- 2 different caching strategies: Lazy loading and Write Through
- Lazy Loading only caches the data when it is requested
- Elasticache Node failures not fatal, just lots of cache misses
- Cache miss penalty: Initial request, query database, writing to cache
- Avoid stale data by implementing a TTL
- Write Through strategy writes data into the cache whenever there is a change to the database
- Data is never stale
- Write penalty: Each write involves a write to the cache
- Elasticache node failure means that data is missing until added or updated in the database
- Wasted resources if most of the data is never used
- ElastiCache for **Redis** - Redis AUTH command can improve data security by requiring the user to enter a password before they are granted permission to execute Redis commands on a password-protected Redis server

### Storage Gateway

- Enables hybrid storage between on-premises storage environments and the AWS Cloud.
The Storage Gateway virtual appliance connects directly to your local infrastructure as a file server, as a volume, or as a virtual tape library (VTL)
- Tape Gateway enables you to replace using physical tapes on-premises with virtual tapes in AWS without changing existing backup workflows.
- it is not suitable for transferring large sets of data to AWS

- **File Gateway** (nfs) - For flat files, stored directly on S3
- **Volume Gateway** (isci)
  - **Stored Volumes** - Entire Dataset is stored **on site** and is asynchronously backed up to S3.
  - **Cached Volumes** - Entire Dataset is stored **on S3** and the most frequently accessed data is cached on site
- **Gateway Virtual Tape Library** - Used for backup and uses popular backup applications like Netbackup, Backup Exec, Veeam etc.

### AWS DataSync

- move large amounts of data from on-premises to Amazon S3, EFS, or Amazon FSx for Windows File Server.
- used with NFS & SMB
- Install DataSync agent
- Can be used to replicate EFS to EFS

### VPC

- IVP4 CIDR range must be provided first in order to configure an IPV6 CIDR range.
- You can enable access to your network from your VPC by attaching a virtual private gateway to the VPC, creating a custom route table, updating your security group rules, and creating an AWS managed VPN connection.
- Each subnet maps to a single Availability Zone.
- Every subnet that you create is automatically associated with the main route table for the VPC.

#### Network ACL

- To enable the connection to a service running on an instance, the associated network ACL must allow both inbound traffic on the port that the service is listening on as well as allow outbound traffic from **ephemeral ports**.

#### Security groups for your VPC

- You might set up network ACLs with rules similar to your security groups in order to add an additional layer of security to your VPC.

| Security group                                                                                                                                               | Network ACL                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Operates at the instance level                                                                                                                               | Operates at the subnet level                                                                                                                                                           |
| Supports allow rules only                                                                                                                                    | Supports allow rules and deny rules                                                                                                                                                    |
| Is stateful: Return traffic is automatically allowed, regardless of any rules                                                                                | Is stateless: Return traffic must be explicitly allowed by rules                                                                                                                       |
| We evaluate all rules before deciding whether to allow traffic                                                                                               | We process rules in order, starting with the lowest numbered rule, when deciding whether to allow traffic                                                                              |
| Applies to an instance only if someone specifies the security group when launching the instance, or associates the security group with the instance later on | Automatically applies to all instances in the subnets that it's associated with (therefore, it provides an additional layer of defense if the security group rules are too permissive) |

#### EC2 access from the Internet

- EIP or public IP address
- route table properly configured

### AWS OpsWorks

- Configuration management service that provides managed instances of Chef and Puppet

### AWS Glue

- Fully managed extract, transform, and load (ETL) service that makes it easy for customers to prepare and load their data for analytics.

### Amazon EMR

- big data platform for processing vast amounts of data using open source tools such as Apache Spark, Apache Hive, Apache HBase, Apache Flink, Apache Hudi, and Presto.
- analyzing log files

### Route 53

- **Latency Routing** serve user requests from the AWS Region that provides the lowest latency. It does not, however, guarantee that users in the same geographic region will be served from the same location.
- **Geoproximity Routing** route traffic to your resources based on the geographic location of your users and your resources.
- **Geolocation Routing** choose the resources that serve your traffic based on the geographic location of your users, meaning the location that DNS queries originate from. Cannot control the coverage size from which traffic is routed to your instance in Geolocation Routing
- **Weighted Routing** lets you associate multiple resources with a single domain name  or subdomain name and choose how much traffic is routed to each resource.


### Amazon Kinesis Data Streams

- If the DynamoDB table used by Kinesis does not have enough capacity to store the lease data, increase the write capacity assigned to the shard table.

### Aws Global Accelerator

- Service in which you create accelerators to improve availability and performance of you applications for local and global users.
- You are assigned two static IP addresses (or you can bring your own)
- You can control traffic using traffic dials. This is done within the endpoint group.

### AWS Firewall Manager

- simplifies AWS WAF and AWS Shield Advanced administration and maintenance tasks across multiple accounts and resources


### ALB NLB CLassic LB

- ALB - support sni
- NLB - Can get Elastic IP address assigned

### AWS Direct Connect

- dedicated network connection from your premises to AWS

### AWS Transit Gateway 

- provide a hub and spoke design for connecting VPCs and on-premises networks
- By attaching a transit gateway to a Direct Connect gateway using a transit virtual interface, you can manage a single connection for multiple VPCs or VPNs that are in the same AWS Region. You can also advertise prefixes from on-premises to AWS and from AWS to on-premises.

### Cloudformation

- Use **CreationPolicy** attribute with a resource to prevent its status from reaching create complete until AWS CloudFormation receives a specified number of success signals or the timeout period is exceeded. To signal a resource, you can use the **cfn-signal** helper script or SignalResource API.

## AWS AppSync
## AWS Private Link
- can provision interface VPC endpoints (interface endpoints) in your virtual private cloud (VPC) instead of connecting over the internet
- endpoint type
  - Gateway endpoints for Amazon S3
  - Interface endpoints for Amazon S3 (You pay an hourly rate for every provisioned Interface endpoint)
## Kinesis  data stream versus Firehose
## Kinesis data stream

By default, the data records are only accessible for 24 hours from the time they are added to a Kinesis stream.

## Kinesis SHarding

### CloudFront

- OAI - Origin Access Identity - prevents users from viewing your S3 files by simply using the direct URL for the file. Instead, they would need to access it through a CloudFront URL.
- CloudFront signed URLs or signed cookies - allow you to control who can access your content
- S3 Pre-signed URLs - use the owner’s security credentials to grant others time-limited permission to download or upload objects.

### AWS Backup

- centralized backup service for Aurora, DynamoDB, RDS, FSx,EFS,EBS, Storage Gateway, EC2

