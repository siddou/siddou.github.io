---
classes: wide
title:  "aws certified Solutions Architect"
last_modified_at: 2019-07-04
tags:
  - aws
  - certification
---
{% include toc %}

## [Exam guide](https://d1.awsstatic.com/training-and-certification/docs-sa-pro/AWS%20Certified%20Solutions%20Architect-Professional_Exam%20Guide.pdf){:target="_blank"}

### Domain 1: Design for Organizational Complexity

#### 1.1. Determine cross-account authentication and access strategy for complex organizations (for example, an organization with varying compliance requirements, multiple business units, and varying scalability requirements).

#### 1.2. Determine how to design networks for complex organizations (for example, an organization with varying compliance requirements, multiple business units, and varying scalability requirements).

#### 1.3. Determine how to design a multi-account AWS environment for complex organizations (for example, an organization with varying compliance requirements, multiple business units, and varying scalability requirements).

### Domain 2: Design for New Solutions

#### 2.1. Determine security requirements and controls when designing and implementing a solution.

#### 2.2. Determine a solution design and implementation strategy to meet reliability requirements.

#### 2.3. Determine a solution design to ensure business continuity.

#### 2.4. Determine a solution design to meet performance objectives.

#### 2.5. Determine a deployment strategy to meet business requirements when designing and implementing a solution.

### Domain 3: Migration Planning

#### 3.1. Select existing workloads and processes for potential migration to the cloud.

#### 3.2. Select migration tools and/or services for new and migrated solutions based on detailed AWS knowledge.

#### 3.3. Determine a new cloud architecture for an existing solution.

#### 3.4. Determine a strategy for migrating existing on-premises workloads to the cloud.

### Domain 4: Cost Control

#### 4.1. Select a cost-effective pricing model for a solution.

#### 4.2. Determine which controls to design and implement that will ensure cost optimization.

#### 4.3. Identify opportunities to reduce cost in an existing solution.

### Domain 5: Continuous Improvement for Existing Solutions

#### 5.1. Troubleshoot solution architectures.

#### 5.2. Determine a strategy to improve an existing solution for operational excellence.

#### 5.3. Determine a strategy to improve the reliability of an existing solution.

#### 5.4. Determine a strategy to improve the performance of an existing solution.

#### 5.5. Determine a strategy to improve the security of an existing solution.

#### 5.6. Determine how to improve the deployment of an existing solution.

### [Solutions Architect notes]({{ site.baseurl }}{% post_url 2019-07-03-aws-solutions-architect-notes %})

### acloud.guru training

#### CHAPTER 1 Introduction

| Domain | % of Examination |
| Domain 1: Design for Organizational Complexity | 12.5% |
| Domain 2:  Design for New Solutions | 31% |
| Domain 3: Migration Planning  | 15% |
| Domain 4:  Cost Control  | 12.5% |
| Domain 5: Continuous Improvement for Existing Solutions | 29% |
| Total | 100% |

- 130 Minutes in Length
- 65 questions
- Results immediately
- Passmark is 720 (72%). Top Score 1000.
- $150 USD

