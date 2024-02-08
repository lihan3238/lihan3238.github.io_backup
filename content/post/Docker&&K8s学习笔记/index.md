---
title: Docker&&K8s学习笔记
description: 学习Docker和K8s的笔记(ubuntu)
slug: dockerStudy
date: 2023-10-03 15:41:00+0800
image: docker.png
categories:
    - techStudy
tags:
    - docker   
    - Ubuntu
    - liunx
    - k8s
#weight: 1       # You can add weight to some posts to override the default sorting (date descending)
comments: true

---
# Docker&&K8s学习笔记

## Docker
- [官网](https://hub.docker.com)
- [官方文档](https://docs.docker.com)

### Docker安装（Ubuntu22.04.3）

- 不同平台有差异，建议百度

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo service docker start
```


#### 1. 卸载旧版本

```shell
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

#### 2. 安装依赖并添加GPG密钥


```shell
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
```

#### 3. 添加Docker软件源仓库

```shell
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

#### 4. 安装Docker Engine

```shell
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
# 验证安装
sudo docker run hello-world
```

#### 5. 卸载Docker Engine

```shell
#卸载软件包
sudo apt-get purge docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin docker-ce-rootless-extras
#删除所有镜像、容器和卷
sudo rm -rf /var/lib/docker
sudo rm -rf /var/lib/containerd
```

#### 6. 设置ustc镜像源

```shell
#在/etc/docker/daemon.json中写入
{
  "registry-mirrors": ["https://docker.mirrors.ustc.edu.cn"]
}
```

### Docker常用命令

- `docker --help`：查看docker帮助

#### 1. 启动docker服务

```shell
#启动docker服务
sudo systemctl start docker
#查看docker服务状态
sudo systemctl status docker
#停止docker服务
sudo systemctl stop docker
#重启docker服务
sudo systemctl restart docker
#开机自启动docker服务
sudo systemctl enable docker
```

#### 2. 镜像相关

##### 2.1 查看镜像
  
```shell
docker images

#REPOSITORY : 镜像名称
#TAG ：镜像标签
#IMAGE ID ：镜像ID
#CREATED ：镜像创建时间
#SIZE ： 镜像大小
```
![](1.png)

##### 2.2 搜索镜像

```shell
docker search [镜像名称]

#NAME ：镜像名称
#DESCRIPTION ：镜像描述
#STARS ：镜像评价
#OFFICIAL ：是否官方
#AUTOMATED ：是否自动构建，表示该镜像由DockerHub自动构建流程创建的
```
![](2.png)

##### 2.3 拉取镜像

```shell
docker pull [镜像名称]:[标签]
#不加标签时，默认拉取latest标签
```
![](3.png)

##### 2.4 删除镜像

```shell
docker rmi [镜像ID]
#删除镜像时，要求该镜像没有被容器使用

#删除所有镜像
docker rmi `docker images -q`

```

#### 3. 容器相关

##### 3.1 查看容器

```shell
#查看正在运行中的容器
docker ps

#查看停止的容器
docker ps -f status=exited

#查看所有容器
docker ps -a

#查看最近一次创建的容器
docker ps -l
```

##### 3.2 创建与启动容器

```shell
docker run

#参数说明
#-i ：以交互模式运行容器，通常与 -t 同时使用；
#-t ：启动后进入其命令行，即为容器重新分配一个伪输入终端，通常与 -i 同时使用；
#--name ：为容器指定一个名称；
#-v ：将本地目录挂载到容器中，前一个是宿主机目录，后一个是容器内部的挂载点；
#-d ：后台运行守护式容器，创建容器后不会自动登陆容器。
#-p ：指定端口映射，前一个是宿主机端口，后一个是容器内部的映射端口，可用多个-p做多个端口映射。
```

(1) 交互式方式创建容器

```shell
docker run -it --name=[容器名称] [镜像名称]:[标签] /bin/bash
#创建即登录，退出即关闭
```

(2) 守护式方式创建容器
```shell
docker run -di --name=[容器名称] [镜像名称]:[标签] /bin/bash
#创建不登陆，退出不关闭

#登录容器
docker exec -it [容器名称] /bin/bash

```

##### 3.3 启动与停止容器

```shell
docker start [容器名称]
docker stop [容器名称]
```

##### 3.4 文件拷贝

```shell
#从容器拷贝到主机
docker cp [容器名称]:[容器内路径] [主机路径]
#从主机拷贝到容器
docker cp [主机路径] [容器名称]:[容器内路径]
```

##### 3.5 目录挂载
- 目录挂载是将主机的目录挂载到容器中，容器中的文件会实时同步到主机中，主机中的文件也会实时同步到容器中(共享文件夹)

```shell
docker run -di --name=[容器名称] -v [主机目录]:[容器内目录] [镜像名称]:[标签] 
#似乎docker目录只能写相对路径，不能写绝对路径
```
##### 3.6 查看容器ip

```shell

#查看容器全部信息
docker inspect [容器名称]

#查看容器ip
docker inspect --format='{{.NetworkSettings.IPAddress}}' [容器名称]

```

##### 3.7 删除容器

```shell  
docker rm [容器名称]
#删除所有容器
docker rm `docker ps -a -q`
```

##### 3.8 容器日志

```shell
docker logs --help
docker logs -tf <--tail [显示数量]> [容器名称]

#示例
docker run -di --name=lihan_ubuntu ubuntu:22.04 /bin/sh -c "while true; do echo hello world; sleep 1; done"

docker logs -tf --tail 10 lihan_ubuntu

```
![](9.png)

#### 3.9 查看容器中进程信息 ps
  
```shell
docker top [容器名称]
```

#### 3.10 查看容器中元数据

```shell
docker inspect [容器名称]
```

#### 4. 应用部署

##### 4.1 MySQL

```shell
#拉取镜像
docker pull mysql:5.7

#创建容器
docker run -di --name=lihan_mysql -p 33306:3306  -e MYSQL_ROOT_PASSWORD=lihan mysql:5.7
```
- 使用`MySQL Workbench`连接数据库
- 用127.0.0.1连不上，突然想起来我用的是虚拟机。。。
![](4.png)
- 导入[sql文件](test.sql)
![](5.png)

##### 4.2 Tomcat

```shell
#拉取镜像
docker pull tomcat:7-jre7

#创建容器
docker run -di --name=lihan_tomcat -p 18080:8080 -v /usr/local/webapps:/usr/local/tomcat/webapps tomcat:7-jre7
```
将[sample.war](sample.war)放在docker宿主机的`/usr/local/webapps`目录下，访问`http://localhost:18080/sample`即可测试
![](6.png)

##### 4.3 Nginx

```shell
#拉取镜像
docker pull nginx

#创建容器
docker run -di --name=lihan_nginx -p 180:80 nginx
```
[testweb](./testweb/)目录复制到docker中
` docker exec -it lihan_nginx /bin/bash`进入容器,进入`:/etc/nginx/conf.d`目录，查看`default.conf`文件，根据`root   /usr/share/nginx/html;`,将`testweb`目录中的文件复制到`/usr/share/nginx/html`目录下，访问`http//localhost:180`即可测试
![](7.png)

##### 4.4 Redis部署
  
```shell
#拉取镜像
docker pull redis

#创建容器
docker run -di --name=lihan_redis -p 6379:6379 redis
```
略，没学过，先不测试了

#### 5.迁移与备份

##### 5.1 容器保存为镜像
  
```shell
docker commit [容器名称] [镜像名称]:[标签]

#查看镜像
docker images
```

##### 5.2 镜像保存为文件(.tar)

```shell
docker save -o [文件名].tar [镜像名称]:[标签]
```

##### 5.3 文件(.tar)导入为镜像

```shell
docker load -i [文件名].tar
```

#### 6. Dockerfile

##### 6.1 Dockerfile介绍

Dockerfile是由一系列命令和参数构成的脚本，这些命令应用于基础镜像并最终创建一个新的镜像
- 对于开发人员:可以为开发团队提供一个完全一致的开发环境;
- 对于测试人员:可以直接拿开发时所构建的镜像或者通过Dockerfile文件构建一个新的镜像开始工作
- 对于运维人员:在部署时，可以实现应用的无缝移植。

##### 6.2 Dockerfile指令
```shell
#指定基础镜像
FROM [镜像名称]:[标签]

#维护者信息
MAINTAINER [维护者姓名]

#设置环境变量
ENV [key] [value]

#镜像操作指令
RUN [shell命令] 

#拷贝文件
COPY [源路径] [目标路径]

#COPY并解压压缩包
ADD [源路径] [目标路径]

#设置工作目录
WORKDIR [工作目录]

#设置容器启动时执行的命令
ENTRYPOINT [shell命令]

```

##### 6.3 Dockerfile构建镜像


- jdk8镜像构建为例 

- [jdk-8u371-linux-x64.tar.gz](https://www.oracle.com/sg/java/technologies/javase/javase8u211-later-archive-downloads.html#license-lightbox)

```shell Dockerfile
# 将jdk-8u371-linux-x64.tar.gz放在宿主机的/usr/local/dockerjdk目录下
# 创建`Dockerfile`文件
FROM ubuntu:18.04
MAINTAINER lihan
RUN mkdir /usr/local/java
ADD jdk-8u371-linux-x64.tar.gz /usr/local/java/
# jdk-8u371-linux-x64.tar.gz 解压后为 jdk1.8.0_371
ENV JAVA_HOME /usr/local/java/jdk1.8.0_371
ENV JRE_HOME $JAVA_HOME/jre
ENV CLASSPATH $JAVA_HOME/bin/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib:$CLASSPATH
ENV PATH $JAVA_HOME/bin:$PATH
``` 

```shell
# 构建镜像
# . 表示当前目录下的Dockerfile文件
docker build -t lihanjdk1.8 .
```

#### 7. Docker私有仓库

##### 7.1 搭建与配置私有仓库

```shell
# 拉取私有仓库镜像
docker pull registry

# 创建私有仓库容器
docker run -di --name=lihan_registry -p 5000:5000 registry

# 打开浏览器，访问http://<ip>:5000/v2/_catalog，看到`{"repositories":[]}`表示私有仓库搭建成功

# 修改docker配置文件，添加私有仓库地址，使本地可以上传镜像到私有仓库
在`/etc/docker/daemon.json`中添加
{
  "insecure-registries": ["<ip>:5000"]
}
# 重启服务
systemctl restart docker
```

##### 7.2 上传和下载镜像到私有仓库

```shell
# tag镜像,为镜像创建一个新的标签
docker tag [镜像名称]:[标签] [私有仓库地址]/[镜像名称]:[标签]

# 上传镜像，确保registry是运行的
docker start [registry镜像容器名]
docker push [私有仓库地址]/[镜像名称]:[标签]

# 下载镜像
docker pull [私有仓库地址]/[镜像名称]:[标签]
```
![](8.1.png)
![](8.2.png)

### Docker网络(Docker0)

- [Docker网络详解](https://blog.csdn.net/meser88/article/details/131190900)

- 查看容器IP：
- `docker inspect --format='{{.NetworkSettings.IPAddress}}' [容器名称]`
- `docker inspect [容器名称] | grep IPAddress`
#### 实现原理

Docker在安装时会创建一个名为docker0的虚拟网桥，当创建一个容器时，会为其分配一个IP地址，称为Container-IP，同时将容器加入到docker0网桥中，这样容器就可以和docker0网桥中的其他容器通信，也可以和宿主机通信，从而实现容器之间的通信。

#### 四种网络模式

当你安装Docker时，它会自动创建三个网络。bridge（创建容器默认连接到此网络）、 none 、host。你可以使用以下`docker network ls`命令列出这些网络:

![](10.png)

bridge网络代表docker0，所有Docker安装中存在的网络。除非你使用`docker run --network=`选项指定，否则Docker守护程序默认将容器连接到此网络

使用`docker run`创建Docker容器时，可以用` --net `选项指定容器的网络模式，Docker可以有以下4种网络模式：

- `host模式`：使用` --net=host `指定。
- `none模式`：使用` --net=none `指定。
- `bridge模式`：使用` --net=bridge `指定，默认设置。
- `container模式`：使用` --net=container:NAME_or_ID `指定

|Docker网络模式|配置|说明|
|:---|:---|:---|
|host模式|`--net=host`|容器和宿主机共享Network namespace。容器将不会虚拟出自己的网卡，配置自己的IP等，而是使用宿主机的IP和端口。|
|container模式|`--net=container:NAME_or_ID`|容器和另外一个容器共享Network namespace。创建的容器不会创建自己的网卡，配置自己的IP，而是和一个指定的容器共享IP、端口范围|
|bridge模式|`--net=bridge`| **默认为该模式** 此模式会为每一个容器分配、设置IP等，并将容器连接到一个docker0虚拟网桥，通过docker0网桥以及Iptables nat表配置与宿主机通信。|
|none模式|`--net=none`|容器使用自己的网络，容器与主机不共享网络，容器之间不能互相通信| 

1. host模式

使用host模式，那么这个容器将不会获得一个独立的Network Namespace，而是和宿主机共用一个Network Namespace。容器将不会虚拟出自己的网卡，配置自己的IP等，而是使用宿主机的IP和端口。但是，容器的其他方面，如文件系统、进程列表等还是和宿主机隔离的。

使用host模式的容器可以直接使用宿主机的IP地址与外界通信，容器内部的服务端口也可以使用宿主机的端口，不需要进行NAT，host最大的优势就是网络性能比较好，但是docker host上已经使用的端口就不能再用了，网络的隔离性不好。

![](11.png)

2. container模式

指定新创建的容器和已经存在的一个容器共享一个 Network Namespace，而不是和宿主机共享。新创建的容器不会创建自己的网卡，配置自己的 IP，而是和一个指定的容器共享 IP、端口范围等。同样，两个容器除了网络方面，其他的如文件系统、进程列表等还是隔离的。两个容器的进程可以通过 lo 网卡设备通信。

![12](12.png)

3. none模式

Docker容器拥有自己的Network Namespace，但是，并不为Docker容器进行任何网络配置。也就是说，这个Docker容器没有网卡、IP、路由等信息。需要我们自己为Docker容器添加网卡、配置IP等。

这种网络模式下容器只有lo回环网络，没有其他网卡。none模式可以在容器创建时通过--network=none来指定。这种类型的网络没有办法联网，封闭的网络能很好的保证容器的安全性。

![13](13.png)

4. bridge模式

当Docker进程启动时，会在主机上创建一个名为docker0的虚拟网桥，此主机上启动的Docker容器会连接到这个虚拟网桥上。虚拟网桥的工作方式和物理交换机类似，这样主机上的所有容器就通过交换机连在了一个二层网络中。

从docker0子网中分配一个IP给容器使用，并设置docker0的IP地址为容器的默认网关。在主机上创建一对虚拟网卡veth pair设备，Docker将veth pair设备的一端放在新创建的容器中，并命名为eth0（容器的网卡），另一端放在主机中，以vethxxx这样类似的名字命名，并将这个网络设备加入到docker0网桥中。可以通过brctl show命令查看。

bridge模式是docker的默认网络模式，不写--net参数，就是bridge模式。使用docker run -p时，docker实际是在iptables做了DNAT规则，实现端口转发功能。可以使用iptables -t nat -vnL查看。

![14](14.png)

#### 自定义网络

建议使用自定义的网桥来控制哪些容器可以相互通信，还可以自动DNS解析容器名称到IP地址。你可以根据需要创建任意数量的网络，并且可以在任何给定时间将容器连接到这些网络中的零或多个网络。当容器连接到多个网络时，其外部连接通过第一个非内部网络以词法顺序提供。

1. 自定义bridge网络

```shell
# 创建自定义bridge网络 my_bridge
docker network create --driver bridge --subnet 192.168.0.0/16 --gateway 192.168.0.1 my_bridge

# 使用自定义网络创建容器并指定ip

docker run -di --name=lihan_tomcat -p 18080:8080 -v /usr/local/webapps:/usr/local/tomcat/webapps --net my_bridge --ip 192.168.0.2 tomcat:7-jre7

# 查看自定义网络
docker network inspect my_bridge

# docker0和自定义网络之间网络不通

```

2. Macvlan

Macvlan是一个新的尝试，是真正的网络虚拟化技术的转折点。Linux实现非常轻量级，因为与传统的Linux Bridge隔离相比，它们只是简单地与一个Linux以太网接口或子接口相关联，以实现网络之间的分离和与物理网络的连接。

Macvlan提供了许多独特的功能，并有充足的空间进一步创新与各种模式。这些方法的两个高级优点是绕过Linux网桥的正面性能以及移动部件少的简单性。删除传统上驻留在Docker主机NIC和容器接口之间的网桥留下了一个非常简单的设置，包括容器接口，直接连接到Docker主机接口。由于在这些情况下没有端口映射，因此可以轻松访问外部服务。

3. overlay网络

overlay网络用于连接不同机器上的docker容器，允许不同机器上的容器相互通信，同时支持对消息进行加密，当我们初始化一个swarm或是加入到一个swarm中时，在docker主机上会出现两种网络：
![](15.png)

1、称为ingress的overlay网络，用于传递集群服务的控制或是数据消息，若在创建swarm服务时没有指定连接用户自定义的overlay网络，将会加入到默认的ingress网络

2、名为docker_gwbridge桥接网络会连接swarm中所有独立的docker系统进程

可以使用docker network create创建自定义的overlay网络，容器以及服务可以加入多个网络，只有同一网络中的容器可以相互交换信息，可以将单一容器或是swarm服务连接到overlay网络中，但是两者在overlay网络中的行为会有所不同.





## Kubernetes(K8s)

- 
- 

### Kubernetes安装













