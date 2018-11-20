---
title:  "Replicated Local Storage (RLS) with DRBD9+Xen on Ubuntu 16.04LTS Xenial"
tags:
  - DRBD9
  - tutorial
  - ubuntu
  - xenial
  - ubuntu 16.04
  - linux
---
{% include toc %}
# Hardware Setup
Server 1 and 2 have 4 1GB nic:
- eno1 connected lan
- eno2,eno3 and eno4 directly connected their respective ports on the other server for bonding with cat 6 or 7 rj45 cables.

- 2 raid1 HD (raid5 isn't recommended for DRBD)
- sda1 system
- sdb1 lvm type for DRBD

# Setup network+bonding
**on both servers**
```shell
apt-get install ifenslave bridge-utils
```

```shell
nano /etc/network/interfaces
```
```shell
auto lo
iface lo inet loopback

iface eno1 inet manual

auto peth0
iface peth0 inet static
	address 192.168.0.1  #192.168.0.2 on server2
	netmask 255.255.255.0
	gateway 192.168.0.254
        bridge_ports eno1
        bridge_stp off    

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
      address 192.168.30.1 #192.168.30.2 on server2
      netmask 255.255.255.252
      mtu 9000
      bond-slaves eno2 eno3 eno4
      bond_mode balance-rr
      bond_miimon 100
      bond_downdelay 200
      bond_updelay 200
```

check my article about bonding <a href="/Linux-bonding/" target="_blank">here</a>

# Install xen
**on both servers**
check my article about XEN install <a href="/install-xen-on-debian-8-jessie/" target="_blank">here</a>

# Configure LVM
**on both servers**
```shell
nano /etc/lvm/lvm.conf
```
```shell
write_cache_state = 0
```

restart computer, bonding and xen should ok.


# Add DRBD sources
**on both servers**
```shell
nano /etc/apt/sources.list.d/linbit-ubuntu-linbit-drbd9-stack-xenial.list
```
```shell
deb-src http://ppa.launchpad.net/linbit/linbit-drbd9-stack/ubuntu xenial main
```

```shell
apt-get install wget
wget -O- http://packages.linbit.com/gpg-pubkey-53B3B037-282B6E23.asc | apt-key add -
apt-key add gpg-pubkey-53B3B037-282B6E23.asc
apt-get update
```

# Install DRBD9
**on both servers**
```shell
apt-get install drbd-utils python-drbdmanage drbd-dkms
```


# Configure the DRBD9 pool
**on both servers**
```shell
vgcreate drbdpool /dev/sdb1
```


```shell
apt-get install thin-provisioning-tools
lvcreate -L 499G --thinpool drbdthinpool drbdpool
```
Leave a little free space on drbdpool or else it will fail to create the thinpool


# Configure DRBD9 cluster
**on server 1:**
copy key on server2 and test ssh root@192.168.30.2
```shell
ssh-keygen
ssh-copy-id root@192.168.30.2
```

**on server 2:**
copy key on server1 and test ssh root@192.168.30.1
```shell
ssh-keygen
ssh-copy-id root@192.168.30.1
```

**on server 1:**
```shell
drbdmanage init 192.168.30.1
```
```shell
drbdmanage add-node server2 192.168.30.2
```

Configuring storage plugins:
```shell
drbdmanage modify-config
```
```shell
[GLOBAL]
loglevel = INFO
storage-plugin = drbdmanage.storage.lvm_thinlv.LvmThinLv
```

```shell
drbdmanage modify-config --node server1
```
```shell
[Node:server1]
[Plugin:ThinLV]
pool-name = drbdthinpool
```

```shell
drbdmanage modify-config --node server2
```
```shell
[Node:server2]
[Plugin:ThinLV]
pool-name = drbdthinpool
```
Restart both server.

# Create disk for our first Xen Virtual machine
**on server 1:**
```shell
drbdmanage add-volume VM-disk 10G --deploy 2
drbdmanage list-resources 
drbdadm status
drbdmanage list-volumes --groupby Size
```


# Check if VM-disk is present on both server
```shell
drbdsetup status --verbose --statistics
lvdisplay /dev/drbdpool | grep "LV Path"
```
```shell
  LV Path                /dev/drbdpool/.drbdctrl_0
  LV Path                /dev/drbdpool/.drbdctrl_1
  LV Path                /dev/drbdpool/VM-disk_00
```
If VM-disk_00 is not on server2, stop right here something wrong with the cluster!

Check drbdmanage config on both node: especially storage-plugin and pool-name
delete VM-disk and restart to apply changes.

# Install VM with xen-tools
First i create a base vm on system disk:
```shell
xen-create-image --hostname=base --dhcp --vcpus=2 --pygrub --dist=xenial
```

Then i copy it on the DRBD ressource:
```shell
apt-get install dcfldd
dcfldd if=/dev/rootvg/base-disk of=/dev/drbd/by-res/VM-disk/0 bs=1M
```

Create a xen config:
```shell
nano /etc/xen/VM.cfg
```
```shell
bootloader = '/usr/lib/xen-4.6/bin/pygrub'
vcpus       = '20'
memory      = '16384'
root        = '/dev/xvda2 ro'
disk        = [
                  'phy:/dev/drbd/by-res/VM-disk/0,xvda2,w',
              ]
name        = 'VM'
dhcp        = 'dhcp'
vif         = [ 'mac=00:cc:3E:86:3C:c1,bridge=peth0' ]

on_poweroff = 'destroy'
on_reboot   = 'restart'
on_crash    = 'restart'
```

Check drbd status:
```shell
drbdsetup status
.drbdctrl role:Primary
  volume:0 disk:UpToDate
  volume:1 disk:UpToDate
  server2 role:Secondary
    volume:0 peer-disk:UpToDate
    volume:1 peer-disk:UpToDate

VM role:Secondary
  disk:UpToDate
  server2 role:Secondary
    peer-disk:UpToDate
```

As soon as we launch the VM on server 1 the VM DRBD ressource will be **automatically** promoted to primary
and will not be mountable/usable on server2.

Start vm on server1:
```shell
xl create /etc/xen/VM.cfg
```

Check drbd status:
```shell
.drbdctrl role:Primary
  volume:0 disk:UpToDate
  volume:1 disk:UpToDate
  server2 role:Secondary
    volume:0 peer-disk:UpToDate
    volume:1 peer-disk:UpToDate

VM role:Primary
  disk:UpToDate
  server2 role:Secondary
    peer-disk:UpToDate
```


# drbdmanage common operations
## snapshot & duplicate
```shell
drbdmanage create-snapshot VM-disk-snap VM-disk server1
drbdmanage restore-snapshot VM-disk2  VM-disk VM-disk-snap
drbdmanage remove-snapshot VM-disk VM-disk-snap

drbdmanage list-snapshots
drbdmanage list-resources
```

## Resize
```shell
drbdmanage list-volumes
```
Add 10G to a 50G vm:
```shell
drbdmanage resize-volume VM-disk2 0 60GiB
```

**Cannot reduce,rename with drbdmanage yet**

## remove
```shell
drbdmanage list-volumes
drbdmanage list-resources
drbdmanage remove-volume VM-disk 0
drbdmanage remove-resource VM-disk
```

## Show DRBD9 ressources disks
```shell
apt-get install tree
```
```shell
tree /dev/drbd/by-res
/dev/drbd/by-res/VM-disk2/0
```

## Backup VM
```shell
lvcreate -L 50,05G -n VM-backup /dev/datavg
drbdmanage create-snapshot VM-snap VM server1
ionice -c2 -n7 dcfldd if=/dev/drbdpool/VM.VM-snap_00 of=/dev/datavg/VM-backup bs=1M
drbdmanage remove-snapshot VM VM-snap
```

## Split Brain/Standalone mode Recover
server1 got our latest datas, we need to resync server2:

on server2:
```shell
drbdadm disconnect .drbdctrl
drbdadm secondary .drbdctrl
drbdadm connect --discard-my-data .drbdctrl
```

on server1:
```shell
drbdadm disconnect .drbdctrl
drbdadm connect .drbdctrl
```

on server2:
```shell
drbdadm disconnect VM-disk
drbdadm secondary VM-disk
drbdadm connect --discard-my-data VM-disk
```

on server1:
```shell
drbdadm disconnect VM-disk
drbdadm connect VM-disk
```

# Next step configure HA Cluster with PCS
...

# auto start drbd if you won't use an HA cluster manager
```shell
nano /etc/systemd/system/drbdmanaged.service
```
```shell
[Unit]
Description=DRBDManage Service
Documentation=https://www.drbd.org/en/doc/users-guide-90
Requires=dbus.service
Wants=network-online.target sshd.service
After=network-online.target sshd.service

[Service]
ExecStart=//usr/bin/python /usr/bin/dbus-drbdmanaged-service
User=root
PrivateTmp=yes

[Install]
WantedBy=multi-user.target
```

```shell
systemctl enable drbdmanaged
```

reboot and check:
```shell
systemctl status drbdmanaged -l
drbdsetup status --verbose --statistics
```

[users-guide-90](https://www.drbd.org/en/doc/users-guide-90){:target="_blank"}


{% include disqus.html %}