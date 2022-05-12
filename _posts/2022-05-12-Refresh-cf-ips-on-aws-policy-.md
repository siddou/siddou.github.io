---
classes: wide
title:  "Refresh cloudflare IPs for an AWS iam policy"
tags:
  - aws
  - cloudflare
  - github
---
{% include toc %}


### Github action

#### main.yml
```shell
  cloudflare_ips:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          path: "main"
      - run: mkdir -p main/aws/cloudflare_ips
      - run: wget https://www.cloudflare.com/ips-v4 -O main/aws/cloudflare_ips/ips-v4
      - uses: EndBug/add-and-commit@v9
        with:
          message: 'Update cloudflare ips'
          add: '.'
          cwd: 'main'
```

### AWS Policy with terraform

#### variables.tf
```shell
locals {
  CF_IPS = split("\n", file("./cloudflare_ips/ips-v4"))
}
```

#### main.tf
```shell
data "aws_iam_policy_document" "bucket_policy_cf" {
  statement {
    sid = "PublicReadGetObject"
    principals {
      type        = "AWS"
      identifiers = ["*"]
    }
    effect = "Deny"
    actions = [
      "s3:GetObject",
    ]
    resources = [
      "${module.s3-bucket.s3_bucket_arn}/*",
    ]
    condition {
      test     = "NotIpAddress"
      variable = "aws:SourceIp"
      values   = local.CF_IPS
    }
  }
}
```