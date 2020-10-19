#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/18
# @Author  : Sanzro Lee
# @Contact : sanzrolee@gmail.com
# @File    : Orders.py
# @Software: PyCharm
"""
需求数据交互
"""

from fastapi import APIRouter
# 需求类，用于校验数据
from app.utils.custom_model import Order
# 获得游标对象，一个游标对象可以对数据库进行执行操作
from app.router.DataBaseConfig import conn, cursor

router = APIRouter()


# 创建需求表
@router.get("/api/order/createtable", summary="创建需求数据表")
async def create_order_table():
    sql = """
        CREATE TABLE IF NOT EXISTS orders(
            orderid varchar(18) PRIMARY KEY,
            createuser varchar(5) NOT NULL,
            orderaddress varchar(30) NOT NULL,
            orderphonenum varchar(11) NOT NULL,
            taskmaster varchar(5),
            masterphonenum varchar(11),
            createdate varchar NOT NULL,
            starttime varchar NOT NULL,
            endtime varchar NOT NULL,
            ordertype integer NOT NULL,
            orderdesc varchar(20) NOT NULL,
            orderprice decimal NOT NULL,
            orderrate decimal,
            orderpic varchar NOT NULL
        );
    """
    try:
        data = cursor.execute(sql)
        print("order table created successfully")
        conn.commit()
        return data
    except Exception as e:
        conn.rollback()


# 新建需求
@router.post("/api/oerder/create", summary="创建需求")
async def create_order(order: Order):
    idsql = """SELECT * FROM orders where orderid = %s"""
    idparams = (order.orderid,)
    cursor.execute(idsql, idparams)
    conn.commit()
    rows = cursor.fetchall()
    print(rows)
    if rows:
        return -1
    else:
        sql = """
        INSERT INTO orders (
            orderid,
            createuser,
            orderaddress,
            orderphonenum,
            createdate,
            starttime,
            endtime,
            ordertype,
            orderdesc,
            orderprice,
            orderrate,
            orderpic
        ) VALUES (
            %(orderid)s,
            %(createuser)s,
            %(orderaddress)s,
            %(orderphonenum)s,
            %(createdate)s,
            %(starttime)s,
            %(endtime)s,
            %(ordertype)s,
            %(orderdesc)s,
            %(orderprice)s,
            %(orderrate)s,
            %(orderpic)s)
        """
        params = {
            'orderid': order.orderid,
            'createuser': order.createuser,
            'orderaddress': order.orderaddress,
            'orderphonenum': order.orderphonenum,
            'createdate': order.createdate,
            'starttime': order.starttime,
            'endtime': order.endtime,
            'ordertype': order.ordertype,
            'orderdesc': order.orderdesc,
            'orderprice': order.orderprice,
            'orderrate': order.orderrate,
            'orderpic': order.orderpic,
        }
    try:
        data = cursor.execute(sql, params)
        conn.commit()
        return data
    except Exception as e:
        conn.rollback()


# 删除需求
@router.post("/api/order/delete", summary="删除需求")
async def delete_order(orderid: str):
    sql = """delete from  orders where orderid = %s  """
    params = (orderid,)
    try:
        data = cursor.execute(sql, params)
        conn.commit()
        return data
    except Exception as e:
        conn.rollback()


# 更新需求信息
@router.post("/api/order/update", summary="更新需求信息")
def update_order(orderid: str, username: str, password: str):
    sql = """UPDATE orders set username = %s and password = %s where orderid = %s"""
    params = (username, password, orderid)
    try:
        data = cursor.execute(sql, params)
        conn.commit()
        return data
    except Exception as e:
        conn.rollback()


# 查找特定需求
@router.post("/api/order/find", summary="查找特定需求")
def find_order(orderid: str):
    # sql语句 建表
    sql = """SELECT * FROM orders where orderid = %s;"""
    # 执行语句
    params = (orderid,)
    try:
        cursor.execute(sql, params)
        # 抓取
        rows = cursor.fetchall()
        # 事物提交
        conn.commit()
        return rows
    except Exception as e:
        conn.rollback()


# 查询所有需求
@router.get("/api/order/searchall", summary="查找所有需求")
async def search_all_order():
    # sql语句 建表
    sql = """SELECT * FROM orders;"""
    try:
        # 执行语句
        cursor.execute(sql)
        # 抓取
        rows = cursor.fetchall()
        # 事物提交
        conn.commit()
        return rows
    except Exception as e:
        conn.rollback()
