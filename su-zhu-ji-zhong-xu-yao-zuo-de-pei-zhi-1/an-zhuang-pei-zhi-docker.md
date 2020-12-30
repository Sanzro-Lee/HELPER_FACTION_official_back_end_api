---
description: Docker 容器配置
---

# 安装 & 配置 Docker

### 2. 安装 & 配置 `Docker`

```bash
# 安装 Docker
yum -y install docker

# 启动 Docker 后台服务，安装完后需运行
systemctl start docker

# 开机自启动 Dokcer，建议开启
systemctl enable docker

# 查看 Dokcer 运行信息
systemctl status docker

# 重启 Docker 服务
systemctl restart docker

# 检测 Docker 是否正常安装，尝试跑一个叫 hello-word 的镜像
docker run hello-world

# 查看是存在 hello-world 镜像，如果存在，则成功
docker images

# 拉取 CentOS 镜像，注意':'后面带的是系统版本，
# 同样的 docker images 可以查看是否存在 centos 这个镜像
docker pull centos:7.2.1511

# 运行 docker centos 的时候，
# 一定要注意开放端口，以方便容器内的 Fastapi 使用
docker run -ti -d -p 80:80 -p 8011:8011 --privileged=true centos:7.8.2003 /usr/sbin/init

# 查看所有镜像的信息，方便使用 container id 进入
docker ps -a

# 先执行 attach 命令，以获得 systemctl 权限
docker attach docker_container_id

# 下次进入 docker 就不是上面那句 attach 命令了，而是
docker exec -it docker_container_id /bin/bash
# 所以需要 docker ps -a 查看 container id
```

**!重要!：之后进入这个容器就不能用 `docker attach docker_container_id` 了，但为了保险，先 `attach` 一次，以获得容器内 `CentOS 7` 执行 `systemctl` 命令的权限**

```bash
# 然后关掉终端或命令行，开启新的终端或命令行，这次换另外一条命令进入 虚拟机
docker exec -it docker_container_id /bin/bash
```

关于 CentOS 7 安装 Docker 更详细的信息：[https://www.jianshu.com/p/3a4cd73e3272](https://www.jianshu.com/p/3a4cd73e3272)

关于 Docker 安装 CentOS 7 及基本配置：[https://victorzhong.github.io/2018/01/15/Docker%E5%AE%89%E8%A3%85CentOS7%E5%8F%8A%E5%9F%BA%E6%9C%AC%E9%85%8D%E7%BD%AE/](https://victorzhong.github.io/2018/01/15/Docker%E5%AE%89%E8%A3%85CentOS7%E5%8F%8A%E5%9F%BA%E6%9C%AC%E9%85%8D%E7%BD%AE/)

