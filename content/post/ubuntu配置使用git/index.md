---
title: Ubuntu上配置使用git
description: 在Ubuntu上配置git，在命令行使用git
slug: git_ubuntu
date: 2023-12-25 20:59:00+0800
image: git.png
categories:
    - techStudy
tags:
    - Git
    - Github
    - Ubuntu

#weight: 1       # You can add weight to some posts to override the default sorting (date descending)
comments: true

#license: flase
#math: true
#toc: true
#style: 
#keywords:
#readingTime:
---

## 安装git

```bash
sudo apt-get update
sudo apt-get install git
```

## 配置git

```bash
git config --global user.name "Your Name"
git config --global user.email "Your Email"
```

## 配置ssh key

```bash
# 检查是否能访问github
ssh -T git@github.com
# Permission denied (publickey).说明可以访问，但是没有权限

cd ~/.ssh
ssh-keygen -t rsa -C "lihan3238@163.com"



# 查看公钥
cat ~/.ssh/id_rsa.pub

# 生成ssh key后，需要将公钥添加到github上

# 添加私钥到ssh-agent

#如果报错，则先执行： eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa

# 验证是否添加成功
ssh git@github.com

```

## 从github上clone仓库

```bash
git clone git@github.com:lihan3238/webDatabaseApp.git
```

## 创建仓库

```bash
# github上创建仓库 dockerfiles

# 在本地创建仓库
mkdir dockerfiles
cd dockerfiles
git init

# 添加文件
vim README.md

# 添加到暂存区
git add README.md

# 提交到仓库
git commit -m "first commit"

# 添加远程仓库
## 关联远程仓库
git remote add origin https://github.com/lihan3238/dockerfiles.git

## 推送到远程仓库
git push -u origin main

```

## 从远程仓库拉取

```bash
git pull origin main

```

