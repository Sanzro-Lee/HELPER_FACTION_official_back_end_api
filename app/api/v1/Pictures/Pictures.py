#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/22
# @Author  : Sanzro Lee
# @Contact : sanzrolee@gmail.com
# @File    : Pictures
# @Software: PyCharm
"""
图片上传、查看
"""

import shutil
from typing import List
from fastapi import Response, APIRouter, File, UploadFile

router = APIRouter()


@router.post("/api/pictures/upload", summary="上传图片")
async def upload_picture(files: List[UploadFile] = File(...)):
    # 单图片上传
    # filename = file.filename
    # temp = filename.split('.')
    # if temp[len(temp) - 1] not in ["png", "jpg"]:
    #     return {"code": 203, "msg": "不支持图片格式"}
    # else:
    #     try:
    #         res = await file.read()
    #         with open(filename, "wb") as f:
    #             f.write(res)
    #         return {"code": 200, "msg": "上传成功"}
    #     except Exception as err:
    #         return {"code": 201, "msg": err}
    # 单图片上传

    for file in files:
        with open(file.filename, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    return {"code": 200, "PicUrl": ['http://127.0.0.1:8000/api/pictures/' + file.filename for file in files]}


@router.get('/api/pictures/{filename}', summary="查看图片")
async def get_picture(filename: str):
    with open(r'{}'.format(filename), 'rb') as f:
        resp = Response(f.read())
        return resp
