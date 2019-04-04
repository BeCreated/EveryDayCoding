

-- 创建表
CREATE TABLE table_name(
);


CREATE TABLE IF NOT EXISTS `t_test`(
    `id` INT UNSIGNED AUTO_INCREMENT,
    `title` VARCHAR(100) NOT NULL,
    `author` VARCHAR(40) NOT NULL,
    `date` DATE,
    PRIMARY KEY (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- 删除表
DROP TABLE table_name;


