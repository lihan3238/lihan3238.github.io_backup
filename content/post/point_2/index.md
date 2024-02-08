---
title: gitpush失败问题
description: gitpush偶尔出现失败报错
slug: point_2
date: 2023-10-15 22:29:00+0800
image: git.png
categories:
    - techStudy
tags:
    - TortoiseGit
    - Git
    - Github
    - SSH
    - point
#weight: 1       # You can add weight to some posts to override the default sorting (date descending)
comments: true

#license: flase
#math: true
#toc: true
#style: 
#keywords:
#readingTime:
---

# 问题

在使用TortoiseGit进行Git push的时候，发现无法push,出现报错。

![](1.png)

# 原因

不知道什么原因，TortoiseGit的Pageant出现了问题，丢失了私钥privateKey。

# 解决方案
打开Pageant，添加私钥privateKey，即可。

![](2.png)
![](3.png)
![](4.png)
