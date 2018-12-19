---
title:  "Install rancid and cvsweb on Debian 8 Jessie"
tags:
  - tutorial
  - debian
  - jessie
  - debian 8
  - linux
  - rancid
---

Rancid is a nice tool that connect to your network devices and backup their configuration.
Cvsweb is the web interface to check the configurations files and diff.

{% include toc %}
# Cisco user
```shell
username ranciduser privilege 4 secret 5 gh$j$ghj$ghj$gh$jgh$DFnroHfS8aWBv0
```

# Rancid:
```shell
apt-get install rancid cvsweb
```
```shell
nano /etc/rancid/rancid.conf
```
```shell
...
LIST_OF_GROUPS="group1 group2"; export LIST_OF_GROUPS
...
```

```shell
su - rancid
nano .cloginrc
```
```shell
add method * {ssh}
add user * {ranciduser}
add password * {rancidpassword}
add autoenable * {1}
```
```shell
exit
chmod 600 /var/lib/rancid/.cloginrc
su - rancid
/usr/lib/rancid/bin/rancid-cvs
nano /var/lib/rancid/group1/router.db
```
```shell
192.168.0.252;cisco;up;switch01
```

```shell
nano /var/lib/rancid/group2/router.db
```
```shell
192.168.0.253;cisco;up;switch02
```

```shell
/usr/lib/rancid/bin/rancid-run
exit
```

# Cvsweb:
```shell
nano /etc/cvsweb/cvsweb.conf
```
modify these lines:
```shell
...
'my switches'   => ['my switches Repository', '/var/lib/rancid/CVS'],
...
"hidecvsroot" => "1",
...
```

go to http://server_name/cgi-bin/cvsweb
 to check switches configs

# Cron every week:
```shell
nano /etc/cron.d/rancid
```
```shell
# run config differ hourly
1 * * * * rancid /usr/bin/rancid-run
# clean out config differ logs
50 23 * * * rancid find /var/log/rancid -type f -mtime +2 -exec rm {} \;
```


# Mail alias:
```shell
nano /etc/aliases
```
```shell
rancid: siddou@siddou.github.io
rancid-group1: siddou@siddou.github.io
rancid-admin-group1: siddou@siddou.github.io
rancid-group2: siddou@siddou.github.io
rancid-admin-group2: siddou@siddou.github.io
```
```shell
newaliases
```

# Mail alias fix for exim4:
Thanks to : <a href="http://blog.dhampir.no/content/make-exim4-on-debian-respect-forward-and-etcaliases-when-using-a-smarthost" target="_blank">http://blog.dhampir.no/content/make-exim4-on-debian-respect-forward-and-etcaliases-when-using-a-smarthost</a>

```shell
nano /etc/exim4/conf.d/router/175_cathedral-config_system_aliases
```
```shell
.ifdef DCconfig_smarthost DCconfig_satellite

cathedral_aliases:
  debug_print = "R: cathedral_aliases for $local_part@$domain"
  driver = redirect
  domains = $qualify_domain
  allow_fail
  allow_defer
  data = ${lookup{$local_part}lsearch{/etc/aliases}}
  .ifdef SYSTEM_ALIASES_USER
  user = SYSTEM_ALIASES_USER
  .endif
  .ifdef SYSTEM_ALIASES_GROUP
  group = SYSTEM_ALIASES_GROUP
  .endif
  .ifdef SYSTEM_ALIASES_FILE_TRANSPORT
  file_transport = SYSTEM_ALIASES_FILE_TRANSPORT
  .endif
  .ifdef SYSTEM_ALIASES_PIPE_TRANSPORT
  pipe_transport = SYSTEM_ALIASES_PIPE_TRANSPORT
  .endif
  .ifdef SYSTEM_ALIASES_DIRECTORY_TRANSPORT
  directory_transport = SYSTEM_ALIASES_DIRECTORY_TRANSPORT
  .endif

cathedral_userforward:
  debug_print = "R: cathedral_userforward for $local_part@$domain"
  driver = redirect
  domains = $qualify_domain
  check_local_user
  file = $home/.forward
  require_files = $local_part:$home/.forward
  no_verify
  no_expn
  check_ancestor
  allow_filter
  forbid_smtp_code = true
  directory_transport = address_directory
  file_transport = address_file
  pipe_transport = address_pipe
  reply_transport = address_reply
  skip_syntax_errors
  syntax_errors_to = real-$local_part@$domain
  syntax_errors_text = \
    This is an automatically generated message. An error has\n\
    been found in your .forward file. Details of the error are\n\
    reported below. While this error persists, you will receive\n\
    a copy of this message for every message that is addressed\n\
    to you. If your .forward file is a filter file, or if it is\n\
    a non-filter file containing no valid forwarding addresses,\n\
    a copy of each incoming message will be put in your normal\n\
    mailbox. If a non-filter file contains at least one valid\n\
    forwarding address, forwarding to the valid addresses will\n\
    happen, and those will be the only deliveries that occur.

.endif
```


```shell
nano /etc/exim4/update-exim4.conf.conf
```
```shell
dc_eximconfig_configtype='satellite'
dc_other_hostnames='localhost'
dc_local_interfaces='127.0.0.1'
dc_readhost=''
dc_relay_domains=''
dc_minimaldns='false'
dc_relay_nets=''
dc_smarthost='mail_server_name'
CFILEMODE='644'
dc_use_split_config='true'
dc_hide_mailname='true'
dc_mailname_in_oh='true'
dc_localdelivery='mail_spool'
```
```shell
systemctl restart exim4
```

# Apache2 ldap config:
conf apache2:
```shell
       ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/
       <Directory "/usr/lib/cgi-bin">
               Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
               AllowOverride None
               Order allow,deny
               Allow from all
               AuthType Basic
               AuthName "admin Authentication"
               AuthBasicProvider ldap
               AuthLDAPURL ldaps://ldap/ou=Users,dc=siddou,dc=com?uid
               AuthLDAPBindDN cn=ldap,dc=siddou,dc=com
               AuthLDAPBindPassword xxxxxxxxxxxx
               AuthLDAPGroupAttributeIsDN off
               AuthLDAPGroupAttribute memberUid
               ErrorDocument 401 "Wrong credentials!<br>"
               Require ldap-group cn=it,ou=Groups,dc=siddou,dc=com
       </Directory>

ScriptAlias /cvsweb/cvsweb /usr/lib/cgi-bin/cvsweb
Alias /cvsweb /usr/share/cvsweb
```
```shell
a2enmod authnz_ldap
systemctl restart apache2
```

{% include disqus.html %}