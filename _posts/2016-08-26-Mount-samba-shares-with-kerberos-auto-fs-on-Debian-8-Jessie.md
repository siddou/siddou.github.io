---
title:  "Mount samba shares with kerberos+auto fs on Debian 8 Jessie"
tags:
  - debian
  - jessie
  - debian 8
  - linux
---

### Install autofs and cifs
```shell
apt-get install autofs cifs-utils
```

### Configure auto fs
```shell
nano /etc/auto.master
```
```shell
+dir:/etc/auto.master.d
/mnt/files                /etc/auto.files           --ghost,--timeout=30
+auto.master
```
```shell
nano /etc/auto.files
```
```shell
#samba shares
share1    -fstype=cifs,sec=krb5,uid=${UID},cruid=${UID}                         ://samba_server/share1
share2    -fstype=cifs,sec=krb5,uid=${UID},cruid=${UID}                         ://samba_server/share2
#homes
*                   -fstype=cifs,sec=krb5,uid=&,cruid=&                           ://samba_server/&
```
```shell
systemctl restart autofs
```
### Test
Your kerberos ticket should be valid (check with "klist", or else do "kinit loginname").
Browse to /mnt/files with the files explorer, you shoud see share1 and share2.
Browse to /mnt/files/loginname, you shoud see your private samba folder.

{% include comments.html %}