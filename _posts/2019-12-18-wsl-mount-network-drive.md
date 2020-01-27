---
title:  "WSL mount network drive"
tags:
  - wsl
  - linux
---
{% include toc %}
```shell
sudo mkdir /z
sudo nano /etc/fstab
```

```shell
#add
Z: /z drvfs defaults        0 0
```

```shell
sudo mount -a
ls /z
```