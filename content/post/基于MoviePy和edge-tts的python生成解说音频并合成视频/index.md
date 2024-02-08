---
title: 基于MoviePy和edge-tts的python生成解说音频并合成视频
description: Python+MoviePy合成视频，edge-tts生成解说音频
slug: moviePy
date: 2023-12-20 18:27:00+0800
image: moviepy.png
categories:
    - techStudy
tags:
    - python
    - Moviepy
    - edge-tts
    - media
#weight: 1       # You can add weight to some posts to override the default sorting (date descending)
comments: true

#license: flase
#math: true
#toc: true
#style: 
#keywords:
#readingTime:

---
# 代码介绍:

代码使用pipenv进行包管理
代码分为三部分:
1. dubbingVideo 用于从解说素材中生成音频 使用了edge-tts包
2. resize_images 用于将图片素材格式调整至一致 使用了PIL包
3. cideoCreate 用于将图片素材和音频合成为视频 使用了moviepy包


# 代码使用方法

将图片素材放在`1-图像素材`文件夹下，解说素材放在`2-解说素材`文件夹下，配乐素材放在`3-配乐素材`文件夹下，打开命令行进入主目录下，进行输入操作:

1. 确定python版本为 3.10
2. pip install pipenv
3. pipenv shell
4. pipenv install
5. python ./基于MoviePy的影视解说视频合成.py
