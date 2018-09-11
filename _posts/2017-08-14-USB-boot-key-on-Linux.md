---
title:  "USB boot key on Linux"
tags:
  - linux
---

```shell
sudo dd if=debian-9.1.0-amd64-netinst.iso of=/dev/sdx bs=4M && sync
```