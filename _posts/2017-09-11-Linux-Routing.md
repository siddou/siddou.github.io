---
tags:
  - linux
  - route
---

### List routes
```bash
sudo route -n
sudo ip route
```

### Add new route
```bash
sudo route add -net 192.168.15.0 netmask 255.255.255.0 gw 10.255.11.6
sudo ip route add 192.168.15.0/24 dev enp3s0
```

### Delete old route
```bash
sudo route del -net 192.168.15.0 netmask 255.255.255.0 gw 10.255.11.4
sudo ip route del 192.168.15.0/24
```
{% include comments.html %}