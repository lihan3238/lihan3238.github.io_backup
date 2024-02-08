---
title: cmd命令行扫描局域网在线ip
slug: LAN_ip_scan
date: 2024-01-12 01:20:00+0800
image: LAN.png
categories:
    - techStudy
tags:
    - computernetworksecurity
    - LAN
    - ip
    - Windows
#weight: 1       # You can add weight to some posts to override the default sorting (date descending)
comments: true

#license: flase
#math: true
#toc: true
#style: 
#keywords:
#readingTime:
---

# 引入

有时候需要知道局域网内有哪些设备在线，可以使用cmd命令行扫描局域网在线ip。
这在比如ssh连接舍友电脑时候可能有用哈哈。

# 步骤

1. 打开cmd命令行，输入`ipconfig`查看本机ip地址，如`192.168.31.*`，其中`*`为本机ip地址的最后一位。

根据这个知道大概的局域网范围

2. 扫描ip

```bash
for /L %i IN (1,1,254) DO ping -w 1 -n 1 192.168.31.%i #192.168.31.为本机ip地址前三位

```

等待扫描结束

3. 查看扫描结果

```bash
arp -a
```

# 注意

- 只能用`win+r`+`cmd`打开的命令行，否则会报错。