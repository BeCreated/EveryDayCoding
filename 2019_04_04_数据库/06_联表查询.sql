

SELECT 字段 FROM t1, t2 WHERE t1.col = t2.col AND
-- 从t1，t2 中选择


SELECT a.id, a.name, a.address, a.date, b.math
FROM t1 AS b, t2 AS a WHERE a.id=b.id;
-- 从t1，t2中选择是t1和t2中id相等。


SELECT a.id, a.name, a.address, b.math 
FROM t1 a, t2 b 
WHERE a.id=b.id AND b.id='$_POST[textid]'


SELECT id, name, pwd FROM t1 UNION 
SELECT uid, price, date FROM t2 ;


SELECT id, name, sex, date FROM t1 
WHERE id in (SELECT id  FROM t2 WHERE id='$_POST[test]')



