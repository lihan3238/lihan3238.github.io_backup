---
title: Ubuntu下安装包时缺少依赖的快速解决方法
slug: point_5
date: 2023-11-11 15:20:00+0800
image: apt.png
categories:
    - techStudy
tags:
    - linux
    - Ubuntu
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

在Ubuntu等Linux系统下，使用`apt`或`dpkg`安装包时，可能会出现缺少依赖的情况。

# 解决方案

使用`apt --fix-broken install`命令即可解决。