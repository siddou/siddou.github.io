---
title: "Debian repositories"
permalink: /debian-repositories/
tags:
  - Debian
comments: true
---

{% include toc title="Table of Contents" %}

### Timeline
[![]({{ "/assets/images/debian/timeline_debian_1993_20111.png" | absolute_url }}){:class="img-responsive"}]({{ "/assets/images/debian/timeline_debian_1993_20111.png" | absolute_url }})

### Lenny
![]({{ "/assets/images/debian/Id_2784_lenny.jpg" | absolute_url }}){:class="img-responsive"}

```shell
deb http://mirrors.fe.up.pt/debian-archive/debian/ lenny main
```

### Squeeze
![]({{ "/assets/images/debian/squeeze.jpg" | absolute_url }}){:height="60%" width="60%"}

```shell
deb http://ftp.fr.debian.org/debian/ squeeze main
deb-src http://ftp.fr.debian.org/debian/ squeeze main
 
deb http://security.debian.org/ squeeze/updates main
deb-src http://security.debian.org/ squeeze/updates main
 
deb http://ftp.fr.debian.org/debian/ squeeze-updates main
deb-src http://ftp.fr.debian.org/debian/ squeeze-updates main
```

### Wheezy
![]({{ "/assets/images/debian/wheezy.jpg" | absolute_url }}){:class="img-responsive"}

```shell
deb http://ftp.fr.debian.org/debian/ wheezy main
deb-src http://ftp.fr.debian.org/debian/ wheezy main
 
deb http://security.debian.org/ wheezy/updates main
deb-src http://security.debian.org/ wheezy/updates main
 
deb http://ftp.fr.debian.org/debian/ wheezy-updates main
deb-src http://ftp.fr.debian.org/debian/ wheezy-updates main
```

### Jessie
![]({{ "/assets/images/debian/toy_story_jessie.jpg" | absolute_url }}){:height="50%" width="50%"}

```shell
deb http://ftp.fr.debian.org/debian/ jessie main
deb-src http://ftp.fr.debian.org/debian/ jessie main
 
deb http://security.debian.org/ jessie/updates main
deb-src http://security.debian.org/ jessie/updates main
 
deb http://ftp.fr.debian.org/debian/ jessie-updates main
deb-src http://ftp.fr.debian.org/debian/ jessie-updates main
```

### stretch
![]({{ "/assets/images/debian/Stretch.jpg" | absolute_url }}){:class="img-responsive"}

```shell
deb http://ftp.fr.debian.org/debian/ stretch main
deb-src http://ftp.fr.debian.org/debian/ stretch main
 
deb http://security.debian.org/ stretch/updates main
deb-src http://security.debian.org/ stretch/updates main
 
deb http://ftp.fr.debian.org/debian/ stretch-updates main
deb-src http://ftp.fr.debian.org/debian/ stretch-updates main
```

### Buster
![]({{ "/assets/images/debian/buster.png" | absolute_url }}){:class="img-responsive"}

```shell
deb http://ftp.fr.debian.org/debian/ buster main
deb-src http://ftp.fr.debian.org/debian/ buster main
 
deb http://security.debian.org/ buster/updates main
deb-src http://security.debian.org/ buster/updates main
 
deb http://ftp.fr.debian.org/debian/ buster-updates main
deb-src http://ftp.fr.debian.org/debian/ buster-updates main
```

{% include comments.html %}