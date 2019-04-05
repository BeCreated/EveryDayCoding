
-- 聚合查询

SELECT COUNT(*) FROM shop;

SELECT COUNT(*) AS total FROM shop;

SELECT stuName, COUNT(*) AS total FROM grade
GROUP BY stuName;

-- 求和， SUM
SELECT stuName, SUM(grade) FROM grade WHERE stuName='小王';

SELECT stuName, SUM(grade) FROM grade WHERE BY stuName;

-- 求平均值， AVG
SELECT stuName, AVG(grade) FROM grade WHERE stuName='小王';


-- ASC      升序
-- DESC     降序
-- 时间查询
SELECT * FROM DB 
WHERE col BETWEEN '2017-05-10' AND '2017-05-18'
ORDER BY col DESC;

SELECT * FROM DB
WHERE col > '2017-05-10' AND col <= '2017-05-18'
ORDER BY col DESC;

SELECT * FROM db 
WHERE DATE_FORMAT(date, '%Y%m%d') 
BETWEEN '20170601' AND '20170628';

SELECT * FROM db
WHERE DATE_FORMAT(date, '%Y%m')
BETWEEN '201706' AND '201708';


-- TOP 10
SELECT id, name, img, SUM(gold) AS gold FROM db
LEFT JOIN user ON user.id=user_id 
WHERE GROUP BY user_id 
ORDER BY gold DESC 
LIMIT 0, 10;



