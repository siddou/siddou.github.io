---
title:  "Openfire 4 + AD + Pidgin SSO on Debian 8 Jessie"
tags:
  - openfire
  - tutorial
  - debian
  - jessie
  - debian 8
  - linux
---
{% include toc %}

# Openfire 4 + AD
## Install Openfire 4
Get deb file
```shell
wget https://www.igniterealtime.org/downloadServlet?filename=openfire/openfire_4.0.2_all.deb -O openfire_4.0.2_all.deb
```

Install package and set up mysql
```shell
apt-get install openjdk-7-jre-headless mysql-server
dpkg -i openfire_4.0.2_all.deb

mysql_secure_installation
mysql -u root -p
mysql> create database openfire;
mysql> GRANT ALL PRIVILEGES ON openfire.* TO openfire_user@localhost IDENTIFIED BY 'openfire_pass';
mysql> exit
```



## Enable AD auth:
On AD:
- Create a pidginuser to bind to AD
- Create a pidgin group for allowed user

On openfire, switch to java8.
tar xvf java jre archive in /opt/jre1.8.0_102

```shell
nano /etc/default/openfire
```
```shell
JAVA_HOME=/opt/jre1.8.0_102
systemctl restart openfire
```

Configure Openfire:
 go to http://servername:9090

```shell
select mysql
dbhostname: localhost
dbname: openfire
user: openfire_user
pass: openfire_pass
```

```shell
Server type: Active Directory
Host: ad.siddou.com
Port: 389
Base DN:  dc="siddou",dc="com"
Administrator DN: pidginuser@siddou.com


Username Field: sAMAccountName

User filter:
(objectClass=organizationalPerson)
(&(memberOf=CN=pidgin,CN=Users,DC=siddou,DC=com))

Group Field: cn
Member Field: member
Description Field: description
Group filter: (objectClass=group)(cn=pidgin)
```

- Server settings -> Client Connections
- 5222
- advanced configuration:
- STARTTLS policy -> optional

- Mutual Authentication -> Disabled

Certificate chain checking:
- Uncheck Allow peer certificates to be self-signed.
- check Verify that the certificate is currently valid (based on the 'notBefore' and 'notAfter' values of the certificate).

- disable 5223

# Pidgin SSO
[openfire-enable-single-sign-on-sso-on-linux](https://community.spiceworks.com/how_to/13930-openfire-enable-single-sign-on-sso-on-linux){:target="_blank"}

## Prerequisite
Openfire 4.1.6
Java Version:	1.8.0_102 Oracle Corporation -- Java HotSpot(TM) 64-Bit Server VM
server joined to the domain + Ad enabled in openfire


## Java Cryptography Extension
[Download jce8](http://www.oracle.com/technetwork/java/javase/downloads/jce8-download-2133166.html){:target="_blank"}

unzip local_policy.jar and copy to java security folder:
```shell
cp local_policy.jar /opt/jre1.8.0_102/lib/security/
```

## Enable GSSAPI in Openfire server
Add the following parameters in system properties in openfire:
http://openfireserver:9090/server-properties.jsp
```shell
sasl.gssapi.config	/etc/openfire/conf/gss.conf
sasl.gssapi.debug	true
sasl.gssapi.useSubjectCredsOnly	false
sasl.mechs	GSSAPI,PLAIN
sasl.realm	SIDDOU.TK
xmpp.fqdn	openfire.siddou.tk

#might be required:
xmpp.server.certificate.accept-selfsigned	true
xmpp.server.certificate.verify	false
xmpp.server.certificate.verify.chain	false
```
```shell
nano /etc/openfire/conf/gss.conf
```
```shell
com.sun.security.jgss.accept { 
com.sun.security.auth.module.Krb5LoginModule 
required 
storeKey=true 
keyTab="/etc/openfire/krb5.xmpp.keytab" 
doNotPrompt=true 
useKeyTab=true 
realm="SIDDOU.TK" 
principal="xmpp/openfire.siddou.tk@SIDDOU.TK"
debug=true 
isInitiator=false; 
};
```

## Create keytab
```shell
kinit domainadmin
net ads keytab add xmpp -k
ktutil
	rkt /etc/krb5.keytab
	delent # remove everything other than xmpp principle
	wkt /etc/openfire/krb5.xmpp.keytab
	exit
chown openfire:openfire /etc/openfire/krb5.xmpp.keytab
```

Finally restart server:
```shell
systemctl restart openfire
```

## Client configuration
host must be joined to the domain.
libsasl2-modules-gssapi-mit should be installed
Tested pigin version is 2.12.0-1

Configure account without a password, done.
debug windows:
```shell
(16:55:30) jabber: Recv (311): <stream:features><starttls xmlns="urn:ietf:params:xml:ns:xmpp-tls"></starttls><mechanisms xmlns="urn:ietf:params:xml:ns:xmpp-sasl"><mechanism>PLAIN</mechanism><mechanism>GSSAPI</mechanism></mechanisms><compression xmlns="http://jabber.org/features/compress"><method>zlib</method></compression></stream:features>
(16:55:30) jabber: Recv (ssl)(453): <?xml version='1.0' encoding='UTF-8'?><stream:stream xmlns:stream="http://etherx.jabber.org/streams" xmlns="jabber:client" from="openfireserver.siddou.tk" id="5vjzc0rrvy" xml:lang="en" version="1.0"><stream:features><mechanisms xmlns="urn:ietf:params:xml:ns:xmpp-sasl"><mechanism>PLAIN</mechanism><mechanism>GSSAPI</mechanism></mechanisms><compression xmlns="http://jabber.org/features/compress"><method>zlib</method></compression></stream:features>
(16:55:30) sasl: Mechs found: PLAIN GSSAPI
(16:55:30) sasl: GSSAPI client step 1
(16:55:30) jabber: Sending (ssl) (siddou@openfireserver): <auth xmlns='urn:ietf:params:xml:ns:xmpp-sasl' mechanism='GSSAPI' xmlns:ga='http://www.google.com/talk/protocol/auth' ga:client-uses-full-bind-result='true'>password removed</auth>
(16:55:30) sasl: GSSAPI client step 1
(16:55:30) sasl: GSSAPI client step 2
```

{% include disqus.html %}