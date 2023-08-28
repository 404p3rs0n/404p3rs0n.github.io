# GZ::CTF平台搭建记录


## 准备工作

- 弃用了下载资源包内容，现在只需`docker-compose.yml`和`appsettings.json`文件即可
- 安装好docker和docker-compose

## 端口暴露范围

这里可设置也可以不设置，如果是云服务器的还是推荐设置，内网的话无所谓

```bash
sudo nano /etc/sysctl.conf
```

添加如下内容，指定 ip_local_port_range：

```bash
net.ipv4.ip_local_port_range = 20000 50000
```

执行 `sudo sysctl -p`使配置生效，重启Docker服务

## 搭建及配置记录

在同一个文件夹(GZCTF)下新建两个文件：`appsettings.json`和`docker-compose.yml`

### 配置appsettings.json文件

在appsettings.json文件内写入如下内容：

```javascript
{
  "AllowedHosts": "*",
  "ConnectionStrings": {
    "Database": "Host=db:5432;Database=gzctf;Username=postgres;Password=<String1>"
      //<String1>换成数据库密码，随机密码且长度足够
  },
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft": "Warning",
      "Microsoft.Hosting.Lifetime": "Information"
    }
  },
    //邮箱配置
  "EmailConfig": {
    "SendMailAddress": "Admin@xxx.com",		// 填入邮箱
    "UserName": "ctf_noreply",				// 发件人名称
    "Password": "UWPTINWMFPQVMPAH",			// 邮箱密码，部分服务商需要填入授权码
    "Smtp": {
      "Host": "smtp.163.com",				// 此处为163邮箱服务器，具体自定
      "Port": 465
    }
  },
  "XorKey": "<String2>",					// 自定XorKey
  "ContainerProvider": {
    "Type": "Docker",
    "PublicEntry": "xx.xx.xx.xx",			// 域名或IP配置，用于容器生成,域名不带http/https
    "DockerConfig": {
      "SwarmMode": false,
      "Uri": ""								// 本地配置Docker因此此处置空
    }
  },
  "RequestLogging": false,
  "DisableRateLimit": false,
  "RegistryConfig": {
    "UserName": "",
    "Password": "",
    "ServerAddress": ""
  },
    
    //谷歌验证码配置
  "GoogleRecaptcha": {
    "VerifyAPIAddress": "https://www.recaptcha.net/recaptcha/api/siteverify",
    "Sitekey": "",
    "Secretkey": "",
    "RecaptchaThreshold": "0.5"
  }
}
```

### 配置docker-compose.yml文件

```yaml
version: '3.0'
services:
  gzctf:
    image: gztime/gzctf:latest
    restart: always
    environment:
      - "GZCTF_ADMIN_PASSWORD=<String3>" # <String3>换成管理员账户密码，账号为Admin
    ports:
      - "80:80" # 对外端口号，前为外部端口。
    networks:
      default:
    volumes:
      - "./data/files:/app/uploads"
      - "./appsettings.json:/app/appsettings.json:ro"
      - "./logs:/app/log"
      - "./data/keys:/root/.aspnet/DataProtection-Keys"
      # - "./k8sconfig.yaml:/app/k8sconfig.yaml:ro"
      - "/var/run/docker.sock:/var/run/docker.sock"
    depends_on:
      - db

  db:
    image: postgres:alpine
    restart: always
    environment:
      - "POSTGRES_PASSWORD=<String1>" # 数据库密码，务必要和appsettings.json中的配置一致
    networks:
      default:
    volumes:
      - "./data/db:/var/lib/postgresql/data"

networks:
  default:
    driver: bridge
    ipam:
      config:
        - subnet: 192.168.12.0/24
```

### 部署及测试记录

将配置文件上传至服务器后，通过docker进行部署

```bash
cd GZCTF
docker-compose up -d
```

部署完成后查看Logs，看部署是否成功

> 主要是看GZCTF容器是否连接上了数据库

查看容器ID：

```bash
docker ps -a
```

这里可以看到GZCTF的ID，然后再通过如下命令查看日志

```bash
docker logs ID
```

看到连接上数据库的日志即可成功配置，接下来就可以对平台进行测试

> 登录域名或IP（域名需要在域名服务商配置），用Admin和前面设置的密码登录



## 报错及修改记录

### 将当前用户加入docker组

若出现如下报错需执行此过程

```bash
[xxxx@xxxx ~]$ docker ps
Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/containers/json": dial unix /var/run/docker.sock: connect: permission denied
```

问题出在用户为访问/var/run/docker.sock的权限，只需给用户增加权限即可。命令行输入：

```bash
sudo chown root:docker /var/run/docker.sock	# 修改docker.sock权限为root:docker
sudo groupadd docker          				# 添加docker用户组 
sudo gpasswd -a $USER docker  				# 将当前用户添加至docker用户组
newgrp docker                 				# 更新docker用户组
```

### 修改管理员密码

进入数据库容器内进行连接

```bash
# 这是连接命令
psql postgres://username:password@host:port/dbname
```

- username：连接数据的用户名，默认值是postgres
- password：密码，默认值是postgres
- host：主机名，默认值是localhost
- port：端口，默认值是5432
- dbname：要连接的数据库名，默认值是postgres

然后直接执行

```bash
UPDATE "AspNetUsers" SET "Role"=3 WHERE "UserName"='需要设置为管理员的用户名';
```


