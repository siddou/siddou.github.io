---
title:  "Puppet apt hiera sample"
tags:
  - puppet
---

```yaml
---
apt::sources:
  'stretch':
    'location': "http://ftp.fr.debian.org/debian/"
    'release': "stretch"
    'repos': "main contrib non-free"
 
  'stretch-updates':
    'location': "http://ftp.fr.debian.org/debian/"
    'release': "stretch-updates"
    'repos': "main"
 
  'stretch-security':
    'location': "http://security.debian.org/"
    'release': "stretch/updates"
    'repos': "main"
#gitlab runner
  'runner_gitlab-ci-multi-runner':
    location: 'https://packages.gitlab.com/runner/gitlab-ci-multi-runner/debian/'
    release: 'stretch'
    repos: 'main'
    pin:
     packages: 'gitlab-runner'
     origin: 'packages.gitlab.com'
     explanation: 'Prefer GitLab provided packages over the Debian native ones'
     priority: 1001
    key:
      id: '1A4C919DB987D435939638B914219A96E15E78F4'
      source: 'https://packages.gitlab.com/runner/gitlab-ci-multi-runner/gpgkey'
```

{% include disqus.html %}