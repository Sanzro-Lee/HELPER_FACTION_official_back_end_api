# from DataBaseConfig import connlocal, cursor
from DataBaseConfig import connserver, cursor

# conn = connlocal
conn = connserver
# 获得游标对象，一个游标对象可以对数据库进行执行操作


# 新建员工
def create_staff(id: str, username: str, password: str):
    idsql = """SELECT * FROM staff where id = %s"""
    idparams = (id,)
    cursor.execute(idsql, idparams)
    conn.commit()
    rows = cursor.fetchall()
    print(rows)
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


# 更改员工
def update_staff(id: str, username: str, password: str):
    sql = """UPDATE staff set username = %s and password = %s where id = %s"""
    params = (username, password, id)
    try:
        cursor.execute(sql, params)
        conn.commit()
    except Exception as e:
        conn.rollback()
    else:
        conn.commit()


# 按条件查找员工
def find_staff(username, password):
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


# 查询所有员工
def search_all_staff():
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


# 创建员工表
def create_staff_table():
    sql = """CREATE TABLE IF NOT EXISTS staff(
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
