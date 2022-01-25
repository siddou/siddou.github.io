---
classes: wide
title:  "AWS Certified Solutions Architect – Professional – notes"
tags:
  - aws
  - certification
---
{% include toc %}

## AWS Accounts and Organizations

### AWS Organizations

- Main account -> Management Account (always at the root)
- join existing account
- group account into OUs
- Service Control Policies (SCPs) -> Control tagging and the available API actions
- Create accounts programmatically using API
- Enable AWS SSO using on-prem directory
- Consolidated bill
- Enable Cloutrail in management account and apply to members

### Service Control Policies (SCPs)

- SCPs control the maximum available permissions
- IAM give you the privileges to perform an action
- SCP controls whether you're allowed to in that particular account
- It is best practice not to create Users in the management account
- Tag policy are about standardizing, forcing standardization of tags that you apply to your resources
- **Explicit deny will always take precedence**

### SCP Strategies and Inheritance

- Default strategy -> Deny List Strategy
- Deny List Strategy
  - **FullAWSAccess** SCP is attached to every OU and account
  - Explicitly allows all permissions to flow down from the root
  - Can explicitly override with a deny in an SCP
- Allow List Strategy
  - **FullAWSAccess** SCP is **removed** from every OU and account
  - To allow a permission, SCPs with allow statment must be added to the account and every OU above it including root
  - Every SCP in the hierarchy must explicitly allow the APIs you want to use

## Identity Management and Permissions

### How IAM Works

- IAM Principals must be **authenticated** to send requests (with a few exeptions)
- A principal is a person or application that can make a request for an **action** or **operation** on an AWS resource (User, Role, Federated User, Application)
- Request context
  - actions / operations
  - Resources
  - Principal
  - Environment data
  - Resource data
- AWS determines whether to authorize the request (allow/deny)
- We can control this through IAM policies:
  - Identity-based policy (apply to user and roles)
  - Resource-based policy (applies to AWS resources)

### Overview of Users, Groups, Roles and Policies

- group: container for users.
- The user gains the permissions applied to the group through a identity-based policy.
- Identity-based policy can be applied to users, groups, and roles
- Policies define the permissions for the identities or resources they are associated with
- Roles are used for delegation and are assumed
- User can authenticate via username/password for console or access keys for API/CLI.
- IAM role is an IAM identity that has specific permissions
- Roles are assumed by users, applications, and services
- Once assumed, the identity "becomes" the role and gain the roles' permissions.

### IAM Authentication Methods

- user account: Use Username and Password & MFA Token (optional)
- CLI & API: Use Access key ID & Secret access key. Associated with a user account.
- Signing Certificate. X.509 certificate authentication method. Used to access some services like Amazon EC2 SOAP and CLI interfaces.
- SSH and HTTPS Git Credentials. AUth to AWS COdeCommit.
- Keyspace Credentials

### AWS Security Token Service (STS)

- Ex access S3 from an application running on EC2.
- Create an Instance Profile, attach an IAM Role to it. The EC2 attempts to assume role (sts:AssumeRole API call).
- Trust policies control who can assume the role.
- AWS STS return temporary security credentials.
- Credentials include:
  - AccessKeyId
  - Expiration
  - Secret AccessKey
  - SessionToken
- Temporary credentials are used with identity federation, delegation, cross-account access, and IAM roles.

### Multi-Factor Authentication (MFA)
3.7
