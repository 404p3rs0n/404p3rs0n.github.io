---
title: "在Linux系统上部署xll Job分布式任务调度平台"
date: 2023-09-21T16:17:27+08:00
slug: 3815816a4666463c
draft: false
---

## 概述

XXL-JOB是一个分布式任务调度平台，其核心设计目标是开发迅速、学习简单、轻量级、易扩展。

## 下载

#### 文档地址

- [中文文档](https://www.xuxueli.com/xxl-job/)
- [English Documentation](https://www.xuxueli.com/xxl-job/en/)

#### 源码仓库地址

| **源码仓库地址**                                             | **Release Download**                                      |
| ------------------------------------------------------------ | --------------------------------------------------------- |
| [https://github.com/xuxueli/xxl-job](https://github.com/xuxueli/xxl-job) | [Download](https://github.com/xuxueli/xxl-job/releases)   |
| [http://gitee.com/xuxueli0323/xxl-job](http://gitee.com/xuxueli0323/xxl-job) | [Download](http://gitee.com/xuxueli0323/xxl-job/releases) |


## 安装环境

- Maven3+
- Jdk1.8+
- Mysql5.7+

### 安装 Maven

```
yum -y install maven
mvn -v
```

### 安装 JDK 1.8+

```
yum install java-1.8.0-openjdk* -y
java -version
```

## 安装部署

### 导入数据

将/xxl-job/doc/db/tables_xxl_job.sql导入MySQL数据库：

```
 mysql -uroot -p < tables_xxl_job.sql 
```

![image-20230921162900868](https://21r000-image.oss-cn-shanghai.aliyuncs.com/2023/image-20230921162900868.png)

![image-20230921162909760](https://21r000-image.oss-cn-shanghai.aliyuncs.com/2023/image-20230921162909760.png)

### 修改配置文件

修改admin配置：

```
vim ./xxl-job/xxl-job-admin/src/main/resources/application.properties
```

![image-20230921162919134](https://21r000-image.oss-cn-shanghai.aliyuncs.com/2023/image-20230921162919134.png)

可修改服务端口：

```
server.port=8849
```

修改数据库连接信息：

```
### xxl-job, datasource
spring.datasource.url=jdbc:mysql://127.0.0.1:3306/xxl_job?useUnicode=true&characterEncoding=UTF-8&autoReconnect=true&serverTimezone=Asia/Shanghai
spring.datasource.username=root
spring.datasource.password=xxxxxx
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
```

修改执行器配置：

```
vim ./xxl-job/xxl-job-executor-samples/xxl-job-executor-sample-springboot/src/main/resources/application.properties
```

可修改服务端口

```
server.port=8848
```

配置admin链接：

```
### xxl-job admin address list, such as "http://address" or "http://address01,http://address02"
xxl.job.admin.addresses=http://127.0.0.1:8849/xxl-job-admin
```

![image-20230921162927938](https://21r000-image.oss-cn-shanghai.aliyuncs.com/2023/image-20230921162927938.png)

### 编译

```
mvn package
```

![image-20230921162935888](https://21r000-image.oss-cn-shanghai.aliyuncs.com/2023/image-20230921162935888.png)

编译后生成 2 个 jar 包：

```
./xxl-job/xxl-job-admin/target/xxl-job-admin-2.4.1-SNAPSHOT.jar
```

![image-20230921162943291](https://21r000-image.oss-cn-shanghai.aliyuncs.com/2023/image-20230921162943291.png)

```
./xxl-job/xxl-job-executor-samples/xxl-job-executor-sample-springboot/target/xxl-job-executor-sample-springboot-2.4.1-SNAPSHOT.jar
```

![image-20230921162950192](https://21r000-image.oss-cn-shanghai.aliyuncs.com/2023/image-20230921162950192.png)

运行 jar 包：

```
nohup java -jar xxl-job-admin-2.4.1-SNAPSHOT.jar & &> /dev/null
```

![image-20230921162956428](https://21r000-image.oss-cn-shanghai.aliyuncs.com/2023/image-20230921162956428.png)

```
nohup java -jar xxl-job-executor-sample-springboot-2.4.1-SNAPSHOT.jar & &> /dev/null
```

![image-20230921163004674](https://21r000-image.oss-cn-shanghai.aliyuncs.com/2023/image-20230921163004674.png)

### 测试验证

浏览器输入：[http://localhost:ServerPort/xxl-job-admin](http://192.168.1.38:9001/xxl-job-admin)
默认登录账号为“admin/123456”：

![image-20230921163012292](https://21r000-image.oss-cn-shanghai.aliyuncs.com/2023/image-20230921163012292.png)



## Python执行器添加

下载执行器文件：

```
git clone https://github.com/skyfyl/xxl-job-executor-sample-springboot.git
```

修改admin配置地址后，docker部署：

```bash
# 本地编译docker容器或docker pull kobedocker24/xxl-job-executor-sample-springboot
docker build -t xxl-job-executor-sample-springboot:2.2.0 .
docker run -p 8401:8401 -p 8889:8889 -v /root/xxl-job/xxl-job-executor-sample-springboot-master/application.properties:/application.properties --name xxl-job-executor-sample-springboot -d xxl-job-executor-sample-springboot:2.2.0
```

![image-20230921163019690](https://21r000-image.oss-cn-shanghai.aliyuncs.com/2023/image-20230921163019690.png)

添加执行器

![image-20230921163026363](https://21r000-image.oss-cn-shanghai.aliyuncs.com/2023/image-20230921163026363.png)





