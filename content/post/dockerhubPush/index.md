---
title: 在Dockerhub上push镜像
description: 将本地制作的镜像push到Dockerhub上，以便联网用户下载使用
slug: DockerhubPush
date: 2023-11-15 08:15:00+0800
image: dockerhub.png
categories:
    - techStudy
tags:
    - docker
    - dockerhub
#weight: 1       # You can add weight to some posts to override the default sorting (date descending)
comments: true

#license: flase
#math: true
#toc: true
#style: 
#keywords:
#readingTime:
links:
  - title: Docker Hub
    description: Docker镜像仓库网站
    website: https://hub.docker.com/
    image: https://raw.githubusercontent.com/docker-library/docs/471fa6e4cb58062ccbf91afc111980f9c7004981/swarm/logo.png
---

## 1. 在dockerhub上创建一个repository

![1](1.png)

登录[dockerhub](https://hub.docker.com/)网站后，点击上图圈处创建新仓库。

## 2. 给本地镜像打上tag

```bash
# tag格式
docker tag <本地镜像名> <dockerhub用户名>/<仓库名>:<tag>
# 有一个名为`lihan_ndbmgm:1.0`的镜像
docker tag lihan_ndbmgm:1.0 lihan3238/mysql_ndb_cluster-ubuntu:lihan_ndbmgm`
```

- tips

此时本地出现两个tag指向同一个镜像，分别是原来的`lihan_ndbmgm:1.0`和新的`lihan3238/mysql_ndb_cluster-ubuntu:lihan_ndbmgm`。
使用`docker rmi`命令任意删除一个tag不会影响镜像的使用。

## 3. push镜像

```bash
# 命令行登录docker
docker login -u lalalalal --password-stdin balabala docker.io
# push镜像
docker push lihan3238/mysql_ndb_cluster-ubuntu:lihan_ndbmgm
```

```bash
