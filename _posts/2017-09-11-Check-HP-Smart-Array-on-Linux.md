# Check Raid controller
```shell
lspci | grep RAID
03:00.0 RAID bus controller: Hewlett-Packard Company Smart Array Gen9 Controllers (rev 01)
```

# Add hp repo
```shell
apt-get install curl
nano /etc/apt/sources.list
```
:arrow_right: for jessie :
```shell
deb http://downloads.linux.hpe.com/SDR/repo/mcp jessie/current non-free
```

:arrow_right: for stretch :
```shell
deb http://downloads.linux.hpe.com/SDR/repo/mcp/ stretch/current non-free
```

enroll apt keys and update
```shell
curl http://downloads.linux.hpe.com/SDR/hpPublicKey1024.pub | apt-key add -
curl http://downloads.linux.hpe.com/SDR/hpPublicKey2048.pub | apt-key add -
curl http://downloads.linux.hpe.com/SDR/hpPublicKey2048_key1.pub | apt-key add -
curl http://downloads.linux.hpe.com/SDR/hpePublicKey2048_key1.pub | apt-key add -

apt-get update
```

:warning: Other key may be appear in : http://downloads.linux.hpe.com/keys.html


# Installation

:arrow_right: for wheezy
```shell
apt-get install hpacucli
```

:arrow_right: for jessie and newer :
```shell
apt-get install ssacli       # May change in the future
```

# ensure of retrocompatibility

make an alias of 'ssacli' commands to 'hpssacli' :

```shell
ln -s /usr/sbin/ssacli /usr/sbin/hpssacli
```

# Use :

### show disk details
```shell
hpssacli ctrl all show config
```

### Determine wich one is sda, sdb, etc..
```shell
hpssacli
=> controller slot=0 logicaldrive all show detail
=> exit
```