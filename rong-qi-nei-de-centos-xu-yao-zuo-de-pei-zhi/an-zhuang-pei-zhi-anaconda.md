---
description: Anaconda 配置
---

# 安装 & 配置 Anaconda

### 2. 安装 & 配置 `Anaconda`

以下内容大部分来自此链接🔗 ：[https://juejin.im/post/6854573222273220621](https://juejin.im/post/6854573222273220621)

```bash
# 下载 wget
yum -y install wget

# 配置 下载源
yum -y install perl

# 下载 Anaconda
wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh

# 安装 Anaconda
bash Anaconda3-5.3.1-Linux-x86_64.sh

# 进入安装程序，提示输入“ENTER”继续：
Please, press ENTER  to continue
>>> ENTER

# 输入yes确认接受许可协议
Do you accept the license terms? [yes|no]
[no] >>> yes

# 确认Anaconda的安装位置, 可改可不改
Anaconda3 will now be installed into this location:/root/anaconda3  - 
Press ENTER to confirm the location  - Press CTRL-C to abort the installation  - 
Or specify a different location below[/root/anaconda3] >>> /opt/anaconda3

# 安装完成后，出现询问是否在用户的.bashrc文件中初始化Anaconda3的相关内容，此处选 yes
Do you wish the installer to initialize Anaconda3by running conda init? [yes|no][no] >>> yes
```

安装完成 ✅ ，`Anaconda` 的一些基础命令：

```bash
# 执行下：source ~/.bashrc，
# 使用 conda 命令时就不会报 conda command not found 了

# 创建一个 Python3.7 版本的虚拟环境
conda create --name fastapienv python=3.7

# 删除虚拟环境命令
conda remove -n fastapienv --all

# 激活虚拟环境，可直接激活虚拟环境，无需先停用当前虚拟环境
conda activate fastapienv

# 停用虚拟环境
conda deactivate fastapienv

# 查看当前虚拟环境已安装的包
conda list

# conda 安装包命令，假如是安装 fastapi
conda install fastapi

# 当 conda install 无法安装某个包时，通过查询 pip 的路径，
# 如果有显示当前虚拟环境名，则可以使用 pip 安装 Python 包，看是否能装上

whereis pip
pip install fastapi

# 如果 pip install / coonda install 都无法安装，则需要下载源码包，使用命令解压安装。
```

解决每次进入虚拟机时，`Anaconda` 虚拟环境皆为 `base` 的问题 （源自此链接🔗：[https://www.cnblogs.com/alphacode/p/13760470.html）](https://www.cnblogs.com/alphacode/p/13760470.html）)

```bash
# 修改 ~/.bash_profile 文件，有时 ~/.bashrc 文件里也会有此配置

export PATH="~/anaconda/envs/your_env_name/bin:$PATH"
# your_env_name 是你自定义的环境名

# 修改 ~/.bashrc 文件

conda activate your_env_name
# "your_env_name"就是你的环境名

# 更新配置
source ~/.bashrc
source ~/.bash_profile

# 设置好后，返回到刚进入虚拟机的状态 [root@xxx /]#，
# 执行以下命令以停止 base 虚拟环境自启动
conda config --set auto_activate_base false
```

我的配置:

```bash
# vi ~/.bashrc

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/root/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/root/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/root/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/root/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
conda activate fastapienv
# <<< conda initialize <<<

# vi ~/.bash_profile

# PATH=$PATH:$HOME/bin
PATH="~/anaconda3/envs/fastapienv/bin:$PATH"
export PATH
export LANG="en_US.UTF-8"
```

`Anaconda` 配置完毕

我的 `Anaconda` 虚拟环境 `fastapienv` 还需要安装的包

```text
# 除了基本的包以外

还安装了：
fastapi
uvicorn
psycopg2

# 小程序解密用
pycryptodome
```

