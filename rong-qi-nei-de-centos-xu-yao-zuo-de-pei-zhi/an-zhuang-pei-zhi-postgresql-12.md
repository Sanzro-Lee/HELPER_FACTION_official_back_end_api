---
description: PostgreSQL 12 配置
---

# 安装 & 配置 PostgreSQL 12

### 1. 安装 & 配置`PostgreSQL 12`

记得在 `sql shell` 里面的命令，结尾都要加上 `;` 分号。

```bash
# 先安装 yum 的下载源，即安装 epel-release，
# 下载之后，就可以直接跳到 安装 PostgreSQl 12 那一步

#（还有其它的国内源请看：https://www.jianshu.com/p/541c737bc947）

yum -y install epel-release

# 如果选择不安装 yum 下载源 则使用下面的命令
yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm

# 安装 PostgreSQL 12
yum install -y postgresql12 postgresql12-server

# 初始化数据库
/usr/pgsql-12/bin/postgresql-12-setup initdb 

# 启动PostgreSQL服务
systemctl start postgresql-12

# 设置 PostgreSQL 服务为开机启动
systemctl enable postgresql-12

# 查看 PostgreSQL 服务状态
systemctl status postgresql-12

# 进入 PostgreSQL 命令行
su postgres

# 启动SQL Shell
psql
```

**!重要!，此时先不要退出 `sql shell`！接下来，可输入 `\l` 查看 `DataBase` 的 `Encoding`，假若 `Encoding` 不为 `UTF8`，插入中文值到数据库的时候，会出错！**

**请先不要急着卸载或执行破坏性命令（血与泪的教训），请按照顺序执行下面的命令，以更改 `DataBase` 的 `Encoding`。**

**这些命令全都要在 `SQL Shell` 里面执行！记得 `;` 分号结尾，如果还是忘了，按 ctrl / command + c 可以退回到初始状态。**

```sql
# 先切换 DataBase
\c template0;

# 将 template1 的 datistemplate 改为 false
update pg_database set datistemplate = FALSE where datname = 'template1';

# 删除 template1 DataBase
drop database template1;

# 重新创建 template1 DataBase 以 UTF8 编码
create database template1 with encoding = 'UTF8' LC_CTYPE = 'en_US.UTF-8' LC_COLLATE = 'en_US.UTF-8' template = template0;

# 重新将 template1 的 datistemplate 改为 true
update pg_database set datallowconn = TRUE where datname = 'template1';

# 接下来切换到 template1 Database
\c template1;

# 重复步骤，修改 template0 的 datistemplate
update pg_database set datistemplate = FALSE where datname = 'template0';

# 删除 template0 DataBase
drop database template0;

# 重新创建 template0 DataBase 以 UTF8 编码
create database template0 with encoding = 'UTF8' LC_CTYPE = 'en_US.UTF-8' LC_COLLATE = 'en_US.UTF-8' template = template1;

# 重新将 template0 的 datistemplate 改为 true
update pg_database set datallowconn = TRUE where datname = 'template0';
```

**!重要!，切勿真的删除 `template0` & `template1` 这两个数据库**

```sql
# postgres 数据库，重复以上步骤，即可把 Encoding 改为 UTF8，不再赘述注释

\c template1;

update pg_database set datistemplate = FALSE where datname = 'postgres';

drop database template0;

create database postgres with encoding = 'UTF8' LC_CTYPE = 'en_US.UTF-8' LC_COLLATE = 'en_US.UTF-8' template = template0;

update pg_database set datallowconn = TRUE where datname = 'postgres';

\c postgres;

# 再次输入 \l 查看 Encoding，确保修改成功。
```

当执行了破坏性命令，例如：`yum remove postgresql12 postgresql12-server`。

并重新执行了`yum install postgresql12 postgresql12-server`后，执行初始化数据库命令时会出错，

即当在`[root@xxx /]#`状态下执行 `/usr/pgsql-12/bin/postgresql-12-setup initdb` 命令时会出现，**该文件夹 📁 不为空的报错**。

此时需执行：`rm -rf /var/lib/pgsql/12/data/` 删除该文件夹。

然后重新执行 `/usr/pgsql-12/bin/postgresql-12-setup initdb` 命令即可。

```sql
# 修改 postgres 数据库密码
ALTER USER postgres WITH PASSWORD 'NewPassword';
```

**!重要!，允许所有 IP 访问，我的配置**

```bash
# 修改配置文件
vi /var/lib/pgsql/12/data/pg_hba.conf

# 将 ipv4 下面的内容改为
# IPv4 local connections:
host    all             all               127.0.0.1/32          trust

# 重启 postgresql-12 服务，注意⚠️一定要带上 -12
systemctl restart postgresql-12

# 如果需要退出 postgres=# 或 bash-4.2$ 的状态
直接输入 exit 按回车即可。
```

`PostgreSQL 12` 安装 & 配置完毕

`PostgreSQL` 修改数据库编码方式代码源自🔗：[https://www.jianshu.com/p/62893363b0d2](https://www.jianshu.com/p/62893363b0d2)

更详细的信息可点击此链接🔗（大部分内容也源自此链接）：[https://ken.io/note/centos7-postgresql12-install-and-configuration](https://ken.io/note/centos7-postgresql12-install-and-configuration)

