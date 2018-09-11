---
title:  "Ftp/sftp Vacuum"
tags:
  - ftp
  - sftp
  - lftp
---

# FTP:
```shell
lftp -c 'open FTPSERVER_ADRESS;user USERNAME PASSWORD;mirror / /LOCAFOLDER; quit'
```
ex:
```shell
lftp -c 'open 88.88.88.88;user paludia secret123;mirror / /home/paludia; quit'
```
# SFTP:
```shell
lftp -c 'open sftp://FTPSERVER_ADRESS;user USERNAME PASSWORD;set sftp:auto-confirm yes;mirror / /LOCAFOLDER; quit'
```
ex:
```shell
lftp -c 'open sftp://ftp01.didou.com;user paludia secret123;set sftp:auto-confirm yes;mirror / /home/paludia; quit'
```