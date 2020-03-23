sql_table='''
create table `history`(
`ds` datetime NOT NULL COMMENT '日期',
`confirm` int(11) DEFAULT NULL COMMENT '累计确诊',
`confirm_add` int(11) DEFAULT NULL COMMENT '当日新增确诊',
`suspect` int(11) DEFAULT NULL COMMENT '剩余疑似',
`suspect_add` int(11) DEFAULT NULL COMMENT '当日新增疑似',
`heal` int(11) DEFAULT NULL COMMENT '累计治愈',
`heal_add` int(11) DEFAULT  NULL COMMENT '当日新增治愈',
`dead` int(11) DEFAULT NULL COMMENT '累计死亡',
`dead_add` int(11) DEFAULT NULL COMMENT '当日新增死亡',
PRIMARY KEY (`ds`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
'''
sql_table1='''
create table `details`(
`id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
`update_time` datetime default null comment'数据最后跟新时间',
`province` varchar(50) default null comment '省',
`city` varchar(50) default null comment '市',
`confirm` int(11) DEFAULT NULL COMMENT '累计确诊',
`confirm_add` int(11) DEFAULT NULL COMMENT '新增确诊',
`heal` int(11) DEFAULT NULL COMMENT '累计治愈',
`dead` int(11) DEFAULT NULL COMMENT '累计死亡'
)  ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
'''
sql_table2='''
create table`hotsearch`(
`id` int(11) not null auto_increment,
`dt` datetime default null on update current_timestamp,
`content` varchar(255) default null,
primary key(`id`)
)engine=innoDB default charset=utf8mb4
'''