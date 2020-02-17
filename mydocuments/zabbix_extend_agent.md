# Number of Mysql thread
:example

UserParameter=mysql.threads,/opt/mysql-5.7/bin/mysqladmin --login-path=local --socket=/opt/mysql-5.7/mysql.sock -h 10.127.0.3 -uroot -p'!@#$QAZX' status|cut -f3 -d":"|cut -f1 -d"Q"


# How is work
Syntax:

UserParameter = some.key[*], somescripts.sh $1 $2
*: Unlimited number of item start with some.key


mysql_threads.sh
---
#! /bin/bash
export MYSQL_PWD='!@#$QAZX'
MYSQL_DIR='/opt/mysql-5.7'
MYSQL_SOCK='/opt/mysql-5.7/mysql.sock'

$MYSQL_DIR/bin/mysqladmin --socket $MYSQL_SOCK -u root status |cut -f3 -d":"|cut -f1 -d"Q"

UserParameter=mysql.threads[*], /opt/zabbix-server-3.2.11/UserParameter_Scripts/mysql_threads.sh

# Create item on zabbix
name: Mysql Threads
key: mysql.thead[1]

# Shell parameter
UserParameter=mysql.threads[mysql_user, mysql_pass],mysqladmin -u$1 -p$2 status|cut -f3 -d":"|cut -f1 -d"Q"
$1 -> mysql_user
$2 -> mysql_pass