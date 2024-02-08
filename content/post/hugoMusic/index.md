---
title: hugo博客音乐组件
description: 给hugo博客添加音乐组件(Aplayer)
slug: hugoMusic
date: 2023-09-23 22:31:00+0800
image: Aplayer.png
categories:
    - techStudy
tags:
    - music
    - blog   
    - Hugo
#weight: 1       # You can add weight to some posts to override the default sorting (date descending)
comments: true
---
## 前言
本来在搭建了个人博客后觉得实用性更重要,几次准备学习如何装音乐组件又放弃了,但今天突然想到顺便妥善保存自己喜欢的音乐,就整了一个基于Aplayer和GitHub仓库的音乐组件,哈哈,github真成云盘了.
- 本文以Hugo|Stack主题为例

## 链接
- [Aplayer官方中文文档](https://aplayer.js.org/#/zh-Hans/)
- [基于github的自动化音乐仓库](https://github.com/lihan3238/music/)
## 博客导入Aplayer
1. music.html 
在博客仓库`\layouts\partials`(如果没有就新建)目录下新建`music.html`文件,复制以下代码(可根据[官网文档](https://aplayer.js.org/#/zh-Hans/)修改)
```html
<!DOCTYPE html>
<html>

<head>
    <!-- require APlayer -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/aplayer/dist/APlayer.min.css">
    <script src="https://cdn.jsdelivr.net/npm/aplayer/dist/APlayer.min.js"></script>
    <!-- require MetingJS -->
    <script src="https://cdn.jsdelivr.net/npm/meting@2.0.1/dist/Meting.min.js"></script>
</head>

<body>
    <div class="demo">
        <div id="player1">
        </div>
    </div>
    <script>
        var ap = new APlayer
            ({
                element: document.getElementById('player1'),
                fixed: true,
                autoplay: false,
                mini: true,
                theme: '#f8f4fc',
                loop: 'all',
                order: 'random',
                preload: 'auto',
                volume: 0.4,
                mutex: true,
                listFolded: true,
                listMaxHeight: '500px',
                lrcType: 0,
                music: [
                    {
                        name: 'name',
                        artist: 'artist',
                        url: 'url.mp3',
                        cover: 'cover.jpg'
                    }
                ]
            });
        //ap.init();
    </script>
</body>
```

2. custom.html
在博客仓库`\layouts\partials\footer\custom.html`文件中插入(新建)以下代码
```html
{{ partial "music" . }}
```

3. 配置
- 详见[官网文档](https://aplayer.js.org/#/zh-Hans/)
常见参数:

名称 | 默认值 | 描述
----|-------|----
container | document.querySelector('.aplayer') | 播放器容器元素
fixed | false | 开启吸底模式, [详情](https://aplayer.js.org/#/home?id=fixed-mode)
mini | false | 开启迷你模式, [详情](https://aplayer.js.org/#/home?id=mini-mode)
autoplay | false | 音频自动播放
theme | '#b7daff' | 主题色
loop | 'all' | 音频循环播放, 可选值: 'all', 'one', 'none'
order | 'list' | 音频循环顺序, 可选值: 'list', 'random'
preload | 'auto' | 预加载，可选值: 'none', 'metadata', 'auto'
volume | 0.7 | 默认音量，请注意播放器会记忆用户设置，用户手动设置音量后默认音量即失效
audio | - | 音频信息, 应该是一个对象或对象数组
audio.name | - | 音频名称
audio.artist | - | 音频艺术家
audio.url | - | 音频链接
audio.cover | - | 音频封面
audio.lrc | - | [详情](https://aplayer.js.org/#/home?id=lrc)
audio.theme | - | 切换到此音频时的主题色，比上面的 theme 优先级高
audio.type | 'auto' | 可选值: 'auto', 'hls', 'normal' 或其他自定义类型, [详情](https://aplayer.js.org/#/home?id=mse-support)
customAudioType | - | 自定义类型，[详情](https://aplayer.js.org/#/home?id=mse-support)
mutex | true | 互斥，阻止多个播放器同时播放，当前播放器播放时暂停其他播放器
lrcType | 0 | [详情](https://aplayer.js.org/#/home?id=lrc)
listFolded | false | 列表默认折叠
listMaxHeight | - | 列表最大高度
storageName | 'aplayer-setting' | 存储播放器设置的 localStorage key

## 基于Github仓库的音乐链接
由于播放器需要在线音乐链接,我选择了将音乐上传到GitHub仓库,然后获取链接,顺便还储存了自己喜欢的音乐.
可以浏览 [**基于github的自动化音乐仓库**](https://github.com/lihan3238/music/) ,学习如何上传音乐到GitHub仓库.
最方便的是这个仓库中直接将音乐生成了符合格式的代码,可以直接复制粘贴到`music.html`中的`music`参数中使用.


## 本博客参考了[山茶花舍-给 Hugo 加一点好玩的功能](https://irithys.com/p/%E7%BB%99hugo%E5%8A%A0%E4%B8%80%E7%82%B9%E5%A5%BD%E7%8E%A9%E7%9A%84%E5%8A%9F%E8%83%BD/)