---
classes: wide
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

### [Developer notes]({{ site.baseurl }}{% post_url 2019-03-15-aws-developer-notes %})

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
- Passmark is 720 (72%). Top Score 1000.
- $150 USD

12/02/2019
Hi - yes it is up to date for the latest exam. The exam was released in June 2018 and has not been refreshed since then,

[Tips](https://www.whizlabs.com/blog/aws-certified-developer-associate-practice-tests-updated/)

[Tips](https://medium.com/devopslinks/passing-the-aws-certified-developer-associate-exam-c83c894cb780)

[Tips](https://acloud.guru/forums/aws-cda-2018/discussion/-LVjFQsZd5s5_HLdVQrx/passed_developer_associate)

[Tips](https://acloud.guru/forums/aws-cda-2018/discussion/-LUk6O3fg_B3MvFP0feD/aws_certified_developer_-_asso)

[Tips](https://acloud.guru/forums/aws-cda-2018/discussion/-L_dBng3i_Y5NFJ7zPsY/cleared_out_aws_developer_asso)

[Tips](https://acloud.guru/forums/aws-certified-developer-associate/discussion/-KUdI5f2LNbi4wvK7v4I/how_to_pass_aws_certified_deve)

[Tips](https://acloud.guru/forums/aws-cda-2018/discussion/-LWDVxz601aEDRXyZS_P/passed_the_cda_exam_on_friday)

[Tips](https://acloud.guru/forums/aws-cda-2018/discussion/-LZRDTlcsGXtCh6EYIwY/passed:_cda_feb_2019)

[Tips](https://www.2ndwatch.com/blog/how-to-upgrade-your-chances-of-passing-any-aws-certification-exam/#respond)

[Tips](https://www.selikoff.net/2019/03/02/does-a-cloud-guru-acg-prepare-you-for-the-aws-associate-developer-exam/)
[Tips](https://www.selikoff.net/wp-content/uploads/2019/03/AWS-Associate-Developer-Study-Guide.pdf)
[Tips](https://www.selikoff.net/2019/03/02/how-i-studied-for-the-aws-associate-developer-cert/)
[Tips](https://www.selikoff.net/2019/03/02/how-i-recommend-studying-for-the-aws-associate-developer-exam/)

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

[Read the FAQ!](https://aws.amazon.com/s3/faqs/){:target="_blank"}

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
  - mybucket/**7eh4**-2018-03-04-15-00-00/cust1234234/photo1.jpg
  - mybucket/**h35d**-2018-03-04-15-00-00/cust1234234/photo2.jpg
  - mybucket/**o3n6**-2018-03-04-15-00-00/cust1234234/photo3.jpg


####  CHAPTER 5 Introduction to Serverless Computing
##### Lambda - Exam Tips
- Lambda scales out (not up) automatically
- Lambda functions are independent, 1 event = 1 function
- Lambda is serverless
- Know what services are serverless!
- Lambda functions can trigger other lambda functions, 1 event can = x
functions if functions trigger other functions

- Architectures can get extremely complicated, AWS X-ray allows you to debug what is happening
- Lambda can do things globally, you can use it to back up S3 buckets to other S3 buckets etc
- Know your triggers

##### Exam Tips
- Remember what API Gateway is at a high level
- API Gateway has caching capabilities to increase performance
- API Gateway is low cost and scales automatically
- You can throttle API Gateway to prevent attacks
- You can log results to CloudWatch
- If you are using Javascript/AJAX that uses multiple domains with API Gateway, ensure that you have enabled CORS on API Gateway
- CORS is enforced by the client

##### Version Control With Lambda Exam Tips
- Can have multiple versions of lambda functions
- Latest version will use $latest
- Qualified version will use $latest, unqualified will not have it
- Versions are immutable (Cannot be changed).
- Can split traffic using aliases to different versions
  - Cannot split traffic with $latest, instead create an alias to latest.

##### Step Functions
- Great way to visualize your serverless application.
- Step Functions automatically triggers and tracks each step.
- Step Functions logs the state of each step so if something goes wrong you can track what went wring and where.

##### X-Ray Exam Tips
The X-Ray SDK provides:
- Interceptors to add to your code to trace incoming HTTP requests
- Client handlers to instrument AWS SDK clients that your application uses to call other AWS services
- An HTTP client to use to instrument calls to other internal and external HTTP web services
The X-Ray Integrates with the following AWS services:
- Elastic Load Balancing
- AWS Lambda
- Amazon API Gateway
- Amazon Elastic Compute Cloud
- AWS Elastic Beanstalk
The X-Ray Integrates with the following languages:
- Java
- Go
- Node.js
- Python
- Ruby
- .Net

#### CHAPTER 6 DynamoDB
##### DynamoDB Exam Tips
- Amazon DynamoDB is a low-latency NoSQL database.
- Consists of Tables, Items, and Attributes
- Supports both document and key-value data models
- Supported document formats are JSON, HTML, XML
- 2 types of Primary Keys: Partition Key and combination of Partition Key + Sort Key (Composite Key)
- 2 Consistency models: Strongly Consistent/Eventually Consistent.
- Access is controlled using IAM policies.
- Fine grained access control using IAM Condition parameter:
**dynamodb:LeadingKeys** to allow users to access only the items where the partition key value matches their user ID
##### DynamoDB Indexes - Exam Tips
- Indexes enable fast queries on specific data columns.
- Give you a different view of your data based on alternative Partition / Sort Keys
- Important to understand the differences
  | Local Secondary Index | Global Secondary Index |
  | Must be created at when you create your table | Can create any time - at table creation of after |
  | Same Partition Key as your table | Different Partition Key |
  | Different Sort Key | Different Sort Key |
##### Scan Vs Query Exam Tips
- A Query operation finds items in a table using only the Primary Key attribute.
- You provide the Primary Key name and a disctinct value to search for.
- A scan operation examines every item in the table.
  - By default, returns all data attributes
- Use the ProjectionExpression parameter to refine the results.
- Query results are always sorted by the Sort Key (if there is one.)
- Sorted in ascending order
- Set ScanIndexForward parameter to false to reverse the order - queries only
- Query operation is generally more efficient than a Scan.
- Reduce the impact of a query or scan by setting a smaller page size which uses fewer read operations.
- Isolate scan operations to specific tables and segregate them from your mission-critical traffic.
- Try Parallel scans rather than the default sequential scan.
- Avoid using scan operations if you can: design tables in a way that you can use the Query, Get, or BatchGetItem APIs.
##### DynamoDB Provisioned Throughput Exam Tips
- Provisioned Throughput is measured in Capacity Units
- 1 x Write Capacity Unit = 1 x 1KB Write per second.
- 1 x x Read Capacity Unit = 1x 4KB Strongly Consistent Read OR 2 x 4KB Eventually Consistent Reads per second.
###### Calculate Write Capacity Requirements (100 x 512 byte items per second):
- First, calculate how many Capacity Units for each write:
  Size of each item / 1KB (for Write Capacity Units)
  512 bytes / 1KB = 0.5
- Rounded-up to the nearest whole number, each write will need 1 x Write Capacity Unit per write operation
- Multiplied by the number of writes per second = 1 x 100 = 100 Write Capacity Units required
###### Calculate Read Capacity Requirements (80 x 3KB items per second):
- First, calculate how many Capacity Units for each read:
  Size of each item / 4KB (for Read Capacity Units)
  3KB / 4KB = 0.75
- Rounded-up to the nearest whole number, each read will need 1 x Read Capacity Unit operation
- Multiplied by the number of reads per second = 1 x 80 = 80 Read Capacity Units required for Strongly Consistent, but if Eventual Consistency is acceptable, divide by 2 = 40 read Capacity Units required
##### DAX Exam Tips
- Provides in-memory caching for DynamoDB tables
- Improves response times for Eventually Consistent reads only.
- You point your API calls to the DAX cluster instead of your table.
- If the item you are queryng is on the cache, DAX will return it; otherwise, it will perform an Eventually Consistent GetItem operation to your DynamoDB table.
- Not suitable for write-intensive applications or applications that require Strongly Consistent reads.

##### Elasticache Exam Tips
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


#### CHAPTER 7 KMS and Encryption on AWS
##### AWS Key Management 101
AWS Key Management (AWS KMS) is a managed service that makes it easy for you to create and control the encryption keys used to encrypt your data. AWS KMS is integrated with other AWS services including, EBS, S3, Amazon Redshift, Amazon Elastic Transcoder, Amazon WoekMail, Amazon Relational Database Service (Amazon RDS), and others to make it simple to encrypt your data with encryption keys that you manage.
##### AWS Key Management Service Exam Tips
- CMK
  - alias
  - creation date
  - description
  - key state
  - **key material (either customer provided or AWS provided).
- Can **Never** be exported
###### Setup a Customer Master Key:
- Create Alias and Description
- Choose material option...
- Define Key **Administrative Permissions**
  - IAM users/roles that can administer (but not use) the key htrough the KMS API.
- Define Key **Usage Permissions**
  - IAM users/roles that can use the key to encrypt and decrypt data.
###### Key material options:
- Use KMS generated key material
- Your own key material
##### AWS API Calls Exam Tips
- **aws kms encrypt**
- **aws kms decrypt**
- **aws kms re-encrypt**
- **aws kms enable-key-rotation**
##### AWS Encryption Exam Tips
**The Customer Master key:**
- Customer Master Key used to decrypt the data key (envelope key)
- Envelope Key is used to decrypt the data key (envelope key)



#### CHAPTER 8 Other AWS Services
##### SQS Exam Tips
- SQS is a distributed message queueing system
- SQS allows you to decouple the components of an application so that they are independent
- Pull-based not push-based
- Standard Queues (default): best effort ordering, message delivered at least once
- FIFO Queues (First In First Out): ordering strictly preserved, message delivered once, no duplicates (e.g. good for banking transactions which need to happen in strict order)
- Visibility Timeout
  - Default 30 seconds - increase if your task takes >30 seconds to complete
  - Max 12 hours
- Short Polling - returned immediately even if no messages are in the queue
- Long Polling - polls the queue periodically and only returns a response when a message is in the queue or go the timeout is reached
##### SNS Exam Tips
- SNS is a scalable and highly available notification service which allows you to send push notifications from the cloud
- A variety of a message formats are supported: SMS test message, email, Amazon Simple Queue Services (SQS) queues, any HTTP endpoint.
- Pub-sub model whereby users subscribe to topics
- It is a push mechanism rather tahn a pull mechanism
- Exemple architecture: a company wanting to send notifications to multuple customers could use SNS to fan out multiple messages in SQS format using a dedicated SQS queue per customer
##### SNS Vs SES Exam Tips
- Remember that SES is for email only
- It can be used for incoming and outgoing mail
- It is not subscription based-you only need to know the email address
- SNS caters for various formats (SMS, SQS, HTTP, email)
- Push notifications only
- Pub/ sub model-consumers must subscribe to a topic
- You can fan out messages to large number of recipients, (e.g. multiple clients each with their own SQS queue)
##### Kinesis Exam Tips
- Know the difference between the three core services:
  - Kinesis Streams:
    - Video Streams - securely stream video from connected devices to AWS for analytics and machine learning
    - Data Steams - Build custom applications process data in real-time
  - Kinesis Firehose - capture, transform, load data streams into AWS data stores for near real-time analytics with BI tools

- You can configure Lambda to subscribe to a Kinesis Stream and execute a function on your behalf when a new record is detected, before sending the processed data on to its final destination
##### Elastic Beanstalk Exam Tips
- Deploys and scales your web applications including the web application server platform where required
- Supports widely used programming technologies - Java, PHP, Python, Ruby, Go, Docker, .NET, and Node.js
- As well as application server platforms like Tomcat, Passenger, Puma, and IIS
- Provisions the underlying resources for you
- Can fully manage the EC2 instances for you, or you can take full administrative control
- Updates, monitoring, metrics, and health checks all included
##### Updating Elastic Beanstalk Exam Tips
- Remember the 4 different deployment approaches:
  - All at Once
    - Service interruption while you update the entire environment at once
    - To roll back, perform a futher all at All at Once upgrade
  - Rolling
    - Reduced capacity during deployment
    - To roll back, perform a futher rolling update
  - Rolling with Additional Batch
    - Maintains full capacity
    - To roll back, perform a futher rolling update
  - Immutable
    - Preferred option for mission critical production systems
    - Maintains full capacity
    - To roll back, just delete the new instances and autoscaling group
##### Advanced Elastic Beanstalk Exam Tips
- You can customize your Elastic Beanstalk environment by adding configuration files
- The files are written in YAML or JSON
- Files have a .config extension
- The .config files are saved to the .ebextensions folder
- Your .ebextensions folder must be located in the top level directory of your application source code bundle
##### RDS & Elastic Beanstalk Exam Tips
- Two different options for launching your RDS instance:
  - **Launch within Elastic Beanstalk**
    - When you terminate the Elastic Beanstalk environment, the database will also be terminated
    - Quick and easy to add your database and get started
    - Suitable for Dev and Test environments only
  - **Launch outside of Elastic Beanstalk**
    - Additional configuration steps required - Security Group and Connection information
    - Suitable for Production environments, more flexiblility
    - Allows connection from multiple environments, you can tear down the application stack without impacting the database



#### CHAPTER 9 Developer Theory
##### CI/CD Exam Tips
- Definitely worth a few points in the exam
- Worth reading the white paper:
  - [practicing-continuous-integration-continuous-delivery-on-AWS](https://d0.awsstatic.com/whitepapers/DevOps/practicing-continuous-integration-continuous-delivery-on-AWS.pdf){:target="_blank"}
- Continuous Integration is about integrating or merging the code changes frequently - at least once per day, enables multiple devs to work on the same application
- Continuous Delivery is all about automating the build, test, and deployment functions?
- Continuous Deployment fully automate the entire release process, code is deployed into Production as soon as it has successfully passed through the release pipeline.
- AWS CodeCommit - Source Control service (git)
- AWS CodeBuild - compile source code, run tests and package code
- AWS CodeDeploy - Automated Deployment to EC2, on premises systems and Lambda
- AWS CodePipeline - CI/CD workflow tool, fully automates the entire release process (build, test, deployment)
##### AWS CodeCommit Exam Tips
- AWS CodeCommit
  - Based on git
  - Centralized repository for all your code, binaries, images and libraries
  - Tracks and manages code changes
  - Maintains version history
  - Manages updates from multiple sources and enables collaboration
##### AWS CodeDeploy Exam Tips
- AWS CodeDeploy is a fully managed automated deployment service and can be used as part of a Continuous Delivery or Continuous Deployment process.
- Remember the different types of deployment approach:
  - **In-places or Rolling update** - you stop the application on each host and deploy the latest code. EC2 and on premise systems only. To roll back you must re-deploy the previous version of the application.
  - **Blue / Green** - New instances are provisioned and the new application is deployed to these new instances. Traffic is routed to the new instances according to your own schedule. Supported for EC2, on-premise systems and Lambda functions. Roll back is easy, just route the traffic back to the original instances. Blue is the active deployment, green is the new release.

##### CodeDeploy Advanced Settings - Exam Tips
- The AppSec file defines all the parameters needed for the deployment e.g. location of application files and pre/post deployment validation tests to run
- For EC2 / On Premises systems, the appsec.yml file must be placed in the root directory of your revision (the same folder that contains your application code). Written in YAML
- Lambda supports YAML or JSON
- The **Run Order of hooks** in a CodeDeploy deployment:
  - BeforeBlockTraffic -> BlockTraffic -> AfterBlockTraffic
  - ApplicationStop
  - BeforeInstall
  - installAfterInstall
  - ApplicationStart
  - ValidateService
  - BeforeAllowTraffic -> AllowTraffic -> AfterAllowTraffic
##### AWS CodePipeline Exam Tips
- Continuous Integration / Continuous Delivery service
- Automates your end-to-end software release process based on a user defined workflow
- Can be configured to automatically trigger your pipeline as soon as a change is detected in your source code repository
- Integrates with other services from AWS like CodeBuild and CodeDeploy, as well as thrid party and custom plug-ins.
##### Docker and CodeBuild Exam Tips
- Docker allows you to package up your software into Containers which you can run Elastic Container Service (ECS)
- A Docker Container includes everything the software needs to run including code, libraries, runtime and environment variables etc.
- We use a special file called a Dockerfile to specify the instructions needed to assemble your Docker image.
- Once built, Docker images can be stored in Elastic Container Registery (ECR) and ECS can then use the image to launch Docker containers.
##### Docker Exam Tips
- Docker Commands to build, tag (apply an alias) and push your Docker image to the ECR repository
```shell
docker build -t myimagerepo

docker tag myimagerepo:latest 725350006743.dkr.ecr.eu-central-l.amazonaws.com/myimagerepo:latest
docker push 725350006743.dkr.ecr.eu-central-l.amazonaws.com/myimagerepo:latest
```
##### CodeBuild Exam Tips
- CodeBuild is a fully managed build service. It can build source code, run tests and produce software packages based on commands that you define yourself.
- By default the buildspec.yml defines the build commands and settings used by CodeBuild to run your build
- You can completely overrride the settings in buildspec.yml by adding your own commands in the console when you launch the build.
- If your build fails, check the build logs in the CodeBuild console and you can also view the full CodeBuild log in CloudWatch

##### CodePipeline Exam Tips
- Continuous Integration / Continuous Delivery service
- Automates your end-to-end software release process based on a user defined workflow
- Can be configured to automatically trigger your pipeline as soon as a change is detected in your source code repository
- Integrates with other services from AWS CodeBuild and CodeDeploy, as well as thrid party and custom plug-ins.
- 


#### CHAPTER 10 Advanced IAM
##### Web Identity Federation Exam Tips
- Federation allows users to authenticate with a web Identity Provider (Google, Facebook, Amazon)
- The user authentication first with the Web ID Provider and receives an authentication token, which is exchanged for temporary AWS credentials allowing them to assume an IAM role.

##### Cognito Exam Tips
- Cognito is and Identity Broker which handles interaction between your applications and the Web ID provider (you don't need to write your own code to do this.)
  - Provides sign-up, sign-in and guest user access
  - Syncs user data for a seamless experience across your devices
- Cognito is the AWS-recommended approach for Web ID Federation
- Cognito uses User Pools to manage user sign-up and sign-in directly, or via Web Identity Providers
- Cognito uses Push Synchronization to send a silent push notification of user data updates to multiple device types associated with a user ID.

![]({{ "/assets/images/aws/developer/Cognito_user_pools_exemple.png" | absolute_url }}){:class="img-responsive"}

##### Inline Policies Vs Managed Policies vs. Custom Policies Exam Tips
- Remember the 3 different types of IAM Policies:
  - Managed Policy - AWS-managed default Policies
  - Customer Managed Policy - Managed by you
  - Inline Policy - Managed by you and embedded in a single user, group, or role.
- In most cases, AWS recommends using Managed Policies over Inline Policies

#### CHAPTER 11 Monitoring
##### CloudWatch vs CloudTrail vs config
- CloudWatch monitors performance.
- CloudTrail monitors API calls in the AWS platform.
- AWS Config records the state of your AWS environment and can notify you changes.

#### CHAPTER 12 Summary
Summary and next steps

