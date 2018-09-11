---
title:  "Install Openvpn + CRL + OTP on Debian 7 Wheezy"
tags:
  - debian
  - wheezy
  - debian 7
  - linux
---

OpenVPN is a powerfull SSL VPN very easy to set up on both server and client side.
In this post i’ll configure it with strong security settings, including “certificate revocation” and “One Time Password” user auth.

### Server
Package installation
```shell
apt-get install openvpn
```
Create a folder for the CA (should be on another server if possible)
```shell
mkdir /home/easy-rsa/
cp -r /usr/share/doc/openvpn/examples/easy-rsa/2.0/* /home/easy-rsa/
chmod 700 /home/easy-rsa
```
Create CA cert
```shell
nano /home/easy-rsa/vars
```
```shell
...
export KEY_SIZE=2048
 
# In how many days should the root CA key expire?
export CA_EXPIRE=1095
 
# In how many days should certificates expire?
export KEY_EXPIRE=730
 
# These are the default values for fields
# which will be placed in the certificate.
# Don't leave any of these fields blank.
export KEY_COUNTRY="US"
export KEY_PROVINCE="CA"
export KEY_CITY="SanFrancisco"
export KEY_ORG="Fort-Funston"
export KEY_EMAIL="me@myhost.mydomain"
export KEY_EMAIL=mail@host.domain
export KEY_CN=changeme
export KEY_NAME=changeme
"export KEY_OU=changeme
export PKCS11_MODULE_PATH=changeme
export PKCS11_PIN=1234
```
```shell
cd /home/easy-rsa
source vars
./clean-all
./build-ca
```
Create Server cert and dh2048.pem
```shell
./build-key-server openvpn-SRV
./build-dh
```
Create a dummy user to generate crl.pem:
```shell
./build-key dummy-user
./revoke-full dummy-user
./list-crl
cat keys/index.txt
```
Warning: Now each time ./revoke-full is used you need to copy the crl.pem in openvpn folder:
```shell
cp /home/easy-rsa/keys/crl.pem /etc/openvpn/
```
Create ta.key
```shell
cd /home/easy-rsa/keys
openvpn --genkey --secret ta.key
```
OpenVPN server configuration:
```shell
mkdir /var/log/openvpn
nano /etc/openvpn/server.conf
```
```shell
local 192.168.0.2 # changethis
port 1194
proto udp
dev tun
 
ca /home/easy-rsa/keys/ca.crt
cert /home/easy-rsa/keys/openvpn-SRV.crt
key /home/easy-rsa/keys/openvpn-SRV.key
dh /home/easy-rsa/keys/dh2048.pem
 
crl-verify crl.pem
 
server 10.8.0.0 255.255.255.0
push "redirect-gateway def1 bypass-dhcp"
push "dhcp-option DNS 192.168.0.251"
push "dhcp-option DNS 192.168.0.252"
push "dhcp-option DOMAIN siddou.com"
push "dhcp-option SEARCH siddou.com"
 
keepalive 10 120
 
tls-auth /home/easy-rsa/keys/ta.key 0
 
cipher AES-256-CBC
 
comp-lzo
 
max-clients 10
 
user nobody
group nogroup
 
persist-key
persist-tun
 
status /var/log/openvpn/openvpn-status.log
log-append  /var/log/openvpn/openvpn.log
verb 3
mute 10
```
Enable IP Forwarding
```shell
nano /etc/sysctl.conf
```
```shell
net.ipv4.ip_forward = 1
```
verify
```shell
sysctl -p
```
Configure iptables:

Warning, if you use a public IP (no firewall in front) you have to adjust,
with INPUT FORWARD and OUTPUT to DROP then open ports you need 22 tcp,1194 udp…
```shell
nano /etc/fwrules
```
```shell
*nat
-A POSTROUTING -s 10.8.0.0/27 -o eth0 -j MASQUERADE
COMMIT
*filter
-P INPUT ACCEPT
-P FORWARD ACCEPT
-P OUTPUT ACCEPT
COMMIT
```
```shell
nano /etc/network/interfaces
```
```shell
# The primary network interface
auto eth0
iface eth0 inet static
address 192.168.0.2 # replace IP..
netmask 255.255.255.0
gateway 192.168.0.1
pre-up iptables-restore < /etc/fwrules
```
Configure fail2ban
```shell
apt-get install fail2ban
nano /etc/fail2ban/jail.conf
```
```shell
#at the end add:
[openvpn]
 
enabled = true
port = 1194
protocol = udp
filter = openvpn
logpath = /var/log/openvpn/openvpn.log
maxretry = 6
```
```shell
nano /etc/fail2ban/filter.d/openvpn.conf
```
```shell
[Definition]
failregex = <HOST>:\d{1,5} TLS Auth Error
    <HOST>:\d{1,5} VERIFY ERROR:
    <HOST>:\d{1,5} TLS Error: TLS handshake failed
```
```shell
service fail2ban restart
```
Create a cert for the client:
```shell
cd /home/easy-rsa
source vars
./build-key plasc
```
Finally restart the server and
```shell
service openvpn restart
```
### Client
```shell
apt-get install openvpn resolvconf
```
resolvconf is required for the “update-resolv-conf” script

Now get the following files from the server located into /home/easy-rsa/keys/:
* CA.CRT
* TA.KEY
* PLASC.CRT
* PLASC.KEY

And copy them into /etc/openvpn/ on the client.

