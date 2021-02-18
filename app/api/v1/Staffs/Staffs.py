#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/18
# @Author  : Sanzro Lee
# @Contact : sanzrolee@gmail.com
# @File    : Staff.py
# @Software: PyCharm
"""
员工数据交互
"""

import sys
sys.path.insert(0, '/tmp/HELPER_FACTION_official_back_end_api/app/')
sys.path.insert(0, '/tmp/HELPER_FACTION_official_back_end_api/app/api/v1/')
from fastapi import APIRouter
# 员工类，用于校验数据
# from utils.custom_model import Staff, FindStaff
from app.utils.custom_model import Staff, FindStaff
# 获得游标对象，一个游标对象可以对数据库进行执行操作
# from DataBaseConfig.DataBaseConfig import conn, cursor
from app.api.v1.DataBaseConfig.DataBaseConfig import conn, cursor
router = APIRouter()


# 创建员工表
@router.get("/api/staff/createtable", summary="创建员工数据表")
async def create_staff_table():
    sql = """CREATE TABLE IF NOT EXISTS staff(
                id varchar(11) PRIMARY KEY,
                username varchar(20),
                password varchar(50)
            );
    """
    try:
        data = cursor.execute(sql)
        print("staff table created successfully")
        conn.commit()
        return data
    except Exception as err:
        conn.rollback()
        return err


# 新建员工
@router.post("/api/staff/create", summary="新建员工")
async def create_staff(staff: Staff):
    idsql = """SELECT * FROM staff where id = %s"""
    idparams = (staff.id,)
    cursor.execute(idsql, idparams)
    conn.commit()
    rows = cursor.fetchall()
    print(rows)
    if rows:
        return -1
    else:
        sql = """INSERT INTO staff (id, username, password) VALUES (%(id)s,%(username)s, %(password)s)"""
        params = {'id': staff.id, 'username': staff.username, 'password': staff.password}
        try:
            data = cursor.execute(sql, params)
            conn.commit()
            return data
        except Exception as err:
            conn.rollback()
            return err


# 删除员工
@router.post("/api/staff/delete", summary="删除员工")
async def delete_staff(id: str):
    sql = """delete from  staff where id = %s  """
    params = (id,)
    try:
        data = cursor.execute(sql, params)
        conn.commit()
        return data
    except Exception as err:
        conn.rollback()
        return err


# 更新员工信息
@router.post("/api/staff/update", summary="更新员工信息")
async def update_staff(staff: Staff):
    sql = """UPDATE staff set username = %s and password = %s where id = %s"""
    params = (staff.username, staff.password, staff.id)
    try:
        data = cursor.execute(sql, params)
        conn.commit()
        return data
    except Exception as err:
        conn.rollback()
        return err


# 查找特定员工
@router.post("/api/staff/find", summary="查找特定员工")
async def find_staff(staff: FindStaff):
    # sql语句 建表
    sql = """SELECT * FROM staff where username = %s and password = %s;"""
    # 执行语句
    params = (staff.username, staff.password)
    try:
        cursor.execute(sql, params)
        # 抓取
        rows = cursor.fetchall()
        # 事物提交
        conn.commit()
        return rows
    except Exception as err:
        conn.rollback()
        return err


# 查询所有员工
@router.get("/api/staff/searchall", summary="查找所有员工")
async def search_all_staff():
    # sql语句 建表
    sql = """SELECT * FROM staff;"""
    try:
        # 执行语句
        cursor.execute(sql)
        # 抓取
        rows = cursor.fetchall()
        # 事物提交
        conn.commit()
        return rows
    except Exception as err:
        conn.rollback()
        return err
