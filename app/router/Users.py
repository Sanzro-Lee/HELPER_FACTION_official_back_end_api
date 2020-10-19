#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/18
# @Author  : Sanzro Lee
# @Contact : sanzrolee@gmail.com
# @File    : Users.py
# @Software: PyCharm
"""
用户数据交互
"""

from fastapi import APIRouter
# 用户类，用于校验数据
from app.utils.custom_model import User
# 获得游标对象，一个游标对象可以对数据库进行执行操作
from app.router.DataBaseConfig import conn, cursor

router = APIRouter()



# 创建用户表
@router.get("/api/user/createtable", summary="创建用户数据表")
def create_user_table():
    sql = """
        CREATE TABLE users(
            openid varchar(30) PRIMARY KEY,
            username varchar(20),
            region varchar(30),
            address varchar(40)
        );
    """
    try:
        cursor.execute(sql)
        print("user table created successfully")
        conn.commit()
    except Exception as e:
        conn.rollback()
    else:
        conn.commit()


# 新建用户
@router.post("/api/user/create", summary="新建用户")
# async def create_user(openid: str, username: str, region: str, address: str):
async def create_user(user: User):
    idsql = """SELECT * FROM users where openid = %s"""
    idparams = (user.openid,)
    cursor.execute(idsql, idparams)
    conn.commit()
    rows = cursor.fetchall()
    if rows:
        return -1
    else:
        sql = """INSERT INTO users (openid, username, region, address) VALUES (%(openid)s, %(username)s, %(region)s, %(address)s)"""
        params = {
            'openid': user.openid,
            'username': user.username,
            'region': user.region,
            'address': user.address
        }
        try:
            data = cursor.execute(sql, params)
            conn.commit()
            return data
        except Exception as e:
            data = conn.rollback()
            return data
        else:
            conn.commit()


# 删除用户
@router.post("/api/user/delete", summary="删除用户")
async def delete_user(openid: str):
    sql = """delete from users where openid = %s"""
    params = (openid,)
    try:
        data = cursor.execute(sql, params)
        conn.commit()
        return data
    except Exception as e:
        data = conn.rollback()
        return data
    else:
        conn.commit()


# 更改用户
@router.post("/api/user/update", summary="更新用户信息")
# async def update_user(openid: str, username: str, region: str, address: str):
async def update_user(user: User):
    sql = """UPDATE users SET username=%(username)s, address=%(address)s, region=%(region)s WHERE openid=%(openid)s"""
    params = {
        "username": user.username,
        "address": user.address,
        "region": user.region,
        "openid": user.openid
    }
    try:
        data = cursor.execute(sql, params)
        conn.commit()
        return data
    except Exception as e:
        data = conn.rollback()
        return data
    else:
        conn.commit()


# 按条件查找用户
@router.post("/api/user/find", summary="查找特定用户")
def find_user(openid):
    # sql语句 建表
    sql = """SELECT * FROM users where openid = %s;"""
    # 执行语句
    # params = (username, address)
    params = (openid,)
    try:
        cursor.execute(sql, params)
        # 抓取
        rows = cursor.fetchall()
        # 事物提交
        conn.commit()
        return rows
    except Exception as e:
        data = conn.rollback()
        return data
    else:
        conn.commit()


# 查询所有用户
@router.get("/api/user/searchall", summary="查找所有用户")
def search_all_user():
    # sql语句 建表
    sql = """SELECT * FROM users;"""
    try:
        # 执行语句
        cursor.execute(sql)
        # 抓取
        rows = cursor.fetchall()
        # 事物提交
        conn.commit()
        return rows
    except Exception as e:
        data = conn.rollback()
        return data
    else:
        conn.commit()
