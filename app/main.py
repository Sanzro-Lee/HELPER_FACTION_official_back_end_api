#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/18
# @Author  : Sanzro Lee
# @Contact : sanzrolee@gmail.com
# @File    : main.py
# @Software: PyCharm
"""
主控制
"""

from fastapi import FastAPI
from app.router import Orders, DataBaseConfig, MiniProgremCode, Users, Staffs
from fastapi.middleware.cors import CORSMiddleware

# 服务器端配置
app = FastAPI(
    openapi_url="/api/data_manger.json",
    docs_url="/api/docs",
    redoc_url="/api/redocs"
)

app.include_router(Users.router, tags=["用户数据 API"])
app.include_router(Orders.router, tags=["需求数据 API"])
app.include_router(Staffs.router, tags=["员工数据 API"])

app.include_router(DataBaseConfig.router, tags=["关闭数据库连接"])
app.include_router(MiniProgremCode.router, tags=["小程序获取 openid"])

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1",
    "http://127.0.0.1:8080",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