Client configuration:
```shell
nano /etc/openvpn/client.conf
```
```shell
client
dev tun
proto udp
remote 192.168.0.2 1194 #change this
resolv-retry infinite
nobind
persist-key
persist-tun
ca ca.crt
cert plasc.crt
key plasc.key
tls-auth ta.key 1
cipher AES-256-CBC
comp-lzo
verb 3
mute 10
script-security 2
up /etc/openvpn/update-resolv-conf
down /etc/openvpn/update-resolv-conf
```
Finally restart openvpn
```shell
service openvpn restart
```
```shell
root@openvpn-client:/etc/openvpn# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 16436 qdisc noqueue state UNKNOWN 
...
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP qlen 1000
...
38: tun0: <POINTOPOINT,MULTICAST,NOARP,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UNKNOWN qlen 100
    link/none 
    inet 10.8.0.6 peer 10.8.0.5/32 scope global tun0
```
```shell
cat /etc/resolv.conf
```
```shell
# Dynamic resolv.conf(5) file for glibc resolver(3) generated by resolvconf(8)
#     DO NOT EDIT THIS FILE BY HAND -- YOUR CHANGES WILL BE OVERWRITTEN
nameserver 192.168.0.251
nameserver 192.168.0.252
search siddou.com
```
### Set Up OTP with google-authenticator
On server
```shell
apt-get install libqrencode3
```
No package for Wheezy but we can easily install jessie package:
```shell
wget http://ftp.fr.debian.org/debian/pool/main/g/google-authenticator/libpam-google-authenticator_20130529-2_amd64.deb
dpkg -i libpam-google-authenticator_20130529-2_amd64.deb
```
```shell
nano /etc/pam.d/openvpn
```
```shell
#
# /etc/pam.d/common-account - authorization settings common to all services
#
# This file is included from other service-specific PAM config files,
# and should contain a list of the authorization modules that define
# the central access policy for use on the system.  The default is to
# only deny service to users whose accounts are expired in /etc/shadow.
#
# As of pam 1.0.1-6, this file is managed by pam-auth-update by default.
# To take advantage of this, it is recommended that you configure any
# local modules either before or after the default block, and use
# pam-auth-update to manage selection of other modules.  See
# pam-auth-update(8) for details.
#
 
# here are the per-package modules (the "Primary" block)
account [success=1 new_authtok_reqd=done default=ignore]        pam_unix.so
# here's the fallback if no module succeeds
account requisite                       pam_deny.so
# prime the stack with a positive return value if there isn't one already;
# this avoids us returning an error just because nothing sets a success code
# since the modules above will each just jump around
account required                        pam_permit.so
# and here are more per-package modules (the "Additional" block)
# end of pam-auth-update config
auth requisite pam_google_authenticator.so forward_pass
auth required pam_unix.so use_first_pass
```
add 2 lines in the config and restart openvpn
```shell
nano /etc/openvpn/server.conf
```
```shell
plugin /usr/lib/openvpn/openvpn-auth-pam.so openvpn
reneg-sec 0
```
```shell
service openvpn restart
```
Setup user authentication:
```shell
adduser plasc
passwd: 1234
su - plasc
google-authenticator
```
```shell
Do you want authentication tokens to be time-based (y/n) y
https://www.google.com/chart?chs=200x200&chld=M|0&cht=qr&chl=otpauth://totp/user@openvpn-server%XXsecret%XXXXXXXXXXXXXXXXX
```
[![]({{ "/assets/images/qrcode-298x300.png" | absolute_url }}){:height="50%" width="50%"}]({{ "/assets/images/qrcode-298x300.png" | absolute_url }})

```shell
Your new secret key is: XXXXXXXXXXXXXXXX
Your verification code is 111111
Your emergency scratch codes are:
  22222222
  33333333
 
 
Do you want me to update your "/home/plasc/.google_authenticator" file (y/n) y
 
Do you want to disallow multiple uses of the same authentication
token? This restricts you to one login about every 30s, but it increases
your chances to notice or even prevent man-in-the-middle attacks (y/n) y
 
By default, tokens are good for 30 seconds and in order to compensate for
possible time-skew between the client and the server, we allow an extra
token before and after the current time. If you experience problems with poor
time synchronization, you can increase the window from its default
size of 1:30min to about 4min. Do you want to do so (y/n) n
 
If the computer that you are logging into isn't hardened against brute-force
login attempts, you can enable rate-limiting for the authentication module.
By default, this limits attackers to no more than 3 login attempts every 30s.
Do you want to enable rate-limiting (y/n) y
```
On the client cellphone install google authenticator app:
[android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=en){:target="_blank"}
[apple](https://itunes.apple.com/en/app/google-authenticator/id388497605?mt=8){:target="_blank"}
and scan the QR code displayed on the server

[![]({{ "/assets/images/androidopenvpn.png" | absolute_url }}){:height="50%" width="50%"}]({{ "/assets/images/androidopenvpn.png" | absolute_url }})



On client
add 3 lines in the config and restart openvpn
```shell
nano /etc/openvpn/client.conf
```
```shell
auth-user-pass
auth-nocache
reneg-sec 0
```
```shell
service openvpn restart
```
Auth Username is the name of the user
Auth Password is the user password + the 6 number on google auth ex: 1234383360
```shell
[....] Starting virtual private network daemon: clientEnter Auth Username:plasc
Enter Auth Password: 1234383360
. ok
```

{% include toc title="Table of Contents" %}