#### 项目的架构

- [ ] 数据获取
- [x]  数据存储
- [ ]  flask web 后台
- [ ]  数据可视化
- [ ]  echarts

####  基本知识点

- Y M 对单元格的转换

- A B 插入单元格

- DD 删除单元格

-  *+- 后边跟一个空格进行换行

-  两个空格换行

####  爬虫概述

- urllib urllib3 requests  是请求库

- re  beautifulsoup 是内容解析库

  <img src="C:\Users\11928\Desktop\疫情可视化\images\爬虫1.png" style="zoom:50%;" />

  

![数据表示](images\数据表示.png)

#### 数据库的相关问题处理

```sql
desc history 对数据库中的表进行显示
cast( sum( num) as signed) 可以对数据decimal 转换为其他的类型
replace  如果数据存在则进行update 操作， 如果数据不存在就执行insert 操作
```

- 字符串和元组之间的转换，如果不进行分割， 就需要在后边加上，

####  flask 框架 

-  返回的时候必须使用f  {}来传递变量
- ?name=zhangsan&pwd=good html 使用？传递参数，&来传递多个参数
-  action 可以实现页面的重定向
- 返回页面的时候必须要使用templates 的文件中存放的html文件

#### ajax

- 可以修改网页的局部元素

- 使用jquery 矿建可以方便编写ajax代码，

- 但是要注意修改访问的方法

  ##### ajax的操作
  
  - 后台写路由， 前台写ajax 然后调用路由函数 然后设置输出格式$("#tim").html(data)

#### html

```html
<html>
<head>	
<body>	
选择不同的设计模式，absolute 表明独占模式
```

- top是距离页面顶端的位置

- left 是距离左边的额宽度 定义最开始的一个像素点的位置

- width 和height 是块的大小， 设置浮动的大小

- display flex 弹性布局

- css中的# 表示对数据的id .num 表示数据的class

- TypeError: Object of type Decimal is not JSON serializable

- json 的shuju格式不能对十进制文件序列化

-  <div id="main" style="width: 500px; height :800px;" >  </div> 中存在的 设置dom容器必须设置固定的高度和宽度

####  echarts

- 下载对应的js文件
- 设置对应的div 容器
- 初始化echarts.init dom
- setoption (初始化的对象)
- 同时设置的div 对象必须在script的前面
- 

####  生产模式 部署项目

- WSGI 应用服务器搭配ngin![数据库配置文件](images\数据库配置文件.png)x 作为反向代理， 

- 常用的配置有gunicorn   ，uwsgi

![反向代理](images\反向代理.png)![反向代理](images\反向代理配置.png)





####  安装  chrome  

```bash
cd  /etc/yum.repos.d/ #打开centos的yum文件夹
yum -y install wget #安装wget工具
wget  http://mirrors.aliyun.com/repo/Centos-7.repo #用wget下载repo文件
mv  CentOS-Base.repo CentOS-Base.repo.bak #备份系统原来的repo文件
mv Centos-7.repo CentOS-Base.repo #替换系统原来的repo文件
yum clean all
 
yum makecache
 
yum update

yum install https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm

//使用命令查看安装的chrome 版本
sudo yum info google-chrome-stable

已安装的软件包
名称    ：google-chrome-stable
架构    ：x86_64
版本    ：80.0.3987.132
发布    ：1
大小    ：213 M
源    ：installed
来自源：/google-chrome-stable_current_x86_64
简介    ： Google Chrome
网址    ：https://chrome.google.com/
协议    ： Multiple, see https://chrome.google.com/
描述    ： The web browser from Google

// 安装对应的chrome driver

yum.repos.d

然后进行解压
unzip chromedriver_linux64.zip
```

#### 创建虚拟的环境

- pip3 install virtualenv   安装
-  进入相关目录  cd  /home/flask
- virtualenv  env
- source    env/bin/activate   激活环境

默认的域yum中没有 nginx   需要 自己添加:

```perl
rpm -ivh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm

yum repolist   查看中间的包
```

#### nginx 的配置

- 走了好多弯路 ，  主要是宝塔面板和  主机的自动配置环境有冲突问题

```
 cd  当前目录
 #### 配置 一些nginx 的
yum -y install gcc
pcre是一个perl库，包括perl兼容的正则表达式库，nginx的http模块使用pcre来解析正则表达式，所以需要安装pcre库。
yum install -y pcre pcre-devel
yum install -y zlib zlib-devel
yum install -y openssl openssl-devel

#### 下载 从官网下载
wget http://nginx.org/download/nginx-1.9.9.tar.gz  
### 解压
tar -zxvf  nginx-1.9.9.tar.gz

进入到解压的目录


./configure
 
make
 
make install

切换到/usr/local/ nginx 目录
找到 conf 中的nginx.conf 文件

找到nginx  中的sbin 文件 然后启动可执行文件
### 配置的目录是usr/nginx


```

#### guncron

gunicorn -b 127.0.0.0.1:8080  -D app:app



ps -ef  |  grep gunicorn



#### 停止nginx

- ls - i ：80
- kill -9
- ./ nginx -s stop

只用设置 proxy_pass  地址就可以了



#### 数据库知识总结

```
-  insert 有三种方式进行替换
 最简单的是 replace  
 然后还有dupliacte    赋值
 
```

