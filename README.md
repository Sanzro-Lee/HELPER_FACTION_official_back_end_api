<p align="center">
    <a href="#">
        <img alt="叫到帮" src="https://raw.githubusercontent.com/Sanzro-Lee/HELPER_FACTION_official_background_management_system/master/images/%E5%8F%AB%E5%88%B0%E5%B8%AE_logo.png" width="300">
    </a>
</p>

<p align="center">
    叫到帮官方后端接口系统，使用了 CentOS + Docker + Nginx + Anaconda + Fastapi + PostgreSQL，RESTful API 所有前端皆可访问。<br>
    环境配置：https://sanzrolee.gitbook.io/helper-faction-apis/<br>
    内网可访问（配置）：https://juejin.im/post/6884113599644729351/
</p>

<!-- <p align="center">
    <img alt="brage" src="https://img.shields.io/github/issues/Sanzro-Lee/HELPER_FACTION_official_background_management_system" width="auto">
    <img alt="brage" src="https://img.shields.io/github/forks/Sanzro-Lee/HELPER_FACTION_official_background_management_system" width="auto">
    <img alt="brage" src="https://img.shields.io/github/stars/Sanzro-Lee/HELPER_FACTION_official_background_management_system" width="auto">
    <img alt="brage" src="https://img.shields.io/github/license/Sanzro-Lee/HELPER_FACTION_official_background_management_system" width="auto">
</p> -->

## 简介

叫到帮小程序就是帮助大家解决 🧰 各种问题的，其中包括室内装修、电器维修、货物搬迁等问题，有这些问题就找叫到帮！（此项目暂未完成 ❎ ）

此项目为所有前端配套的后端接口系统，作为内部员工使用，当数据上的内容出错时，可使用此系统修改部分数据，以及时修正。


## 运行使用

```bash
# 如果已经按照上面👆 环境配置链接🔗 配置好，则可以运行下面👇 的命令
# 如果不想配置那么麻烦，安装完 Python > 3.7 & PostgreSQL 12 后
# 直接 pip install fastapi uvicorn psycopg2，就可以运行下面👇 的命令了

# 服务启动: 
uvicorn main:app --reload

# 服务器 Dokcer 容器内启动：
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

# 服务器上的路径是：先进入 Docker 容器，再去 /tmp/ 就能找到 HELPER_FACTION_official_back_end_api
```

## 实际演示图

<img alt="实机演示图" src="https://raw.githubusercontent.com/Sanzro-Lee/HELPER_FACTION_official_website/master/images/Background%20Management%20System%20Demo.png" width="auto">

<!-- ## 文档
https://helperfaction.github.io/docs -->

## 生态周边

|项目|版本|描述|状态|
|--|--|--|--|
|[客户端](https://github.com/Sanzro-Lee/HELPER_FACTION_official_weapp_customer)|v1.5|叫到帮小程序客户端|未完成 ❎|
|[服务端](https://github.com/Sanzro-Lee/HELPER_FACTION_official_weapp_service)|v2.0|叫到帮小程序服务端|未完成 ❎|
|[后台系统](https://github.com/Sanzro-Lee/HELPER_FACTION_official_background_management_system)|v1.5|叫到帮后台系统|未完成 ❎|
|[官方网站源码](https://github.com/Sanzro-Lee/HELPER_FACTION_official_website)|v2.0|叫到帮官网源代码|已完成 ✅|
