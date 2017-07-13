## 0x0D SQL Introduction

![SQL](https://azure.microsoft.com/svghandler/sql-database/?width=600&height=315}

#### AUTHOR
Spencer Cheng: [github account](https://github.com/spencerhcheng), [twitter](https://twitter.com/spencerhcheng)

#### SETUP
All files are written and compiled on `Ubuntu 14.04 LTS`using `MySQL 5.7` and `vim`.

### OBJECTIVES
Learning points:
* - What is a database
* - What is ia relational databae
* - What is MySQL
* - How to create a database in MySQL
* - What does `DDL` and `DML` stand for?
* - How to `CREATE` or `ALTER` a table
* - How to `SELECT` data from a table
* - How to `INSERT`, `UPDATE` or `DELETE` data
* - What are `subqueries`
* - How to use MySQL functions

### Installation of MySQL 5.7 on Ubuntu 14.04 LTS
```
$ echo 'deb http://repo.mysql.com/apt/ubuntu/ trusty mysql-5.7-dmr' | sudo tee -a /etc/apt/sources.list
$ sudo apt-get update
$ sudo apt-get install mysql-server-5.7
...
$ mysql --version
mysql  Ver 14.14 Distrib 5.7.8-rc, for Linux (x86_64) using  EditLine wrapper
$
```

### Connecting to MySQL server:
```
$ mysql -hlocalhost -uroot -p
Password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 42
Server version: 5.7.8-rc MySQL Community Server (GPL)

Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> 
mysql> quit
Bye
$
```
