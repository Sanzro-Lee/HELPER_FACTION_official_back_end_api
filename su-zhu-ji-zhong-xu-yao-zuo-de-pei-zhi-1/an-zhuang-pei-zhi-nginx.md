---
description: Nginx配置
---

# 安装 & 配置 Nginx

大部分内容出自此链接🔗：[https://juejin.im/post/6844904134345228301](https://juejin.im/post/6844904134345228301)

```bash
# 安装 Nginx
yum -y install nginx

# 卸载 Nginx
yum remove nginx

# 设置开机启动，建议打开
systemctl enable nginx

# 启动 nginx 服务，安装后需运行
systemcrl start nginx

# 停止 nginx 服务
systemcrl stop nginx

# 重启 nginx 服务
systemcrl restart nginx
```

我我的 Nginx 配置，以下仅为部分配置，可下载一键脚本进行配置。

```text
# 编辑的文件
# vi /etc/nginx/nginx.conf.default

server {
    listen       80;
    server_name  www.xxx.xxx;
    rewrite ^(.*)$  https://$host$1 permanent;
}
server {
    listen 443 ssl http2;
    server_name www.xxx.xxx;
    root /etc/nginx/html;
    index index.php index.html;
    location / {
       try_files $uri $uri/ /index.php?$args;
    }
    # fastapi main
    location /helloworld {
       proxy_pass http://127.0.0.1:8011;
    }
    # fastapi docs
    location /docs {
       proxy_pass http://127.0.0.1:8011/api/docs;
    }
}
```



