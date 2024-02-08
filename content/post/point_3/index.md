---
title: gitpush失败问题2
description: gitpush出现失败报错2
slug: point_3
date: 2023-10-29 02:29:00+0800
image: git.png
categories:
    - techStudy
tags:
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

在使用命令行进行Git push的时候，发现无法push,出现报错。

```bash
`.git@github.com: Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

# 原因

git配置私钥出了问题

# 解决方案

## 检查`C:\Users\[用户名]\.ssh`目录下是否有github的公私钥及`config`文件是否配置正确：

- 私钥格式问题

私钥文件的格式必须是`id_rsa`，而不能是`id_rsa.ppk`，否则会出现报错。
```bash
invalid format
git@github.com: Permission denied (publickey).
```

解决：

```
    打开 PuTTY Key Generator（PuTTYgen）。

    在 PuTTYgen 中，点击 "Load" 按钮，并选择你的 PPK 格式的私钥文件。

    PuTTYgen 会提示你输入私钥文件的密码，如果设置了密码的话，请输入。

    密钥文件加载后，点击 "Conversions" 菜单，然后选择 "Export OpenSSH Key"。

    选择一个目标文件名和目录来保存转换后的 OpenSSH 格式的私钥。确保文件没有扩展名（例如，保存为 github_test_private）。

    保存私钥文件后，你就可以在 Git 中使用它了。
```

- `config`文件配置问题

```bash
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa
```

## 验证

```bash
 ssh -T git@github.com
```