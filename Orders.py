# from DataBaseConfig import connlocal, cursor
from DataBaseConfig import connserver, cursor

# conn = connlocal
conn = connserver
# 获得游标对象，一个游标对象可以对数据库进行执行操作


# 新建需求
def create_order(orderid: str, createuser: str, orderaddress: str, orderphonenum: str, createdate: str, starttime: str,
                 endtime: str, ordertype: int, orderdesc: str, orderprice: float, orderrate: float, orderpic: str):
    idsql = """SELECT * FROM orders where orderid = %s"""
    idparams = (orderid,)
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
            'orderid': orderid,
            'createuser': createuser,
            'orderaddress': orderaddress,
            'orderphonenum': orderphonenum,
            'createdate': createdate,
            'starttime': starttime,
            'endtime': endtime,
            'ordertype': ordertype,
            'orderdesc': orderdesc,
            'orderprice': orderprice,
            'orderrate': orderrate,
            'orderpic': orderpic,
        }
    try:
        cursor.execute(sql, params)
        conn.commit()
    except Exception as e:
        conn.rollback()
    else:
        conn.commit()


# 删除需求
def delete_order(orderid: str):
    sql = """delete from  orders where orderid = %s  """
    params = (id,)
    try:
        cursor.execute(sql, params)
        conn.commit()
    except Exception as e:
        conn.rollback()
    else:
        conn.commit()


# 更改需求
def update_order(orderid: str, username: str, password: str):
    sql = """UPDATE orders set username = %s and password = %s where orderid = %s"""
    params = (username, password, orderid)
    try:
        cursor.execute(sql, params)
        conn.commit()
    except Exception as e:
        conn.rollback()
    else:
        conn.commit()


# 按条件查找需求
def find_order(orderid):
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
    else:
        conn.commit()


# 查询所有需求
def search_all_order():
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
    else:
        conn.commit()


# 创建需求表
def create_order_table():
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
        cursor.execute(sql)
        print("order table created successfully")
        conn.commit()
    except Exception as e:
        conn.rollback()
    else:
        conn.commit()
