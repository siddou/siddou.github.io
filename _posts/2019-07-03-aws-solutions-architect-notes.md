---
classes: wide
title:  "aws certified Solutions Architect notes"
tags:
  - aws
  - certification
---
{% include toc %}

## Comparison of Security Groups and Network ACLs

| Security group                                                                                                                                               | Network ACL                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Operates at the instance level                                                                                                                               | Operates at the subnet level                                                                                                                                                           |
| Supports allow rules only                                                                                                                                    | Supports allow rules and deny rules                                                                                                                                                    |
| Is stateful: Return traffic is automatically allowed, regardless of any rules                                                                                | Is stateless: Return traffic must be explicitly allowed by rules                                                                                                                       |
| We evaluate all rules before deciding whether to allow traffic                                                                                               | We process rules in number order when deciding whether to allow traffic                                                                                                                |
| Applies to an instance only if someone specifies the security group when launching the instance, or associates the security group with the instance later on | Automatically applies to all instances in the subnets that it's associated with (therefore, it provides an additional layer of defense if the security group rules are too permissive) |

## AWS Auto Scaling Group Scale out, Scale up

| Scaling up                                 | Scaling out        |
| ------------------------------------------ | ------------------ |
| change the instance types to a higher type | add more instances |

## AWS Regions and Availability Zones

**AWS Regions**
- Separate geographic areas that AWS uses to house its infrastructure.
- These are distributed around the world so that customers can choose a region closest to them in order to host their cloud infrastructure there.
- The closer your region is to you, the better, so that you can reduce network latency as much as possible for your end-users. You want to be near the data centers for fast service.
- ex. us-east-2, eu-west-3

**Availability zone**
- An AWS Availability Zone (AZ) is the logical building block that makes up an AWS Region

![]({{ "/assets/images/aws/architect/AZ.png" | absolute_url }}){:class="img-responsive"}

**Local Zone**
- Local Zones provide you the ability to place resources, such as compute and storage, in multiple locations closer to your end users

## EC2 usage is calculated by either the hour or the second, depending on which AMI you're running.

### Per-second billing is available for instances launched in:
- On-Demand, Reserved and Spot forms
- All regions and Availability Zones
- Amazon Linux and Ubuntu

### Windows AMI
- billed for a minimum of one hour each time a new instance is started

