---
title:  "Linux bonding, increase network bandwidth"
tags:
  - linux
  - bonding
---

### Hardware Setup
Server 1 and 2 have 4 1GB nic:
eno1 connected lan
eno2,eno3 and eno4 directly connected their respective ports on the other server for bonding with cat 6 or 7 rj45 cables.

### Install package
```shell
apt-get install ifenslave
```
### Configure the bond interface for both server
```shell
auto eno2
iface eno2 inet manual
bond-master bond0
 
auto eno3
iface eno3 inet manual
bond-master bond0
 
auto eno4
iface eno4 inet manual
bond-master bond0
 
auto bond0
iface bond0 inet static
      address 192.168.30.1 #192.168.30.2 for server 2 
      netmask 255.255.255.252
      mtu 9000
      bond-slaves eno2 eno3 eno4
      bond_mode balance-rr
      bond_miimon 100
      bond_downdelay 200
      bond_updelay 200
```

mtu value:
9000 for jumbo frames

bond value:
I choose round robin for increased bandwidth and fault tolerance

balance-rr vs 802.3ad, check [here](http://www.enterprisenetworkingplanet.com/linux_unix/article.php/3850636/Understanding-NIC-Bonding-with-Linux.htm){:target="_blank"}

### Monitor bond interface
restart both server to ensure configuration is correct then:
```shell
cat /proc/net/bonding/bond0
cat /var/log/syslog | grep bond0
ip a
```
```shell
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state 
2: eno1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq 
 
3: eno2: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 9000 qdisc mq master bond0 state UP group default qlen 1000
 
4: eno3: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 9000 qdisc mq master bond0 state UP group default qlen 1000
 
5: eno4: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 9000 qdisc mq master bond0 state UP group default qlen 1000
 
7: bond0: <BROADCAST,MULTICAST,MASTER,UP,LOWER_UP> mtu 9000 qdisc noqueue state UP group default qlen 1000
```
### Monitor bandwith
```shell
apt-get install iperf dstat
```
open 2 shell on server1:

```shell
iperf -s
dstat -N eno1,eno2,eno3,eno4,bond0
```
on server2:
First test using eno1
```shell
iperf -c server1_eno1_IP -d
[  6]  0.0-10.0 sec  1.08 GBytes   927 Mbits/sec
[  4]  0.0-10.0 sec  1.09 GBytes   930 Mbits/sec
```
Then with using bond0
```shell
iperf -c 192.168.30.1 -d
[  6]  0.0-10.0 sec  2.86 GBytes  2.46 Gbits/sec
[  5]  0.0-10.0 sec  2.86 GBytes  2.45 Gbits/sec
```

[![]({{ "/assets/images/dstatbonding.png" | absolute_url }}){:height="50%" width="50%"}]({{ "/assets/images/dstatbonding.png" | absolute_url }})

pretty nice differences!

{% include comments.html %}