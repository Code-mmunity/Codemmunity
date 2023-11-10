CREATE TABLE userDB (
name varchar(20) not null,
nickname varchar(20) not null,
id varchar(20) not null,
password varchar(20) not null,
email varchar(40),
phone varchar(20),
PRIMARY KEY (nickname, id)
)