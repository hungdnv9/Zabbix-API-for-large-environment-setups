# Monitoring log file
# Example 
/var/log/message

[root@vultr: ~]# ll  /var/log/messages
-rw------- 1 root root 2092674 Feb 13 11:04 /var/log/messages


# Create group, add zabbix into group, change group
usermod -a -G adm zabbix
chmod g+r /var/log/messages
chgrp adm /var/log/messages

[root@vultr: ~]# ll  /var/log/messages
-rw-r----- 1 root adm 2095378 Feb 13 11:06 /var/log/messages


# Create item
name: Found Error string in $1
type: active check (only support it)
key: log[/var/log/messages,error] -> systax: log[/path/file.log, string]

Test: 
$ logger error


# Create trigger
{Zabbix server:log[/var/log/messages,error].logsource(error)}=0  --> found error string in 

-> the trigger will always retain the status error

fix:
{<Zabbix server>:log[/var/log/messages,error].nodata(120)}=0 -> affter 120s, if not found "error" string, it clear trigger
To solve this problem, we made use of the nodata function. This function makes it possible for Zabbix to monitor our log file and reset it's status back to normal if no new errors were received for 300 seconds.

