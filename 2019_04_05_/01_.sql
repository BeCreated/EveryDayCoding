

-- 找到最贵物品的编号，销售商，价格
SELECT article, dealer, price FROM shop 
WHERE price=(SELECT MAX(price) FROM shop);
-- 从shop中选择 ，pirce最大的


SELECT article, dealer, price FROM shop 
ORDER BY price DESC LIMIT 1;
-- 以price排序，限制1条记录


-- 每项物品的最高价格是多少？
SELECT article, MAX(price) AS price FROM shop 
GROP BY article;


-- 拥有某字段的组间最大的行
SELECT article, dealer, price FROM shop s1 
WHERE price=(SELECT MAX(s2.price) FROM shop s2 
    WHERE s1.article=s2.article);


-- 用户变量
SELECT @min_price:=MIN(price), @max_price:=MAX(price) FROM shop;
SELECT * FROM shop WHERE price=@min_price OR price=@max_price;



-- 外键查询
SELECT s.* FROM person p, shirt s 
WHERE p.name LIKE 'Lilianna%' AND
    s.owner=p.id AND
    s.color <> 'white';


SELECT field1_index, field2_index FROM test_table
WHERE field1_index = '1' OR field2_index = '1';


SELECT field1_index, field2_index FROM test_table
WHERE test_table WHERE field1_index = '1'
UNION
SELECT field1_index, field2_index FROM test_table
WHERE field2_index WHERE field2_index = '1';


-- 根据天计算访问量

SELECT year, month, BIT_COUNT(BIT_OR(1<<day)) AS days
FROM t1 GROUP BY year, month;

