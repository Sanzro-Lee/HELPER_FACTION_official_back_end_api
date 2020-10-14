import psycopg2

# 本地端获得链接
# conn = psycopg2.connect(database="postgres", user="postgres", password="S@,|RhfU($Q&_c6FkNy[", host="127.0.0.1", port="5433")

# 服务器端获得链接
conn = psycopg2.connect(database="postgres", user="postgres", password="S@,|RhfU($Q&_c6FkNy[", host="127.0.0.1", port="5432")

# 获得游标对象，一个游标对象可以对数据库进行执行操作
cursor = conn.cursor()


# 新建用户
def create_user(id: str, username: str, password: str):
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


# 删除用户
def delete_user(id: str):
    sql = """delete from  staff where id = %s  """
    params = (id,)
    try:
        cursor.execute(sql, params)
        conn.commit()
    except Exception as e:
        conn.rollback()
    else:
        conn.commit()


# 更改用户
def update_user(id: str, username: str, password: str):
    sql = """UPDATE staff set username = %s and password = %s where id = %s"""
    params = (username, password, id)
    try:
        cursor.execute(sql, params)
        conn.commit()
    except Exception as e:
        conn.rollback()
    else:
        conn.commit()


# 按条件查找用户
def find_user(username, password):
    # sql语句 建表
    sql = """SELECT * FROM staff where username = %s and password = %s;"""
    # 执行语句
    params = (username, password)
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
    sql = """SELECT * FROM staff;"""
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
    sql = """CREATE TABLE user(
                id varchar(11) PRIMARY KEY,
                username varchar(20),
                region varchar(3),
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


# 关闭数据库连接
def close_database():
    cursor.close()
    conn.close()
