---
title: "Mac下WX小程序包记录"
date: 2023-09-05T13:10:09+08:00
slug: f0333baedce38442
draft: false
---

> 在写这篇之前，尝试过利用fildder、charles、手机进行证书配置等工具或方法进行流量转发均以失败告终，不知道是不是Mac的原因还是因为WX的接口策略发生了改变导致抓到的数据包都是乱码，无法进一步利用。本文尝试利用Proxyman进行测试。

## 工具介绍

> Proxyman是一个原生的高性能macOS端的抓包工具，它使开发或测试人员能够轻松地捕获、检查和操作HTTP或HTTPS请求/响应。

```bash
下载地址：https://proxyman.io
官方文档：https://docs.proxyman.io
```

![image-20230905132020052](https://21r000-image.oss-cn-shanghai.aliyuncs.com/2023/image-20230905132020052.png)

![image-20230905133458184](https://21r000-image.oss-cn-shanghai.aliyuncs.com/2023/image-20230905133458184.png)

## 配置代理

这里记录配置代理转发利用BP进行抓包测试

![image-20230905132349482](https://21r000-image.oss-cn-shanghai.aliyuncs.com/2023/image-20230905132349482.png)

配置相关代理信息需要和BP的代理信息一致

![image-20230905132440425](https://21r000-image.oss-cn-shanghai.aliyuncs.com/2023/image-20230905132440425.png)

![image-20230905132527776](https://21r000-image.oss-cn-shanghai.aliyuncs.com/2023/image-20230905132527776.png)

## Proxyman请求转代码

算了，结束了，同样存在抓不到数据包情况

