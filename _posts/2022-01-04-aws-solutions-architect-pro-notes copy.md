---
classes: wide
title:  "AWS Certified Solutions Architect – Professional – notes 2"
tags:
  - aws
  - certification
---
{% include toc %}

### AWS Systems Manager (SSM)

#### AWS Systems Manager Patch Manager

- ensure that the EC2 instance reboots do not occur at the same time:
  - uses two Patch Groups
  - Associate the predefined AWS-DefaultPatchBaseline baseline on both patch groups
  - non-overlapping maintenance windows
- ensure non-prod and prod aren't patched at the same time:
  - Tag each instance based on its **environment** and **OS**.
  - Create a patch baseline for each environment.
  - Categorize EC2 instances based on their tags using Patch Groups and apply the patches specified in the corresponding patch baseline to each Patch Group.

### CloudWatch

- efficient way to collect and analyze logs from instances:
  - Set up and configure a unified **CloudWatch Logs agent** in each On-Demand EC2 instance
  - which will automatically collect and push data to CloudWatch Logs.
  - Analyze the log data with CloudWatch Logs Insights.
  - More efficient than SSM agent for instance monitoring

### CloudTrail

- logging solution that will track all of the activities of all AWS resources
  - will only cover the activities of the **regional services** (EC2, S3, RDS etc.)
  - For **global services** such as IAM, CloudFront, AWS WAF, and Route 53, enable:
    - –is-multi-region-trail
    - –include-global-service-events

### AWS Schema Conversion Tool (SCT)

- You can use an **AWS SCT agent** to extract data from your on-premises data warehouse to S3 or AWS Snowball Edge device and migrate it to Amazon Redshift. "aws-schema-conversion-tool-extractor-x".

### AWS Database Migration Service (AWS DMS)

- Configure a **local & DMS Task** using the **the AWS DMS agent** to replicate the ongoing updates to the data warehouse. "aws-schema-conversion-tool-dms-agent-X".
- The local subtask – This task migrates data from the source database to the Snowball Edge appliance.
- The AWS DMS subtask – This task moves the data from the appliance into an Amazon S3 bucket and migrates it to the target database.

### CloudFront

- Create a CloudFront distribution with **Geo-Restriction** enabled to block blacklisted countries.
- Use HTTPS and **field-level encryption** to enforce secure end-to-end connections to origin servers
- Use **Cache-Control max-age** & **max-age** to increase increase cache hit ratio.
- improve the performance of the application login:
  - Use Lambda@Edge to allow your Lambda functions to customize content that CloudFront delivers and to execute the authentication process in AWS locations closer to the users.
  - Set up an origin failover and make CloudFront automatically switches to when the primary origin returns specific HTTP status code failure responses

### VPC

#### VPC-dns-support

- Allow internal DNS resolution between peered VPS
  - private hosted zone
  - Set **enableDnsHostNames** & **enableDnsSupport** to "true".

#### Elastic IP address

- public IPv4 address

### IAM

#### IAM Role

- Roles are applied to users who are generally not a part of your AWS account
- Use roles to delegate access to users, applications, and services that do not have access to your AWS resources

#### IAM Policy

- Policies are applied to users and groups that belong to a particular AWS account

### Elastic Beanstalk

- You can’t deploy an application to your on-premises servers using Elastic Beanstalk

### CloudFormation

- To prevent ressources from being deleted:
  - DeletionPolicy snapshot for RDS.( With the retain option, CloudFormation will keep the RDS instance running.)
  - DeletionPolicy retain for S3

###  AWS Serverless Application Model (SAM)

- The **AWS Serverless Application Repository** is a managed repository for serverless applications.

### HTTP Error

- 2xx success
- 3xx redirection
- 4xx client errors
  - 403 Forbidden
  - 404 Not Found
- 5xx server errors
  - 504: The server was acting as a gateway or proxy and did not receive a timely response from the upstream server.


### AWS CloudHSM

- CloudHSM can perform the SSL transactions for LBs (ensure that the key cannot be accidentally or intentionally moved outside the corporate environment)

### AWS Certificate Manager

- In each new AWS Region, request for SSL/TLS certificates using the AWS Certificate Manager for each FQDN. Associate the new certificates to the corresponding Application Load Balancer of the same AWS Region.


