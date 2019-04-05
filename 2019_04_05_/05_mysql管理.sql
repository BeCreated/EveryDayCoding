

-- 修改密码
-- mysqladmin -u root password '123456'


-- 重新加载授权表
-- mysqladmin -u root -p reload

-- 
-- mysqladmin -u root -p version


-- 
-- mysqladmin -u root -p ping


-- 备份
-- mysqldump [options] db_name [tbl_name]

-- mysqldump [options] --detabases 
-- 


-- 备份
-- mysqldump -u root -p --host='127.0.0.1' --opt python_db > test.sql

-- 还原
-- mysql -u root -p [dbname] < backup.sql