[AWS Cheat Sheets](https://tutorialsdojo.com/aws-cheat-sheets/){:target="_blank"}

[Tips](https://www.facebook.com/pg/LearnWithTutorialsDojo/photos/?tab=album&album_id=2102010900053076)
[Tips](https://www.udemy.com/aws-certified-solutions-architect-associate-amazon-practice-exams/learn/quiz/4394970#questions/5867212)
[Tips](https://acloud.guru/forums/aws-certified-solutions-architect-associate/discussion/-KKr5HCv2bzH3EOBSUAt/my_path_to_solutions_architect)

#### Region, availability zones
?

#### CHAPTER 3 Identity Access Management & S3

##### IAM 101

- **IAM is universal.** It does not apply to regions at this times
- The **"root account"** is simply the account created when first setup your AWS account. It has complete Admin access.
- New Users have **NO permissions** when first created.
- New Users are assigned **Access Key ID & Scecret Access Keys** when first created.
- **These are not the same as a password.** You cannot use the access key ID & Secret Access Key to Login in to the console. You can use this to access AWS via the APIs and Command Line, however.
- **You only get to view these once.** If you lose them, you have to regenerate them. So, save them in a secure location.
- Always setup Multifactor Authentication on your root account.
- You can create and customize your own password rotation policies.

Identity Access Management Consist Of The Following:

- **Users**
- **Groups**
- **Roles**
- **Policies**

##### S3 101

- Remember that S3 is **Object-based**: i.e. allows you to upload files.
- FIles can be from 0 Bytes **to 5 TB**
- There is unlimited storage
- Files are stored in Buckets
- **S3 is a universal namespace**. That is, names must be unique globally.
- http://s3-eu-west-1.amazonaws.com/acloudguru
- **Not suitable to install an operating system on.**
- Successful uploads will generate a **HTTP 200** status code.
- By default, all newly created buckets are **PRIVATE**. You can setup access control to your bucket using:
  - **Bucket Policies**
  - **Access Control Lists**
- S3 buckets can be configured to create access logs which log all requests made to S3 bucket. This can be sent to another bucket and even another bucket in another account.
- You can turn on **MFA Delete**
**The Key Fundamentals of S3 Are:**
- Key (This is simply the name of the object)
- Value (This is simply the data)
- Version ID (Important for versioning)
- Metadata (Data about data you are storing
- Subresources:
  - Access Control Lists
  - Torrent
- Read after Write consistency for PUTS of new Objects
- Eventual Consistency for overwrite PUTS and DELETES (can take some time to propagate)

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

- Encryption In Transit is achieved by
  - **SSL/TLS**
- Encryption At Rest (Server Side) is achieved by
  - **S3 Managed Keys - SSE-S3**
  - **AWS Key Management Service, Managed Keys - SSE-KMS**
  - **Server Side Encryption With Customer Provided Keys - SSE-C**
- Client Side Encryption

##### S3 Version Control

- Stores all versions of an object (including all writes and even if you delete an object)
- Great backup tool
- Once enabled, Versioning cannot be disabled, only suspended.
- Intergrates with lifecycle rules
- Versioning's MFA Delete Capability, which uses multi-factor authentication, can be used to provide an additional layer of security

##### S3 Lifecycle Management and Glacier

- Automates moving your objects between the different storage tiers.
- Can be used in conjunction with versioning.
- Can be applied to current versions and previous versions.

##### Cross Region Replication

- versioning must be enabled on both the source and destination buckets.
- Regions must be unique.
- Files in an existing bucket are not replicated automatically
- All subsequent updated files will be replicated automatically
- Delete markers are not replicated
- Deleting individual versions or delete markers will not be replicated

##### S3 Transfer Acceleration

 Transfer Acceleration takes advantage of Amazon CloudFront’s globally distributed edge locations. As the data arrives at an edge location, data is routed to Amazon S3 over an optimized network path.

##### CloudFront Overview

- **Edge Location** - This is the location where content will be cached. This is separate to an AWS Region/AZ.
- **Origin** - This is the origin of all the files that the CDN will distribute. This can be either an S3 Bucket, an EC2 Instance, an Elastic Load Balancer, or Route53.
- **Distribution** - This is the name given the CDN which consists of a collection of Edge Locations.
- **Web Distribution** - Typically used for Websites.
- **RTMP** - Used for Media Streaming
- Edge locations are not just READ only - you can write to them too. (ie put object on to them.)
- Objects are cached for the life of the **TTL (Time To Live.)**
- You can clear cached objects, but you will be charged.

##### Snowball Overview

- Snowball is a big encrypted disk  (50TB or 80TB)
- Snwoball edge is a mini portable AWS (100TB)
- Snowmobile is a transfer data service using a truck (100PB)
- Import to S3
- Export from S3

##### Storage Gateway

Enables hybrid storage between on-premises storage environments and the AWS Cloud.
The Storage Gateway virtual appliance connects directly to your local infrastructure as a file server, as a volume, or as a virtual tape library (VTL)

- **File Gateway** (nfs) - For flat files, stored directly on S3
- **Volume Gateway** (isci)
  - **Stored Volumes** - Entire Dataset is stored on site and is asynchronously backed up to S3.
  - **Cached Volumes** - Entire Dataset is stored on S3 and the most frequently accessed data is cached on site
- **Gateway Virtual Tape Library** - Used for backup and uses popular backup applications like Netbackup, Backup Exec, Veeam etc.

#### CHAPTER 4 EC2

##### EC2 101

- Amazon Elastic Compute CLoud (Amazon EC2) is a web service that provides resizable compute capacity in the cloud. Amazon EC2 reduces the time required to obtain and boot new server instances to minutes, allowing you to quickly scale capacity, both up and down, as your computing requirements change.
- **On Demand**
  - Allows you to pay a fixed rate by the hour (or by the second) with no commitment.
- **Reserved**
  - Provide you with a capacity reservation, and offer a significant discount on the hourly charge for an instance. Contract Terms are 1 Year or 3 Year Terms.
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

##### Security Groups Basics

- All Inbound traffic is blocked by default.
- All Outbound traffic is allowed.
- Changes to Security Groups take effect immediately.
- You can have any number of EC2 instances within a security group.
- You can have multiple secuirty groups attached to EC2 Instances.
- Security Groups are **STATEFUL**
- If you create an inbound rule allowing traffic in, that traffic is automatically allowed back out again.
- You cannot block specific IP addresses using Security Groups, instead use Network Access Control Lists.
- You can specify allow rules, but not deny rules.

##### EBS Volumes 
Amazon Elastic Block Store
- Persistant block storage
- Termination Protection is **turned off** by default, you must turn it on.
- On an EBS-backed instance, the **default action is for the root EBS volume to be deleted** when the instance is terminated.
- EBS Root Volumes of your DEFAULT AMI's cannot be encrypted. You can also use a third tool (such as bit locker etc) to encrypt the root volume, or this can be done when creating AMI's (lab to follow) in the AWS console or using the API.
- Additional volumes can be encrypted
- Automatically replicated within its AZ
- 5 EBS Types:
  - General Purpose (SSD) -> Most Workloads
  - Provisioned IOPS (SSD) -> Databases
  - Throughput Optimised Hard Disk Drive -> Big Data & Data Warehouses
  - Cold Hard Disk Drive -> File Servers
  - Magnetic -> infrequently accessed

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

##### AMI Types (EBS vs Instance Store)

- Instance Store Volumes are sometimes called Ephemeral Storage
- Instance store volumes cannot be stopped. If the underlying host fails, you will lose your data.
- EBS backed instances can be stopped. You will not lose the data on this instance if it is stopped.
- You can reboot both, you will not lose your data.
- By default, both ROOT volumes will be deleted on termination. However, with EBS volumes, you can tell AWS to keep the root device volume.

##### Encrypted Root Device Volumes & Snapshots

- Snapshots of encrypted Volumes are encrypted automatically
- Volumes restored from encrypted Snapshots are encrypted automatically
- You can share Snapshots, but only if they are unencrypted.
- These snapshots can be shared with other AWS accounts or made public.
- Create a Snapshot of the unencrypted root device volume
- Create a copy of the Snapshot and select the encrypt option
- Create an AMI from the encrypted Snapshot
- Use that AMI to launch new encrypted instances

##### CloudWatch 101

- CloudWatch is used for monitoring performance
- CloudWatch can monitor most of AWS as well as your applications that run on AWS.
- CloudWatch with EC2 will monitor events every 5 minutes by default.
- You can have 1 minute intervals by turning on detailed monitoring.
- You can create CloudWatch alarms which trigger notifications.
- CloudWatch monitors performance.
- CloudTrail monitors is about auditing (API calls).

- What can I do With CloudWatch?
  - Dashboards - Creates awesome dashboards to see what is happening with your AWS environment.
  - Alarms - Allows you to set Alarms that notify you when particular thresholds are hit.
  - Events - CloudWatch Events helps you to respond to state changes in your AWS resources.
  - Logs - CloudWatch Logs helps you to aggregate, monitor, and store logs.

##### The AWS Command Line

- You can interact with AWS from anywhere in the world just by using the command line (CLI).
- You will need to set up access in IAM
- Commands themselves are not in the exam, but some basic commands will be useful to know for real life.

##### Using IAM Roles With EC2

- Roles are more secure than storing your access key and secret access key on individual EC2 instances.
- Roles are easier to manage.
- Roles can be assigned to an EC2 instance after it is created using both the console & command line.
- Roles are universal - you can use them in any region.

##### EC2 Instance Meta Data

- Used to get informations about an instance (such as public ip)
- curl http://169.254.169.254/latest/meta-data/
- curl http://169.254.169.254/latest/user-data/

##### Elastic File System (EFS)

- Supports the Network File System version 4 (NFSv4) protocol
- You only pay for the storage you use (no pre-provisioning required.)
- Can scale up to the petabytes
- Can support thousands of the concurrent NFS connections
- Data is stored across multiple AZ's within a region
- Read After Write Consistency

##### EC2 Placement Groups

- **Cluster Placement Group**
  - Low Network Latency / High Network Throughput
  - Can't span multiple Availability Zones.
  - Only certain types of instances can be launched in a placement group (Compute Optimized, GPU, Memory Optimized, Storage Optimized)
- **Partition Placement Group**
  - Multiple EC2 instances HDFS,HBase, and Cassandra
  - spreads your instances across logical partitions such that groups of instances in one partition do not share the underlying hardware with groups of instances in different partitions. This strategy is typically used by large distributed and replicated workloads, such as Hadoop, Cassandra, and Kafka.
- **Spread Placement Group**
  - Individual Critical EC2 instances
  - Can span multiple Availability Zones.
- The name you specify for a placement group must be unique within your AWS account.
- AWS recommend homogenous instances within placement groups.
- You can't merge placement groups.
- You can't move an existing instance into a placement group. You can create an AMI from your existing instance, and then launch a new instance from the AMI into a placement group.


#### CHAPTER 5 Databases On AWS

##### Databases 101