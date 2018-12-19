---
title:  "install SugarCRM 7.6 Ent on Debian 7 Wheezy"
tags:
  - sugarcrm
  - tutorial
  - debian
  - debian 7
  - wheezy
  - linux
---
{% include toc %}
[SugarCRM](https://www.sugarcrm.com/){:target="_blank"} is nice CRM on linux.
There is a community version but this install is about Entreprise version 7.6

About Sugar_Version 7.6 Ent:
It won't install on Jessie without big tweaks because it use PHP 5.4. Also setup wizard couldn't find recent version of elastisearch so i had to stick to supported version 1.44.


Sources:
- [Supported_Platforms](http://support.sugarcrm.com/Resources/Supported_Platforms/index.html){:target="_blank"}
- [Installation_and_Upgrade_Guide](https://support.sugarcrm.com/Documentation/Sugar_Versions/7.6/Ent/Installation_and_Upgrade_Guide/){:target="_blank"}


# Install
```shell
apt-get install mysql-server apache2 unzip php5 php5-mysql curl libcurl3 libcurl3-dev php5-curl chkconfig php5-gd php5-imap php5-mcrypt
```

Finish mySQL install
```shell
mysql_secure_installation
```

Create sugar admin
```shell
mysql -u root -p
mysql> GRANT ALL PRIVILEGES ON sugarcrm.* TO admin@localhost IDENTIFIED BY 'secret_password';
```

Get software and unzip to apache dir
```shell
mv SugarEnt-Full-7.6.1.0 /var/www/sugar
chown -R www-data:www-data /var/www/sugar
```

# Configure php
```shell
nano /etc/php5/apache2/php.ini
```
```shell
upload_max_filesize = 100M
memory_limit = 512M
post_max_size = 100M
```

# Configure apache2+https

```shell
nano /etc/apache2/sites-enabled/000-default
```
```shell
<VirtualHost *:80>
   ServerName crm
   Redirect permanent / https://crm
</VirtualHost>

<VirtualHost *:443>
	ServerAdmin webmaster@localhost
        ServerName  crm

	DocumentRoot /var/www/sugar
	#<Directory />
	#	Options FollowSymLinks
	#	AllowOverride None
	#</Directory>
	<Directory /var/www/sugar>
	#	Options Indexes FollowSymLinks MultiViews
	#	AllowOverride all
	#	Order allow,deny
	#	allow from all
		Options None
		AllowOverride None
		Order allow,deny
		Allow from all	

SetOutputFilter DEFLATE
AddOutputFilterByType DEFLATE text/html text/plain text/xml text/css text/x-js text/x-javascript application/x-javascript
BrowserMatch ^Mozilla/4 gzip-only-text/html
BrowserMatch ^Mozilla/4.0[678] no-gzip
BrowserMatch bMSIE !no-gzip !gzip-only-text/html
SetEnvIfNoCase Request_URI .(?:gif|jpe?g|png|rar|zip|pdf)$ no-gzip dont-vary
Header append Vary User-Agent

ExpiresActive On
ExpiresDefault A86400
ExpiresByType image/gif A2592000
ExpiresByType image/png A2592000
ExpiresByType image/jpg A2592000


# BEGIN SUGARCRM RESTRICTIONS
RedirectMatch 403 (?i).*\.log$
RedirectMatch 403 (?i)/+not_imported_.*\.txt
RedirectMatch 403 (?i)/+(soap|cache|xtemplate|data|examples|include|log4php|metadata|modules)/+.*\.(php|tpl)
RedirectMatch 403 (?i)/+emailmandelivery\.php
RedirectMatch 403 (?i)/+upload/
RedirectMatch 403 (?i)/+custom/+blowfish
RedirectMatch 403 (?i)/+cache/+diagnostic
RedirectMatch 403 (?i)/+files\.md5$
RedirectMatch 403 (?i)/+composer\.(json|lock)
RedirectMatch 403 (?i)/+vendor/composer/
RedirectMatch 403 (?i).*/\.git

# Fix mimetype for logo.svg (SP-1395)
AddType     image/svg+xml     .svg
AddType     application/json  .json
AddType     application/javascript  .js

<IfModule mod_rewrite.c>
    Options +FollowSymLinks
    RewriteEngine On
    RewriteBase /
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteRule ^rest/(.*)$ api/rest.php?__sugar_url=$1 [L,QSA]
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteRule ^cache/api/metadata/lang_(.._..)_(.*)_public(_ordered)?\.json$ rest/v10/lang/public/$1?platform=$2&ordered=$3 [N,QSA,DPI]

    RewriteRule ^cache/api/metadata/lang_(.._..)_([^_]*)(_ordered)?\.json$ rest/v10/lang/$1?platform=$2&ordered=$3 [N,QSA,DPI]
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteRule ^cache/Expressions/functions_cache(_debug)?.js$ rest/v10/ExpressionEngine/functions?debug=$1 [N,QSA,DPI]
    RewriteRule ^cache/jsLanguage/(.._..).js$ index.php?entryPoint=jslang&module=app_strings&lang=$1 [L,QSA,DPI]
    RewriteRule ^cache/jsLanguage/(\w*)/(.._..).js$ index.php?entryPoint=jslang&module=$1&lang=$2 [L,QSA,DPI]
    RewriteRule ^portal/(.*)$ portal2/$1 [L,QSA]
    RewriteRule ^portal$ portal/? [R=301,L]
</IfModule>

<IfModule mod_mime.c>
    AddType application/x-font-woff .woff
</IfModule>
<FilesMatch "\.(jpg|png|gif|js|css|ico|woff|svg)$">
        <IfModule mod_headers.c>
                Header set ETag ""
                Header set Cache-Control "max-age=2592000"
                Header set Expires "01 Jan 2112 00:00:00 GMT"
        </IfModule>
</FilesMatch>
<IfModule mod_expires.c>
        ExpiresByType text/css "access plus 1 month"
        ExpiresByType text/javascript "access plus 1 month"
        ExpiresByType application/x-javascript "access plus 1 month"
        ExpiresByType image/gif "access plus 1 month"
        ExpiresByType image/jpg "access plus 1 month"
        ExpiresByType image/png "access plus 1 month"
        ExpiresByType application/x-font-woff "access plus 1 month"
        ExpiresByType image/svg "access plus 1 month"
</IfModule>
# END SUGARCRM RESTRICTIONS


	</Directory>
        


	ErrorLog ${APACHE_LOG_DIR}/sugarcrm_error.log

	# Possible values include: debug, info, notice, warn, error, crit,
	# alert, emerg.
	LogLevel warn

	CustomLog ${APACHE_LOG_DIR}/sugarcrm_access.log combined

    # SSL
    SSLEngine on
    SSLProtocol ALL -SSLv2 -SSLv3
    SSLHonorCipherOrder On
    SSLCipherSuite ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+3DES:!aNULL:!MD5:!DSS
    SSLCompression Off
    SSLCertificateFile /etc/ssl/certs/crm.crt
    SSLCertificateKeyFile /etc/ssl/private/crm.key

</VirtualHost>

```


```shell
a2enmod rewrite
a2enmod expires
a2enmod headers
service apache2 restart
```

Install java
```shell
apt-get install openjdk-7-jre-headless
```

Install Elasticsearch
```shell
wget -O - http://packages.elasticsearch.org/GPG-KEY-elasticsearch | apt-key add -
echo 'deb http://packages.elasticsearch.org/elasticsearch/1.4/debian stable main' | tee /etc/apt/sources.list.d/elasticsearch.list
apt-get update
apt-get install elasticsearch=1.4.4
```

```shell
nano /etc/default/elasticsearch
```
```shell
# Run Elasticsearch as this user ID and group ID
ES_USER=elasticsearch
ES_GROUP=elasticsearch

# Heap Size (defaults to 256m min, 1g max)
#ES_HEAP_SIZE=2g

# Heap new generation
#ES_HEAP_NEWSIZE=

# max direct memory
#ES_DIRECT_SIZE=

# Maximum number of open files, defaults to 65535.
#MAX_OPEN_FILES=65535

# Maximum locked memory size. Set to "unlimited" if you use the
# bootstrap.mlockall option in elasticsearch.yml. You must also set
# ES_HEAP_SIZE.
#MAX_LOCKED_MEMORY=unlimited

# Maximum number of VMA (Virtual Memory Areas) a process can own
#MAX_MAP_COUNT=262144

# Elasticsearch log directory
LOG_DIR=/var/log/elasticsearch

# Elasticsearch data directory
DATA_DIR=/var/lib/elasticsearch

# Elasticsearch work directory
WORK_DIR=/tmp/elasticsearch

# Elasticsearch configuration directory
CONF_DIR=/etc/elasticsearch

# Elasticsearch configuration file (elasticsearch.yml)
CONF_FILE=/etc/elasticsearch/elasticsearch.yml

# Additional Java OPTS
#ES_JAVA_OPTS=

# Configure restart on package upgrade (true, every other setting will lead to not restarting)
RESTART_ON_UPGRADE=true
```


```shell
chkconfig elasticsearch on
service elasticsearch restart
```

Done
go to http://crm_IP_OR_Hostname

Follow Setup Wizard
- db name: sugarcrm
- db admin: admin
- db admin password: secret_password

# Setup cron
```shell
crontab -e -u www-data
```
```shell
* * * * * cd /var/www/sugar; php -f cron.php > /dev/null 2>&1
```

# Fix Permission denied errors
```shell
chown -R www-data:www-data /var/www/sugar
find /var/www/sugar/ -type d -exec chmod 775 {} \;
find /var/www/sugar/ -type f -exec chmod 664 {} \;
```

# Configure OpenLDAP backend for users
[Configuring_LDAP_Authentication_Using_Active_Directory](http://support.sugarcrm.com/Knowledge_Base/Administration/Password_Management/Configuring_LDAP_Authentication_Using_Active_Directory/index.html){:target="_blank"}

Go to Admin -> Password Management -> tick Enable LDAP Authentication
```shell
server ldaps://ldapsrv
port number 636
user DN ou=Users,dc=siddou,dc=com
user filter
Bind Attribute dn
Login Attribute uid
Group membership on
group DN ou=Groups,dc=siddou,dc=com
Group Name cn=sugarcrm
User Attribute uid
Group Attribute memberUid
With User DN off

Authentication on
UserName cn=ldapsrv,dc=siddou,dc=com
Password ***********

Auto Create Users on
Encryption Key
```

# Configure Active Directory backend for users
Go to Admin -> Password Management -> tick Enable LDAP Authentication

It wasn't not working for me with server: ad.siddou.com and port:389, so i used ldaps.

```shell
Server: ldaps://ad.siddou.com
Port: 636
User DN: CN=Users,DC=siddou,DC=com
Bind Attribute: userPrincipalName
Login Attribute: sAMAccountName

Group Membership on
Group DN: CN=Users,DC=siddou,DC=com
Group Name: CN=sugarcrm
User Attribute: dn
Group Attribute: member
With User DN off

Authentication on
User Name: administrator@siddou.com

Auto Create Users on
Encryption Key
```

{% include disqus.html %}