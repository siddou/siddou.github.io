---
title:  "Install ISCSI storage on Centos 7"
tags:
  - scsi-target-utils
  - tutorial
  - centos
  - centos 7
  - linux
---
<!-- {% include toc %} -->
[iscsi-initiator-client-setup](http://www.tecmint.com/iscsi-initiator-client-setup/){:target="_blank"}

```shell
yum -y install nano
systemctl stop firewalld
systemctl disable firewalld
```

```shell
nano /etc/sysconfig/selinux
```
```shell
SELINUX=disabled
```
```shell
shutdown -r now
```

```shell
yum install -y epel-release
yum install -y scsi-target-utils
```



```shell
fdisk /dev/sda
#create lvm partition (8e)
...
```


```shell
vgcreate vg_iscsi /dev/sda1
lvcreate -l +100%FREE -n lv_iscsi vg_iscsi
```



```shell
nano /etc/tgt/targets.conf
```
```shell
<target iqn.2014-07.com.storage:tgt1>
       backing-store /dev/vg_iscsi/lv_iscsi
</target>
```

```shell
systemctl enable tgtd
systemctl restart tgtd
systemctl status tgtd -l
tgtadm --mode target --op show
```

{% include disqus.html %}