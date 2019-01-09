---
tags:
  - markdown
  - pandoc
  - linux
---

## Install Pandoc
```shell
sudo apt-get install pandoc
```

## Convert md to PDF
```shell
pandoc zimbra_ooo.markdown -V geometry:margin=1in -o /home/user/Desktop/zimbra_ooo.pdf
```

## if
```shell
pandoc: pdflatex not found. pdflatex is needed for pdf output.
```

```shell
apt-get -y --no-install-recommends install texlive-latex-base texlive-fonts-recommended texlive-latex-extra lmodern
```

{% include comments.html %}