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

![image.png](https://cdn.nlark.com/yuque/0/2023/png/27142791/1695169724517-7bb36836-0d86-4b1c-a292-8b3c96e94ffe.png#averageHue=%231f4d62&clientId=ua2a0a9ce-12c6-4&from=paste&height=206&id=u9107a077&originHeight=412&originWidth=1138&originalType=binary&ratio=2&rotation=0&showTitle=false&size=495760&status=done&style=none&taskId=uf9e861a7-19b3-4516-89cb-8b2e79d51bb&title=&width=569)

![image.png](https://cdn.nlark.com/yuque/0/2023/png/27142791/1695169750315-15f0bdc2-1d33-44c4-9d8d-fb23b8f58c84.png#averageHue=%231d485d&clientId=ua2a0a9ce-12c6-4&from=paste&height=286&id=udc44d7a7&originHeight=572&originWidth=1322&originalType=binary&ratio=2&rotation=0&showTitle=false&size=836170&status=done&style=none&taskId=uaa24ec84-14d7-49fa-829c-90ae84f80c3&title=&width=661)

### 修改配置文件

修改admin配置：

```
vim ./xxl-job/xxl-job-admin/src/main/resources/application.properties
```

![image.png](https://cdn.nlark.com/yuque/0/2023/png/27142791/1695170001301-e541f373-3839-4a22-8e90-9ce9a4eacc61.png#averageHue=%231a475b&clientId=ua2a0a9ce-12c6-4&from=paste&height=328&id=u4db20346&originHeight=656&originWidth=1470&originalType=binary&ratio=2&rotation=0&showTitle=false&size=1062297&status=done&style=none&taskId=u594a03a9-9de1-4f1e-99f6-f00508bcb1e&title=&width=735)

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

![image.png](https://cdn.nlark.com/yuque/0/2023/png/27142791/1695170200470-3bb9f208-2c73-44e4-9b39-8d43665f3f2b.png#averageHue=%231b465b&clientId=ua2a0a9ce-12c6-4&from=paste&height=333&id=ue19baae8&originHeight=666&originWidth=1488&originalType=binary&ratio=2&rotation=0&showTitle=false&size=1086256&status=done&style=none&taskId=u4b23f42d-f4bd-4edf-af2c-462ffa34baf&title=&width=744)

### 编译

```
mvn package
```

![image.png](https://cdn.nlark.com/yuque/0/2023/png/27142791/1695170331465-b607f2e7-7fec-441a-9c1e-dd9ced884587.png#averageHue=%231a3f51&clientId=ua2a0a9ce-12c6-4&from=paste&height=193&id=u1f1f85a3&originHeight=386&originWidth=1460&originalType=binary&ratio=2&rotation=0&showTitle=false&size=626865&status=done&style=none&taskId=u0b875ff2-7d24-43a9-a6aa-2e8cc5d0dbf&title=&width=730)

编译后生成 2 个 jar 包：

```
./xxl-job/xxl-job-admin/target/xxl-job-admin-2.4.1-SNAPSHOT.jar
```

![image.png](https://cdn.nlark.com/yuque/0/2023/png/27142791/1695172643399-98186994-9852-43f1-bc4d-fbef248f056c.png#averageHue=%231e4a61&clientId=u065c50c1-1b02-4&from=paste&height=55&id=u6edcb084&originHeight=110&originWidth=1374&originalType=binary&ratio=2&rotation=0&showTitle=false&size=176192&status=done&style=none&taskId=u51e58029-012e-473e-9e9a-72e7151c809&title=&width=687)

```
./xxl-job/xxl-job-executor-samples/xxl-job-executor-sample-springboot/target/xxl-job-executor-sample-springboot-2.4.1-SNAPSHOT.jar
```

![image.png](https://cdn.nlark.com/yuque/0/2023/png/27142791/1695172662686-8ce3273a-3105-4274-93ba-41cba9fe44d0.png#averageHue=%23153549&clientId=u065c50c1-1b02-4&from=paste&height=79&id=ub213ef92&originHeight=158&originWidth=1396&originalType=binary&ratio=2&rotation=0&showTitle=false&size=251136&status=done&style=none&taskId=uc286f0c3-6b56-4ab0-94eb-400ce7c0710&title=&width=698)

运行 jar 包：

```
nohup java -jar xxl-job-admin-2.4.1-SNAPSHOT.jar & &> /dev/null
```

![image.png](https://cdn.nlark.com/yuque/0/2023/png/27142791/1695173288905-da68643a-58f2-4d8a-be66-6186264dd667.png#averageHue=%23173749&clientId=u84ccbf91-5b59-4&from=paste&height=80&id=u6a84aca3&originHeight=160&originWidth=1324&originalType=binary&ratio=2&rotation=0&showTitle=false&size=256313&status=done&style=none&taskId=ueb120ea2-1848-483d-80c7-4f3afbc9839&title=&width=662)

```
nohup java -jar xxl-job-executor-sample-springboot-2.4.1-SNAPSHOT.jar & &> /dev/null
```

![image.png](https://cdn.nlark.com/yuque/0/2023/png/27142791/1695173305644-88166b71-3a74-42d8-b57c-fba3f97bfa44.png#averageHue=%23163648&clientId=u84ccbf91-5b59-4&from=paste&height=93&id=u1203748f&originHeight=186&originWidth=1432&originalType=binary&ratio=2&rotation=0&showTitle=false&size=321846&status=done&style=none&taskId=u403436dc-b4b7-453c-b505-17ae6e4b17b&title=&width=716)

### 测试验证

浏览器输入：[http://localhost:ServerPort/xxl-job-admin](http://192.168.1.38:9001/xxl-job-admin)
默认登录账号为“admin/123456”：

![image.png](https://cdn.nlark.com/yuque/0/2023/png/27142791/1695173277140-4ff1206a-eab2-401d-9022-9c390a2d5e92.png#averageHue=%23e6ece5&clientId=u84ccbf91-5b59-4&from=paste&height=663&id=u7a77a004&originHeight=1326&originWidth=2582&originalType=binary&ratio=2&rotation=0&showTitle=false&size=173190&status=done&style=none&taskId=ua64a2baf-7b42-4db3-95bf-6973d5155d0&title=&width=1291)



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

![image.png](https://cdn.nlark.com/yuque/0/2023/png/27142791/1695177611911-c353e3ae-4609-4d84-8a8a-da266d5fa208.png#averageHue=%23193d4f&clientId=u84ccbf91-5b59-4&from=paste&height=189&id=u3b77b60b&originHeight=378&originWidth=1476&originalType=binary&ratio=2&rotation=0&showTitle=false&size=638900&status=done&style=none&taskId=u72e4007c-3a61-4dc9-a96b-71ae96e1949&title=&width=738)

添加执行器

![image.png](https://cdn.nlark.com/yuque/0/2023/png/27142791/1695180202317-9c5687d1-cb63-4a53-b57a-0afaf8caf5b5.png#averageHue=%23915f15&clientId=u84ccbf91-5b59-4&from=paste&height=434&id=u5ede74fb&originHeight=868&originWidth=1888&originalType=binary&ratio=2&rotation=0&showTitle=false&size=122844&status=done&style=none&taskId=u97af143d-6350-4a30-9ffd-919f6d813b0&title=&width=944)





