# from DataBaseConfig import connlocal, cursor
from DataBaseConfig import connserver, cursor

# conn = connlocal
conn = connserver
# 获得游标对象，一个游标对象可以对数据库进行执行操作


# 新建用户
def create_user(openid: str, username: str, region: str, address: str):
    idsql = """SELECT * FROM users where openid = %s"""
    idparams = (openid,)
    cursor.execute(idsql, idparams)
    conn.commit()
    rows = cursor.fetchall()
    if rows:
        return -1
    else:
        sql = """INSERT INTO users (openid, username, region, address) VALUES (%(openid)s, %(username)s, %(region)s, %(address)s)"""
        params = {
            'openid': openid,
            'username': username,
            'region': region,
            'address': address
        }
        try:
            cursor.execute(sql, params)
            conn.commit()
        except Exception as e:
            conn.rollback()
        else:
            conn.commit()


# 删除用户
def delete_user(openid: str):
    sql = """delete from users where openid = %s"""
    params = (openid,)
    try:
        cursor.execute(sql, params)
        conn.commit()
    except Exception as e:
        conn.rollback()
    else:
        conn.commit()


# 更改用户
def update_user(openid: str, username: str, region: str, address: str):
    sql = """UPDATE users SET username=%(username)s, address=%(address)s, region=%(region)s WHERE openid=%(openid)s"""
    params = {
        "username": username,
        "address": address,
        "region": region,
        "openid": openid
    }
    try:
        cursor.execute(sql, params)
        conn.commit()
    except Exception as e:
        conn.rollback()
    else:
        conn.commit()


# 按条件查找用户
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
        conn.rollback()
    else:
        conn.commit()


# 查询所有用户
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
        conn.rollback()
    else:
        conn.commit()


# 创建表
def create_user_table():
    sql = """
        CREATE TABLE users(
            openid varchar(30) PRIMARY KEY,
            username varchar(20),
            region varchar(10),
            address varchar(30)
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
