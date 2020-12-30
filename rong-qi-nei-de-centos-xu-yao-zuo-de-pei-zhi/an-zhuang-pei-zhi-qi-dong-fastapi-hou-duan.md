---
description: FastAPI所需配置
---

# 安装 & 配置 & 启动 FastAPI 后端

### 3. 安装 & 配置 & 启动一个 `Fastapi` 基础后端

fastapi官方中文链接🔗：[https://fastapi.tiangolo.com/zh/](https://fastapi.tiangolo.com/zh/)

**执行下面的步骤前，必须先安装好 fastapi & uvicorn & psycopg2**

```python
# 找个你喜欢的路径，（我喜欢 /tmp/） 创建 main.py 文件，键入以下代码：

from typing import Optional
from fastapi import FastAPI

# 跨域
from fastapi.middleware.cors import CORSMiddleware

import psycopg2
import psycopg2.extras

app = FastAPI()

# 跨域配置
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1",
    "http://127.0.0.1:8080",
    "*"
]

# 跨域配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# 一般都是 5432 端口，下文会提及如何查询
conn = psycopg2.connect(database="postgres", user="postgres", password="Your_Pass_Word", host="127.0.0.1", port="5432")

# 这段代码很关键，下文会解释
cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)


@app.get("/")
def read_root():
    return {"Hello": "World"}


# 创建员工数据表
@app.get("/create/stafftable")
def create_staff_table():
    sql = """
        CREATE TABLE staff(
            id varchar(11) PRIMARY KEY,
            username varchar(20),
            password varchar(50)
        );
    """
    try:
        cursor.execute(sql)
        print("staff table created successfully")
        conn.commit()
    except Exception as e:
        conn.rollback()
    else:
        conn.commit()


# 创建员工
@app.get("/create/staff")
def create_staff(id: str, username: str, password: str):
    idsql = """SELECT * FROM staff where id = %s"""
    idparams = (id,)
    cursor.execute(idsql, idparams)
    conn.commit()
    rows = cursor.fetchall()
    if rows:
        return -1
    else:
        sql = """INSERT INTO staff (id, username, password) VALUES (%(id)s,%(username)s, %(password)s)"""
        params = {'id': id, 'username': username, 'password': password}
        try:
            cursor.execute(sql, params)
            conn.commit()
        except Exception as e:
            conn.rollback()
        else:
            conn.commit()


# 删除员工
@app.get("/delete/staff")
def delete_staff(id: str):
    sql = """delete from  staff where id = %s  """
    params = (id,)
    try:
        cursor.execute(sql, params)
        conn.commit()
    except Exception as e:
        conn.rollback()
    else:
        conn.commit()


# 查找所有员工
@app.get("/searchall/staff")
def search_all_staff():
    sql = """SELECT * FROM staff;"""
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        conn.commit()
        return rows
    except Exception as e:
        conn.rollback()
    else:
        conn.commit()


# 关闭数据库连接
def close_database():
    cursor = conn.cursor()
    cursor.close()
    conn.close()
```

**!重要!，此时，我们进来 `Dokcer` 容器的那条命令就发挥作用了，我们进入的时候，映射了两个端口给虚拟机，分别是 `80` & `8011`。**

**如果你没有跑 `docker run -ti -d -p 80:80 -p 8011:8011 --privileged=true centos:7.8.2003 /usr/sbin/init` 这条命令就进入虚拟机，很抱歉，你需要回到创建 docker container 的位置重新创建...**

写好 `main.py` 后，执行以下命令：

```bash
uvicorn main:app --host 0.0.0.0 --port 8011 --reload

# 按 ctrl / command + c 可停止运行
```

此时，你在浏览器的地址栏中输入，你的物理机IP，后面加上`:8011`，就能看到 `hello world` 的提示。

IP后输入 `:8011/docs` 你还能看到 `fastapi` 为我们准备的 交互式 API 文档，你可以在里面测试连接数据库是否存在问题。

`:8011/docs` 还能进行一定的接口测试，看看返回的 Data 是否符合自己的需要。

如键入中文值存在问题，请返回到上文，看看是否是，`DataBase Encoding` 的编码问题。

**另外，如果你的 `Uvicorn` 在后台运作，而你希望重新启动，可使用以下命令让它停止运行**

```bash
# 检查端口被哪个进程占用
netstat -lnp|grep 8011

# 如果无法使用 netstat 执行：
yum install net-tools

# 查看进程的详细信息
ps 11100

# 杀掉进程
kill -9 11100

# 通常，还需再使用 netstat -lnp|grep 8011 复查
```

更多详细信息：[https://blog.csdn.net/u011389452/article/details/53982204](https://blog.csdn.net/u011389452/article/details/53982204)

