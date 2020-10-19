#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/18
# @Author  : Sanzro Lee
# @Contact : sanzrolee@gmail.com
# @File    : MiniProgremCode.py.py
# @Software: PyCharm
"""
小程序数据操作
"""

from fastapi import APIRouter
# 微信小程序获取openid
import requests

# 因小程序id为测试号，所以无法获得手机号，故注释此文件
# from WXBizDataCrypt import WXBizDataCrypt

router = APIRouter()


# 微信小程序获得openid
@router.post('/api/code', summary="小程序获得openid")
def user_wxlogin(appid, secret, code):
    params = {
        'appid': appid,
        'secret': secret,
        'js_code': code,
        'grant_type': 'authorization_code'
    }
    url = 'https://api.weixin.qq.com/sns/jscode2session'
    r = requests.get(url, params=params)
    openid = r.json().get('openid', '')
    session_key = r.json().get('session_key', '')
    return {'openid': openid, 'session_key': session_key}
