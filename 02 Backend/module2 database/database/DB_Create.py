from SQL_Query_Handler import *

query = "CREATE TABLE student (id int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,username varchar(10) DEFAULT NULL,monday char(96) DEFAULT NULL,tuesday char(96) DEFAULT NULL,wednesday char(96) DEFAULT NULL,thursday char(96) DEFAULT NULL,friday char(96) DEFAULT NULL,saturday char(96) DEFAULT NULL,sunday char(96) DEFAULT NULL)"

sql_query(query)
