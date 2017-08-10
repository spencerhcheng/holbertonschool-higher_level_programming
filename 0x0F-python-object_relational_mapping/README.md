## 0x0F. PYTHON - OBJECT RELATIONAL MAPPING

![Object relational mapping](https://image.slidesharecdn.com/orm-131102000642-phpapp01/95/orm-objectrelational-mapping-2-638.jpg?cb=1383350998)

#### AUTHOR
Spencer Cheng: [github account](https://github.com/spencerhcheng), [twitter](https://twitter.com/spencerhcheng)

#### ENVIRONMENT
All files are written and compiles on `Ubuntu 14.04 LTS`. The first line of python scripts will be exactly `#!/usr/bin/python3`. Bash scripts are checked using 
PEP8.

### OBJECTIVES
Learning points:
visual
ewafi
* Using MySQLdb to connect to a MySQL database to execute SQL queries
* Linking to a MySQL database from a Python script
* How to `SELECT` rows in a MySQL table from a Python script
* How to `INSERT` rows in a MySQL table frm a Python script
* How to map a Python Class to a MySQL table

#### Install of MySQLdb Module:

```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.__version__ 
'1.3.10'
```

#### Install of SQLAlchemy Module:

```
$ pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.1.6'
```
