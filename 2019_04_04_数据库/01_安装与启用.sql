
-- 数据库的安装
-- apt-get install mysql-server
-- apt-get install mysql-client
-- apt-get install libmysqlclient-dev


-- 开启数据库服务
-- service mysql start


-- shell进入数据库
-- mysql -u root -p


-- 创建数据库
CREATE DATABASE db_name;
CREATE DATABASE IF NOT EXISTS db_name DEFAULT CHARSET utf8;


-- 删除数据库
DROP DATABASE db_name;


-- 使用数据库
USE db_name；

