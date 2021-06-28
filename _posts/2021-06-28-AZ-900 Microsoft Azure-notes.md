---
classes: wide
title:  "AZ-900 Microsoft Azure notes"
tags:
  - azur
  - certification
---
{% include toc %}

### Application Insights

- an extensible Application Performance Management (APM) service for developers and DevOps professionals. Use it to monitor your live applications.
- Use it to monitor your live applications

### Azure Virtual Machines

- machines are billed by the second
- Any disks that are attached to the VM will actually not be deleted if its VM is deleted.
- Azure storage still charge any attached data disks even if your virtual machines are already stopped.

### Access control IAM

#### Azure role-based access control (Azure RBAC) 

- The Reader role lets you view everything, but not make any changes
- The Owner role lets you manage everything, including access to resources and the contributor’s role. It grants you full access to manage all resources, including the ability to assign roles in Azure RBAC.
- Virtual Machine Contributor role lets you manage virtual machines, but not access to them, and not the **virtual network or storage account** they’re connected to.
- The Contributor role grants you full access to manage all resources but does not allow you to assign roles in Azure RBAC.

