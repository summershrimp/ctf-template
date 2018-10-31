#!/bin/bash
mysqld_safe &
echo -n "Waiting for mysql startup"
while ! mysqladmin --host="localhost" --silent ping ; do
    echo -n "."
    sleep 1
done
echo

mysql -uroot <<EOF
UPDATE mysql.user SET Password=PASSWORD('suCTF_P1us_1s'), plugin = '' WHERE User='root';
create database calc;
use calc;
create table user(
id INT NOT NULL AUTO_INCREMENT primary key,
username varchar(32) NOT NULL,
password varchar(32) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
insert into user values(1,'admin','aa67095d8e65d624548cb6b50bd4778e');
create table file(
id INT NOT NULL AUTO_INCREMENT primary key,
filename varchar(32) NOT NULL,
filehash varchar(32) NOT NULL,
sig varchar(120) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
create table flag(
flag varchar(120) primary key
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
insert into flag values('SUCTF{a_very_long_long_long_long_long_fake_flag_d}');

grant SELECT, INSERT on calc.user to 'suctf'@localhost identified by 'suctf';
grant SELECT, INSERT, UPDATE on calc.file to 'suctf'@localhost ;
grant SELECT on calc.flag to 'suctf'@localhost ;
FLUSH PRIVILEGES;

EOF

mysqladmin -uroot -psuCTF_P1us_1s shutdown