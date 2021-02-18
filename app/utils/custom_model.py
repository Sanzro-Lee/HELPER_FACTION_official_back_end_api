#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/18
# @Author  : Sanzro Lee
# @Contact : sanzrolee@gmail.com
# @File    : custom_exc.py.py
# @Software: PyCharm
"""
自定义类
"""

import uuid
from pydantic import BaseModel


# 创建用户类
class User(BaseModel):
    openid: str = None
    username: str = None
    region: str = None
    address: str = None


# 创建员工类
class Staff(BaseModel):
    id: str = None
    username: str = None
    password: str = None


# 查找员工类
class FindStaff(BaseModel):
    username: str = None
    password: str = None


# 创建需求类
class Order(BaseModel):
    orderid: str = uuid.uuid1()
    createuser: str = None
    latitude: str = None
    longitude: str = None
    orderaddress: str = None
    orderphonenum: str = None
    taskmaster: str = None
    masterphonenum: str = None
    createdate: str = None
    starttime: str = None
    endtime: str = None
    ordertype: int = None
    orderdesc: str = None
    orderprice: float = None
    orderrate: float = None
    orderpic: list = None
