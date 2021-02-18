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

import sys
sys.path.insert(0, '/tmp/HELPER_FACTION_official_back_end_api/app/api/v1/')
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from Users import Users
# from Orders import Orders
# from Staffs import Staffs
# from DataBaseConfig import DataBaseConfig
# from MiniProgremCode import MiniProgremCode

from app.api.v1.Users import Users
from app.api.v1.Orders import Orders
from app.api.v1.Staffs import Staffs
from app.api.v1.DataBaseConfig import DataBaseConfig
from app.api.v1.MiniProgremCode import MiniProgremCode
from app.api.v1.Pictures import Pictures
from app.api.v1.Test import Pictest

# 服务器端配置
app = FastAPI(
    openapi_url="/api/data_manger.json",
    docs_url="/api/docs",
    redoc_url="/api/redocs"
)

app.include_router(Users.router, tags=["用户数据 API"])
app.include_router(Orders.router, tags=["需求数据 API"])
app.include_router(Staffs.router, tags=["员工数据 API"])

app.include_router(Pictures.router, tags=["图片 API"])
app.include_router(Pictest.router, tags=["图片测试 API"])
app.include_router(DataBaseConfig.router, tags=["关闭数据库连接"])
app.include_router(MiniProgremCode.router, tags=["小程序获取 OPENID"])

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
