---
title:  "Create self signed SSL Certificate on Debian 8 Jessie"
tags:
  - tutorial
  - debian
  - jessie
  - debian 8
  - linux
  - openssl
---
Generating RSA private key
```shell
openssl req -x509 -nodes -sha256 -days 3650 -newkey rsa:2048 -keyout siddou.tk.key -out siddou.tk.crt
```
```shell
Country Name (2 letter code) [AU]:FR
State or Province Name (full name) [Some-State]:IDF
Locality Name (eg, city) []:Paris
Organization Name (eg, company) [Internet Widgits Pty Ltd]:siddou   
Organizational Unit Name (eg, section) []:siddou
Common Name (e.g. server FQDN or YOUR name) []:*.siddou.tk          
Email Address []:admin@siddou.tk

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:
An optional company name []:
```


Example: add in apache
```shell
SSLCertificateFile /etc/ssl/private/siddou.tk.crt
SSLCertificateKeyFile /etc/ssl/private/siddou.tk.key
```


{% include disqus.html %}