---
description: 操作数据库问题解决
---

# 可能存在的 Psycopg2 操作 PostgreSQL 数据库问题

### 4. 可能存在的 `Psycopg2` 操作 `PostgreSQL` 数据库问题

如果没有 `import psycopg2.extras` & `cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)` 这段代码。

你的 `/searchall/staff` 请求的返回值，就不会以键值对的形式返回给前端。

**以下内容你可以忽略**

当初我为了这个问题，“学习了”下 `PostgreSQL` `json` & `jsonb` 数据类型的操作，`jsonb` 的读取性能更快（比 `json` 快很多很多倍，但是顺序会乱）

下面放一下 `jsonb` 的 数据库命令 操作，即，直接在 `sql shell` 中执行的命令

```sql
# postgresql jsonb 增删改查 知识点记录 📝 （注意！是jsonb）：

# 在 sql shell 创建表：
CREATE table test_jsonb(id int, info jsonb);

# 增：
insert into test_jsonb values(2, '{"company":"sanzro design", "name":"sanzro", "career":"Full Stack Engineer"}');

# 删（暂时不知道如何通过jsonb去删除整个元素）：
delete from test_jsonb where id = 2;

# 改：
update test_jsonb set info = info||'{"company":"sanzro design"}' WHERE id = 2;

# 查：
select * from test_jsonb where info @> '{"company":"sanzro design"}';
# 查询 id
select * from test_jsonb where id=2;
```

还有如果你需要 `id` 自增，则创建表的时候将 `id` 配置为 `serial`：

```sql
CREATE TABLE test_jsonb (
    id SERIAL PRIMARY KEY,
    info jsonb
);
```

当 `id` 为自增时，其它不变，插入数据变为：

```sql
insert into test_jsonb (info) values('{"company":"sanzro design", "name":"sanzro", "career":"Full Stack Engineer"}');
```

## 其它遇到的问题

后端解密小程序函数

**!重要!，需要 `pip install pycryptodome` ，上文有提及**  
  
 如果依旧无法使用，请参考此链接🔗：从 “警告：请勿使用 `pycrypto`” 看起：[https://qastack.cn/programming/19623267/importerror-no-module-named-crypto-cipher](https://qastack.cn/programming/19623267/importerror-no-module-named-crypto-cipher)

```python
# 示例代码
from fastapi.encoders import jsonable_encoder

@app.post('/code')
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
```

