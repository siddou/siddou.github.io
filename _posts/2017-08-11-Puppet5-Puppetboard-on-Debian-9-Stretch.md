---
title:  "Puppet5+Puppetboard on Debian 9 Stretch"
tags:
  - puppet
  - debian
  - stretch
  - debian 9
  - linux
---

6GB RAM min required

install java:
```shell
apt-get install openjdk-8-jdk-headless
```
add puppet5 repo:
```shell
wget https://apt.puppetlabs.com/puppet5-release-jessie.deb
dpkg -i puppet5-release-jessie.deb
```
add jessie repo for libreadline6
```shell
echo "deb http://ftp.fr.debian.org/debian/ jessie main" > /etc/apt/sources.list.d/jessie.list
apt-get update
apt-get -t jessie install libreadline6
rm puppet5-release-jessie.deb /etc/apt/sources.list.d/jessie.list
apt-get update
```
Install puppet5
```shell
apt-get install puppetserver
ln -s /opt/puppetlabs/bin/puppet /usr/bin/
systemctl enable puppetserver
systemctl start puppetserver
puppet agent --test --server=puppet5.siddou.com
```
Install puppetdb:
```shell
apt-get install puppetdb puppetdb-termini postgresql postgresql-contrib apt-transport-https
puppet module install puppetlabs-puppetdb
```
```shell
nano /etc/puppetlabs/code/environments/manifests/site.pp
```
```ruby
node puppet5 {
  class { 'puppetdb': }
  class { 'puppetdb::master::config': }
}
```
```shell
puppet agent --test --server=puppet5.siddou.com
puppet resource service puppetdb ensure=running enable=true
```
check:
```shell
tail /var/log/puppetlabs/puppetdb/puppetdb.log
```
If JAVA SSL problem:
```shell
puppetdb ssl-setup
```
Install Puppetboard:
```shell
nano /etc/puppetlabs/puppet/puppet.conf
```
add:
```shell
[master]
..
reports = store,puppetdb
 
[agent]
runinterval=1800
report = true
 
 
[main]
server = puppet5.siddou.com
```
```shell
systemctl restart puppetserver
puppet agent --test
```

```shell
nano /etc/puppetlabs/code/environments/manifests/site.pp
```
```ruby
node puppet5 {
  class { 'puppetdb': }
  class { 'puppetdb::master::config': }
  class { 'apache':
    default_vhost => false,
}
  class { 'apache::mod::wsgi': }
  class { 'puppetboard':
    manage_git        => 'latest',
    manage_virtualenv => 'latest',
}
  class { 'puppetboard::apache::vhost':
    vhost_name           => 'puppet5',
    port                 => 443,
    ssl                  => true,
    ssl_key              => "/etc/puppetlabs/puppet/ssl/private_keys/puppetboard.siddou.com.pem",
    ssl_cert             => "/etc/puppetlabs/puppet/ssl/certs/puppetboard.siddou.com.pem",
}
}
```

```shell
apt-get install virtualenv
puppet module install puppetlabs-apache
puppet module install puppet-puppetboard
 
puppet cert generate puppetboard.siddou.com
puppet agent --test
```
go to https://puppet5serverIP


{% include comments.html %}