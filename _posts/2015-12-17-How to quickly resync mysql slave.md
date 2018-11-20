---
title:  "How to quickly resync mysql slave"
tags:
  - mysql
  - tutorial
  - linux
---
<!-- {% include toc %} -->
On master Dump databases:
```shell
mysqldump --master-data -u user -ppassword dbname | gzip -1 > dbname.sql.gz
```
- Dump on disk to release the locks on the master as quickly as possible.
- Master data option will record master_log_pos

Then Copy sql file on slave

On slave:
```shell
mysql -u user -ppassword -h localhost
mysql> STOP SLAVE;
mysql> exit
```

```shell
pv dbname.sql.gz | gunzip | mysql -u user -ppassword dbname
```

```shell
mysql -u user -ppassword -h localhost
mysql> START SLAVE;
mysql> SHOW SLAVE STATUS\G
```

you should see:
```shell
Slave_IO_Running: Yes
Slave_SQL_Running: Yes
```

{% include disqus.html %}